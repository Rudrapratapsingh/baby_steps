import tensorflow as tf
hello = tf.constants("Hello Tensor Flow")
sess = tf.Session()
print(sess.run(hello))

