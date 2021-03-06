import gym
env = gym.make('CartPole-v0')

print(env.action_space)
print(env.observation_space)

print(env.observation_space.high)
print(env.observation_space.low)

from gym import spaces
space = spaces.Discrete(8)
x = space.sample()
assert space.contains(x)
assert space.n == 8