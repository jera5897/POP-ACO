-module(hello).
-export([hello/1]).

hello(Message) ->
    Port = open_port({spawn, "python -u antworld.py"}, [{packet, 1}, binary, use_stdio]),
    port_command(Port, term_to_binary(Message)),
    receive
	{Port, {data, Data}} ->
	    %port_close(Port),
	    binary_to_term(Data)
    after
	60000 ->
	    {error, timeout}
    end.


%% Todo: fixa receive så att den loopar
