# creates a local working directory in user-home
function createLocalDir ()
{
  if [ ! -f $myHomeDir/uqm-0.6.2 ]; then
    echo "creating local working directory $myHomeDir ..."
    set +e
    /usr/share/autodl/AutoDL.py $myShareDir/uqm.autodlrc
    STATUS=$?
    set -e
    # status 2 means download was ok, but the user choose not to start the game
    if [ "$STATUS" = "0" -o  "$STATUS" = "2" ]; then
      cd $myHomeDir/content/
      if [ ! -f ./version ]; then
        ln -s $myShareDir/content/version version
      fi
      cd packages/
      if [ ! -f ./addons ]; then
        ln -s $myShareDir/content/packages/addons addons
      fi
      # Signal succesful datafiles installation
      cd ../..
      touch uqm-0.6.2
    fi

    if [ "$STATUS" != "0" ]; then
      exit $STATUS
    fi
  fi
}
