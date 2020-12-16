# from mycode import cuberoot_approx
# reference: mit 6.0001
# using divide and conquer to solve for cube root
cube = 50
epsilon = 0.01
num_guesses = 0
low = 0
high = abs(cube) if abs(cube) > 1 else 1
guess = (high + low) / 2.0

# smaller the epsilon, more accurate the result will be
while abs(guess ** 3 - abs(cube)) >= epsilon:
    if guess ** 3 < abs(cube):
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0
    num_guesses += 1

# num_guesses, guess = cuberoot_approx(cube)
print("Number of guesses:", num_guesses)
print(
    format(guess if cube > 0 else -guess, ".3f"), "is close to the cube root of", cube
)