# I am a starter for github

import numpy as py
import tensorflow as tf
import matplotlib as plt

node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0) # also tf.float32 implicitly
print(node1, node2)

sess = tf.Session()

node3 = tf.add(node1, node2)

wirter = tf.summary.FileWriter("./tensorgraph_log")
wirter.add_graph(sess.graph)

print ("node 3", node3)
print ("run node 3", sess.run(node3))
