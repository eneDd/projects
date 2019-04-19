 function new_states =  social_step(pre_state, graph, willingness, k)

 willingness_parameter = zeros(length(pre_state),1); % Wilingness vector init.
 
 for agent = 1:length(pre_state)     
 if (pre_state(agent) > 0)          % Distrubutes the parameters to agents
    willingness_parameter(agent) = willingness(pre_state(agent));
 end
 end
 
 prob = (graph*willingness_parameter)*k;  % Calculates the whole probablities of agents 
 prob1 = (1-prob);

 for agent = 1:length(pre_state)    % Conditions for changing States 

 if (pre_state(agent) > 0)
 if (pre_state(agent) == length(willingness))
     new_states(agent) = 3;
 else
     new_states(agent) = pre_state(agent) + 1;
 end
 else
 if (pre_state(agent) == 0)
 if (rand<prob(agent))
     new_states(agent) = 1;
 else
     new_states(agent) = 0;
     
 if (0 < pre_state(agent) < 4 )
 if (rand<prob1(agent))
     new_states(agent) = 0;
 end
 end
 end
 end
 end
 end
 
 
    