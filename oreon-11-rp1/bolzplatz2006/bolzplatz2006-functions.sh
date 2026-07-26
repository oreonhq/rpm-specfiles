# creates a local working directory in user-home
function createLocalDir ()
{
  if [ ! -f $myHomeDir/bolzplatz2006-1.0.3 ]; then
    echo "creating local working directory $myHomeDir ..."
    set +e
    /usr/share/autodl/AutoDL.py $myShareDir/bolzplatz2006.autodlrc
    STATUS=$?
    set -e
    # status 2 means download was ok, but the user choose not to start the game
    if [ "$STATUS" = "0" -o  "$STATUS" = "2" ]; then
      cd $myHomeDir
      tar xfz bolzplatz2006-1.0.3-linux.tar.gz
      mv bolzplatz2006/data .
      rm -fr bolzplatz2006 bolzplatz2006-1.0.3-linux.tar.gz
      # Fix for some files being opened by the wrong name sometimes
      cd data/meshes
      ln -s terrain1.png terrain.png
      ln -s envi4.png envi04.png
      ln -s soccerfield4.png soccerfield04.png
      cd ../..
      # The upstream default input settings only work with German keyboards
      cp $myShareDir/input.xml data/config/input.xml
      cp $myShareDir/input.xml data/config/input-default.xml
      # Signal succesfull datafiles installation
      touch bolzplatz2006-1.0.3
    fi

    if [ "$STATUS" != "0" ]; then
      exit $STATUS
    fi
  fi
}
