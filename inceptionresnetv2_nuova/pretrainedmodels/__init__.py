from .version import __version__

from . import models
#from . import datasets

from .models.utils import pretrained_settings
from .models.utils import model_names

# to support pretrainedmodels.__dict__['nasnetalarge']
# but depreciated

from .models.inceptionresnetv2 import inceptionresnetv2
