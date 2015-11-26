import weka.core.jvm as jvm
from weka.core.converters import Loader


jvm.start()

loader = Loader(classname="weka.core.converters.ArffLoader")
data = loader.load_file("mlabel.txt")
data.class_is_last()

print(data)

