from __future__ import print_function
from wrapper import newAutoDiff, newAutoDiffLike, squareVector, squareMatrix
import numpy as np

x = np.array([1,2,3.])
y = squareVector(x)
assert np.allclose(y.T, np.power(x, 2))

x = newAutoDiff(np.array([1.0, 3.0]), np.array([2.0, 5.0]))
print(x.value())
print(x)
assert (x.value() == np.array([[1.0, 3.0]]).T).all()
assert (x.derivatives() == np.array([[2.0, 5.0]]).T).all()

y = squareVector(x)
print(y.value())
assert (y.value() == np.power(x.value(), 2)).all()
assert (y.derivatives() == x.derivatives() * 2 * x.value()).all()

z = x + y
print(z.value())
assert (z.value() == x.value() + y.value()).all()
assert (z.derivatives() == x.derivatives() + y.derivatives()).all()

w = (((x + 1) - 5) * 2) / 1.5
print(w.value())
assert (w.value() == (x.value() + 1 - 5) * 2 / 1.5).all()
assert np.allclose(w.derivatives(), x.derivatives() * 2 / 1.5)

q = x.arrayMultiply(x)
print(q.value())
assert np.allclose(q.value(), y.value())
assert np.allclose(q.derivatives(), y.derivatives())

x = newAutoDiff(np.array([[1., 2.], [3., 4.]]), np.array([[3., 3., 3., 3.]]).T)
print(x.value())
y = squareMatrix(x)
print(y.value())
assert np.allclose(y.value(), np.power(x.value(), 2))
assert np.allclose(y.derivatives(), 2 * x.value().reshape((-1,1), order='F') * x.derivatives())

y = newAutoDiffLike(x, [1,3,2,4])
print(y.value())
assert np.allclose(y.value(), x.value())
w = x + y
assert np.allclose(w.value(), x.value() + y.value())
assert np.allclose(w.derivatives(), x.derivatives())

big = newAutoDiff(np.random.rand(75,1))
assert np.allclose(big.derivatives(), np.eye(75, 75))

assert np.allclose((big + 2.0).value(), big.value() + 2.0)
assert np.allclose((big + 2.0).derivatives(), big.derivatives())
assert np.allclose((big * 2.0).derivatives(), 2.0 * big.derivatives())