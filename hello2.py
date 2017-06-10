import tensorflow as tf

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b #short cut for tf.add()

sess = tf.Session() #Intialize Session

print(sess.run(adder_node, {a:[1,3], b:[2,4]}))
print(sess.run(adder_node, {a:20.5, b:78.5}))

add_triple = adder_node * 3
print(sess.run(add_triple, {a:3.5, b:7.5}))
