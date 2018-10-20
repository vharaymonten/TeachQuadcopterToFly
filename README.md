# Teach a Quadcopter How to Fly
<img src='others/Udacitycert-1.png'>


---

In this repository you can find my relevant Udacity DLND projects, as results and proof of me being Udacity Deep Learning Nanodegree Foundation Graduate  

---


## Teach Quadcopter How to Fly

### Introduction 
In this project, i had to teach the Agent, the quadcopter, to take off by itself and by no any human interference. The Quadcopter has four rotors which make the Quadcopter can fly in the air. In order to make it fly properly and prevent it from falling, its roters' trust power need to be adjusted to a certain value based on what state the Agent is in. Hardcoding the Quadcopter rotors' would be a doubtful solution. Because it requires a lot of time and the process of hardcoding it is undeniably difficult. However, there's an easier way to solve such quite complex problem, that's using Deep Learning model.

### Algoritm for the Task
Due to continuous state space and action space, Deep-Q Learning, which heavily relies on discrete action space as outputs is unsuited for the task. Therefore, leaving Policy Gradient, Actor Critic, Deterministic Policy Gradient as options to solve the problem would be the most suitable. However, there is a stronger Algorithms that is belived capable of solving the task more efficently, that is Deep Deterministic Policy Gradient. DDPG combines both Deterministic Policy Gradient, Actor Critic, Temporal Difference, and Fixed Target into one set of Algoritm. To "encourge" some explorations to the agent, noises called OU-Noise are added to agent's actions.

### Conclusion

While Algorithm like Deep-Q Learning only able to output discrete action space, DDPG which can outputs both continuous and discrete action space is used to solve the problem. DDPG also has been proven able to overcome problems that other strong Reinforcement Learning Algoritms can't. After many episodes of training with DDPG, the agent is able to fly by itself.  
 
---

## Udacity Projects 
<ul>
  <li><a href="https://github.com/vharaymonten/DogBreedsClassificationWithFlask"> Classify 133 Dog Breeds </a></li>
  <li><a href="https://github.com/vharaymonten/TV-Script-Generation-UdacityProject3">Generate TV script using LSTM</a></li>
  <li><a href="https://github.com/vharaymonten/FaceGenerationWithGAN">Generate Human Face with GANs</a></li>
</ul>

---
