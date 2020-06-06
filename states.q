//This file was generated from (Commercial) UPPAAL 4.0.15 rev. CB6BB307F6F681CB, November 2019

/*
Robot 0 and 1 can collaborate in removing an object
*/
E<> remover0.removeObject and remover1.removeObject

/*
A caller robot will eventually solve the problem
*/
caller0.called --> synch0.IDLE

/*
Robot 0 can not become remover without help arriving
*/
A[] caller0.called imply remover0.NotRemover

/*
A helping robot must have a lower priority than its caller
*/
A[] not (helper1.approved and helper1.myPrio > caller0.myPrio)

/*
Robot 0 can get it's help request approved
*/
E<> caller0.called

/*
A Caller can't become a helper
*/
A[] not (not caller0.NotCaller and synch0.prepareHelper)

/*
A Robot can't travel to a approved caller and become helper to other caller
*/
A[] not (helper1.travelToCaller and synch1.prepareHelper)

/*
A robot should wait no longer than 10 ticks for a response (positive or negative)
*/
A[] not (caller0.waiting and caller0.t0 > 10)

/*

*/
A[] not deadlock
