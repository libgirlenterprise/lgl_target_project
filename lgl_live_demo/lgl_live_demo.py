
def model(x):
    return 1 / (1 + numpy.exp(-x))

def main():
    
# This is the test set, it's a straight line with some Gaussian noise
    xmin, xmax = -10, 10
    n_samples = 100
    numpy.random.seed(0)
    X = numpy.random.normal(size = n_samples)
    y = (X > 0).astype(numpy.float)
    X[X > 0] *= 4
    X += .3 * numpy.random.normal(size = n_samples)
    X = X[:, numpy.newaxis]
    
    # run the classifier
    clf = sklearn.linear_model.LogisticRegression(C=1e5)
    clf.fit(X, y)

    # and plot the result
    matplotlib.pyplot.figure(1, figsize = (4, 3))
    matplotlib.pyplot.clf()
    matplotlib.pyplot.scatter(X.ravel(), y, color='black', zorder=20)
    X_test = numpy.linspace(-10, 10, 300)

    loss = model(X_test * clf.coef_ + clf.intercept_).ravel()
    matplotlib.pyplot.plot(X_test, loss, color='blue', linewidth=3)
    ols = sklearn.linear_model.LinearRegression()
    ols.fit(X, y)
    matplotlib.pyplot.plot(X_test, ols.coef_ * X_test + ols.intercept_, linewidth=1)
    matplotlib.pyplot.axhline(.5, color='.5')
    matplotlib.pyplot.ylabel('y')
    matplotlib.pyplot.xlabel('X')
    matplotlib.pyplot.xticks(range(-10, 10))
    matplotlib.pyplot.yticks([0, 0.5, 1])
    matplotlib.pyplot.ylim(-.25, 1.25)
    matplotlib.pyplot.xlim(-4, 10)
    matplotlib.pyplot.legend(('Logistic Regression Model', 'Linear Regression Model'),
                             loc="lower right", fontsize='small')
    matplotlib.pyplot.show()


