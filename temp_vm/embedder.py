import utilities
from spektral.utils.convolution import localpooling_filter
import numpy as np
from keras.callbacks import EarlyStopping


import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

class Embedder:
    '''Embed a set of graphs in a real space.
    
    Embedder apply sequencially the models.
    Example:
        estim = [model1,model2,model3]
        
        x1 = model1.fit(graphs,targhet).transform(x1)
        x2 = model2.fit(x1, targhet).transform(x2)
        x3 = model3.fit(x2, targhet)
        
    Attributes:
        estim ([Model]): a list of models 
        
    '''

    def __init__(self, estimators,name=""):
        self.estimators = estimators
        self.name = name
        
    def fit(self,X,y):
        '''fit the data on the models.
        
              
        Args:
            X ([nx.graph]) : array of graphs
            y ([int]) : targhet
            
        Returns:
            (self)
        '''
        X_res = X
    
        
        for estimator in self.estimators[:-1]:
            X_res = estimator.fit(X_res,y).transform(X_res)
            
        
        self.estimators[-1].fit(X_res,y)
        return(self)

    def reset_state(self):
        

        for estimator in self.estimators:

            estimator.reset_state()

                

    def transform(self,graphs):
        '''Transform set of graphs in points in a space.
              
        Args:
            X ([nx.graph]) : array of graphs
            
        Returns:
            (X_res) : predicted targhet
        '''
        X_res = graphs
        
        for estimator in self.estimators:
            
            X_res = estimator.transform(X_res)
            
        return(X_res)
        

class Transformer:
    '''Contains an Estimator

    Attributes:
        estimator (Obj): an estimator
        has_fit (boolena [True]): specify if a model has the fit fucntion.
                                For example, Vectorize hasn't fit. 
        
    '''

    def __init__(self, estimator, has_fit=True):
        self.has_fit = has_fit
        self.estimator = estimator

        
    
    def fit(self,X,y,node_feature=None):
        '''Fit the model usign X and y
              
        Args:
            X ([nx.graph]) : array of graphs
            y ([int]) : array of targhets
            
        Returns:
            (self)
        '''
        if (self.has_fit == True):
            
            self.estimator.fit(X,y)
            
        return(self)

   

    def reset_state(self):
        if ("reset_state" in dir(self.estimator)):
            self.estimator.reset_state()
        return None
    
    
    def transform(self,X):
        '''Transform X in pointses_patiencece.
              
        Args:
            X ([nx.graph] or [ines_patienceay of graphs
            
        Returns:
            (X_pred) : predicted targhet
        '''



        y_pred = self.estimator.transform(X)
        return(y_pred)
        
   
class Transformer_GNN:

    def __init__(self, original_model,new_model,batch_size,validation_split,epochs,patience,verbose=0,plot=False):
        self.original_model = original_model
        self.new_model = new_model
        self.batch_size = batch_size
        self.validation_split = validation_split
        self.epochs = epochs
        self.verbose = verbose
        self.patience = patience
        
        self.initial_weights = original_model.get_weights()

        ####
        self.plot = plot


        
    def reset_state(self):
        self.original_model.set_weights(self.initial_weights)
        self.new_model.set_weights(self.initial_weights)
        
        
    def fit(self,graphs,y):
        # Preprocessing
        adj, x, _ = utilities.from_nx_to_adj(graphs)
        fltr = localpooling_filter(adj)
        y_one_hot = utilities.from_np_to_one_hot(y)
        es_callback = EarlyStopping(monitor='val_loss', patience=self.patience)
        
        ### the dataset is splitted, and the input of the model
        ### acceps max_n_nodes as impout, so if needed add a padding
        fltr, x = self.add_padding(fltr,x)

        history = self.original_model.fit([x, fltr],y_one_hot,
                                batch_size=self.batch_size,
                                validation_split=self.validation_split,
                                epochs=self.epochs,
                                callbacks=[es_callback],
                                verbose=self.verbose)
        
        if (self.plot == True):
            tmp_print(history)
        
        
        print(es_callback.stopped_epoch)
        
        ### get the weights
        self.original_weights = self.original_model.get_weights()
        ### set the weights to the new models
        self.new_model.set_weights(self.original_weights)


        return(self)
    
    
    def transform(self,graphs):
        adj, x, _ = utilities.from_nx_to_adj(graphs)
        fltr = localpooling_filter(adj)
        fltr, x = self.add_padding(fltr,x)
        y_pred = self.new_model.predict([x,fltr])

        
        return(y_pred)


    def add_padding(self,fltr,x):
        
        input_model = self.original_model.get_input_shape_at(0)
        #### pad fltr
        new_fltr = []
        if (not fltr.shape[1] == input_model[1][1]):

            pad_size = input_model[1][1] - fltr.shape[1]
            
            for i in fltr:
                new_fltr.append(np.pad(i, (0,pad_size), 'constant', constant_values=(0)))
        else:
            return(fltr,x)   
                
        # pad x
        new_x = []
        if (not x.shape[1] == input_model[0][1]):
            
            for x_matrix in x:
                pad_size = input_model[0][1] - x.shape[1]
                z = np.zeros(len(x_matrix[0]))

                new_x_matrix = []
                for row in x_matrix:
                    new_x_matrix.append(row)
                for i in range(0,pad_size):
                    new_x_matrix.append(z)

                new_x_matrix = np.asarray(new_x_matrix)
                new_x.append(new_x_matrix)

            new_x = np.asarray(new_x)
        else:
            new_x = x


        new_fltr = np.asarray(new_fltr)

        return(new_fltr, new_x)

    
class Transformer_autoencoder:
    
    def __init__(self, autoencoders, encoders ,batch_size,validation_split,epochs,patience,verbose=0,scaler=None,dim=[2,3,5],plot=False):
        
        self.autoencoders = autoencoders
        self.encoders = encoders
        
        self.batch_size = batch_size
        self.validation_split = validation_split
        self.epochs = epochs
        self.verbose = verbose
        self.patience = patience
        
        if (scaler != None):
            self.scaler = scaler
        
        self.plot = plot
        
        self.dim = dim
        self.selected_model = 0
        self.n_components = 0
        
        self.origina_weights = []
        
        for auto in autoencoders:
            self.origina_weights.append(auto.get_weights())
        
    
    def reset_state(self):
        for i in range(len(self.autoencoders)):
            self.autoencoders[i].set_weights(self.origina_weights[i])
        
        
    
    def fit(self,x,_):
        
        self.selected_model = self.dim.index(self.n_components)
        
        
        ##### preprocessing inpuu
        if (self.scaler != None):
            x = self.scaler.fit(x).transform(x)
            
        # callback
        es_callback = EarlyStopping(monitor='val_loss', patience=self.patience)
        
        
        model_history = self.autoencoders[self.selected_model].fit(x,x,
                                                    batch_size=self.batch_size,
                                                    validation_split=self.validation_split,
                                                    epochs=self.epochs,
                                                    verbose=self.verbose,
                                                    callbacks=[es_callback])

        print(es_callback.stopped_epoch)
        
        if (self.plot == True):
            tmp_print(model_history)
        
        
        self.encoders[self.selected_model].set_weights(self.autoencoders[self.selected_model].get_weights())
        
        return(self)
        
    def transform(self,x):
       
        if (self.scaler != None):
            x = self.scaler.transform(x)
        
        return(self.encoders[self.selected_model].predict(x))
    



class Preprocessing_scaler:
    
    def __init__(self,feature_range):
        
        self.feature_range = feature_range
        self.scaler = MinMaxScaler(copy=True, feature_range=(feature_range[0],feature_range[1]))
              
        
    def fit(self,x):
        self.scaler.fit(x)    
        return(self)
    
    
    def transform(self,x):
        return(self.scaler.transform(x))


class Transformer_GNN_embedder:

    def __init__(self, original_models,new_models,batch_size,validation_split,epochs,patience,verbose=0,dim=[2,3,5],plot=False):
        
        self.original_models = original_models
        self.new_models = new_models
        
        self.batch_size = batch_size
        self.validation_split = validation_split
        self.epochs = epochs
        self.verbose = verbose
        self.patience = patience
        
        
        self.dim = dim 
        self.selected_model = 0
        self.n_components = 0
        
        self.original_weights = []
        
        # store the original weigths (the one assigned when the net is compiled)
        
        for original in original_models:
            self.original_weights.append(original.get_weights())
        
        
        ###
        self.plot = plot

        
    def reset_state(self):
        for i in range(len(self.original_models)):
            self.original_models[i].set_weights(self.original_weights[i])

    
    def fit(self,graphs,y):
        
        # select the right model
        self.selected_model = self.dim.index(self.n_components)
        
        
        # Preprocessing
        adj, x, _ = utilities.from_nx_to_adj(graphs)
        fltr = localpooling_filter(adj)
        y_one_hot = utilities.from_np_to_one_hot(y)
        
        # callback
        es_callback = EarlyStopping(monitor='val_loss', patience=self.patience)
        
        
        ### the dataset is splitted, and the input of the model
        ### acceps max_n_nodes as impout, so if needed add a padding
        fltr, x = self.add_padding(fltr,x)

        
        history = self.original_models[self.selected_model].fit([x, fltr],y_one_hot,
                                                                batch_size=self.batch_size,
                                                                validation_split=self.validation_split,
                                                                epochs=self.epochs,
                                                                callbacks=[es_callback],
                                                                verbose=self.verbose)
        if (self.plot == True):
            tmp_print(history)

        print(es_callback.stopped_epoch)
        
        
        current_weights = self.original_models[self.selected_model].get_weights()
        self.new_models[self.selected_model].set_weights(current_weights)

        return(self)
    
    
    
    def transform(self,graphs):
        
        # preprocessing
        adj, x, _ = utilities.from_nx_to_adj(graphs)
        fltr = localpooling_filter(adj)
        fltr, x = self.add_padding(fltr,x)
            
        y_pred = self.new_models[self.selected_model].predict([x,fltr])
        
        return(y_pred)


    def add_padding(self,fltr,x):
        
        input_model = self.original_models[self.selected_model].get_input_shape_at(0)
        #### pad fltr
        new_fltr = []
        if (not fltr.shape[1] == input_model[1][1]):

            pad_size = input_model[1][1] - fltr.shape[1]
            
            for i in fltr:
                new_fltr.append(np.pad(i, (0,pad_size), 'constant', constant_values=(0)))
        else:
            return(fltr,x)   
                
        # pad x
        new_x = []
        if (not x.shape[1] == input_model[0][1]):
            
            for x_matrix in x:
                pad_size = input_model[0][1] - x.shape[1]
                z = np.zeros(len(x_matrix[0]))

                new_x_matrix = []
                for row in x_matrix:
                    new_x_matrix.append(row)
                for i in range(0,pad_size):
                    new_x_matrix.append(z)

                new_x_matrix = np.asarray(new_x_matrix)
                new_x.append(new_x_matrix)

            new_x = np.asarray(new_x)
        else:
            new_x = x


        new_fltr = np.asarray(new_fltr)

        return(new_fltr, new_x)


def tmp_print(model_history):  

    loss = model_history.history['loss']

    val_loss = model_history.history['val_loss']

    epochs = range(len(loss))

    plt.figure()
    plt.plot(epochs, loss, 'bo', label='Training loss')
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()
    plt.show()
    
    print("max loss", np.max(loss))
    print("min loss", np.min(loss))