import numpy as np
import math

class ModelAnalysis:
    def __init__(self, observed_data_image, generated_data_image):
        '''
            Defines each model output

            Args:
                observed_data_image ([w, h, 1] shape tensor)
                generated_data_image ([w, h, 1] shape tensor)
        '''
        self.observed_data_image = observed_data_image
        self.generated_data_image = generated_data_image

    def MSE(self):
        '''
            Calculates the MSE of 2 [w, h, 1] tensors

            Returns:
                [w, h, 1] tensor of point by point MSE
        '''
        return np.square(self.observed_data_image - self.generated_data_image)
    
    def kling_gupta_efficiency(self):
        '''
            Calculates KGE of 2 [w, h, 1] tensors

            Formula = 1 - sqrt( 
                                  (pearson_correlation(generated, observed) - 1)^2
                                + (mean(generated) / mean(observed) - 1)^2
                                + (((std(generated) / mean(generated)) / (std(observed) / mean(observed)) - 1)^2
                            )

            Returns:
                kge: scalar value representing the kling-gupta-efficiency
        '''
        observed_mean = np.mean(self.observed_data_image)
        observed_std = np.std(self.observed_data_image)

        generated_mean = np.mean(self.generated_data_image)
        generated_std = np.std(self.generated_data_image)

        pearson_coefficeint = np.corrcoef(self.observed_data_image.flatten(), self.generated_data_image.flatten())[0, 1]

        kle = 1 - math.sqrt(
              (pearson_coefficeint - 1)**2
            + ((generated_mean / observed_mean) - 1)**2
            + ((generated_std / generated_mean) / (observed_std / observed_mean) - 1)**2
        )
        
        return kle

    
