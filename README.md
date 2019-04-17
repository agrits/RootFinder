# RootFinder
Implementation of 3 root-finding algorithms in Python for university project

## Using in command line

If you want to use the app with your command line, do not hesitate and simply run it with: `python ui.py`

The program will guide you through the process in Polish.

## Using in your browser

The app also allows you to make simple GET calls to a server running the app.
If you want to run a server of your own, you have to type: `python api.py`. The server will run on `localhost:5000`.

The call structure is different for the methods:

Newton's method uses: `/newtons/<function>/<starting point>/<max iterations>/<epsilon>`.
So, if you want to calculate one root of x-3, starting at 1, allowing maximum 1000 iterations and the result should be 1e-7 close to the real root, you type in your browser (or use the address in curl): `localhost:5000/newtons/x-3/1/1000/1e-7`.

Bisection and secant method use: `/bisection|secant/<function>/<starting point a>/<starting point b>/<number of iterations>`.
So, if you want to calculate one root of x-3, starting at x's -1 and 4, allowing 1000 iterations, you type in your browser (or use the address in curl): `localhost:5000/bisection|secant/x-3/-1/4/1000`.
