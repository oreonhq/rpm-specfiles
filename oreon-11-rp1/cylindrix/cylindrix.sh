#!/bin/bash

#if no .cylindrix in home
if [ ! -d ~/.cylindrix ]; then

  #make .cylindrix in home
  mkdir ~/.cylindrix || :
  #link to data
  ln -s /usr/share/cylindrix/3d_data ~/.cylindrix/3d_data || :
  ln -s /usr/share/cylindrix/anything.mod ~/.cylindrix/anything.mod  || :
  ln -s /usr/share/cylindrix/cylindrx.fli ~/.cylindrix/cylindrx.fli || :
  ln -s /usr/share/cylindrix/pcx_data ~/.cylindrix/pcx_data || :
  ln -s /usr/share/cylindrix/wav_data ~/.cylindrix/wav_data || :

  #copy mutable data
  cp -p /usr/share/cylindrix/people.dat ~/.cylindrix/ || :
  cp -pr /usr/share/cylindrix/stats ~/.cylindrix/ || :
  cp -pr /usr/share/cylindrix/gamedata ~/.cylindrix/ || :
fi

if [ ! -a ~/.cylindrix/bz452190 ]; then
  #refresh gamedata/level10.dat
  cp -pf /usr/share/cylindrix/gamedata/level10.dat ~/.cylindrix/gamedata/level10.dat || :
  echo "Correction for broken data file" > ~/.cylindrix/bz452190 || :
fi

cd ~/.cylindrix
exec cylindrix-bin "$@"
