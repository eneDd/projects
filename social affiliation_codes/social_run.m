function social_run = social_run(states)

social_run = zeros(1,2);
 for agent = 1:length(states)
 switch states(agent)
 case 0
 social_run(1) = social_run(1)+1; % Counts the Non Affiliation
 otherwise
 social_run(2) = social_run(2)+1; % Counts the afilliation
 end;
 end;