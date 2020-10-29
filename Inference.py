<<<<<<< HEAD
"""
@author:
"""

=======
>>>>>>> 30db6dc99e1e507eee570129ed7871e577ee56ff
from absl import flags
from absl import logging
from absl import app
from FASTRAL import FASTRAL
from utils import make_dir


FLAGS = flags.FLAGS

flags.DEFINE_integer('k', None,'total number of input gene trees')
flags.DEFINE_string('nt', None,'number of trees per sample, if there are multuple samples use comma seperated values')
flags.DEFINE_string('ns', None,'number of samples, input multiple sample sizes with comma seperated values')
flags.DEFINE_boolean('rep', False, 'whether draw samples with replacement | Default: False')
flags.DEFINE_string('it', None,'path to input gene trees')
flags.DEFINE_string('os', None,'path to samples folders to write sampled trees')
flags.DEFINE_string('time', None,'path to write running times')
flags.DEFINE_string('path_ASTRID', None,'path to ASTRID')
flags.DEFINE_string('path_ASTRAL', None,'path to ASTRAL')
flags.DEFINE_string('aggregate', None,'path to write aggeregated species trees')
flags.DEFINE_integer('heuristics', 0, 'heuristics level of ASTRAL | Default: 0')
flags.DEFINE_string('o', None,'path to write ASTRAL output species tree')

def main(argv):

    make_dir(FLAGS.os)
    make_dir(FLAGS.time, writable = True)
    make_dir(FLAGS.aggregate, writable = True)
    make_dir(FLAGS.o, writable = True)

    method = ASTRALID(FLAGS)
    method.run()

if __name__ == "__main__":
    app.run(main)