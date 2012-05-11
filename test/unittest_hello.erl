%% Author: Opo
%% Created: 11 maj 2012
%% Description: TODO: Add description to unittest_hello
-module(unittest_hello).
-include_lib("eunit/include/eunit.hrl").




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%			   EUnit Test Cases                                  %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% All functions with names ending wiht _test() or _test_() will be
%% called automatically by list:test()


hello1_test() ->
	?assertEqual(1+1,2).	

hello2_test() ->
	?assertEqual(1+1,3).

hello3_test() ->
	?assertNotEqual(1+1,3).