# dnf install python3-cvdupdate
# python -m cvdupdate.cvdupdate --help
cvd config set --dbdir my_dbs
cvdupdate list
cvdupdate update
pushd my_dbs
main_ver=$(file main.cvd | sed -e 's/.*version /main-/;s/,.*/.cvd/')
daily_ver=$(file daily.cvd | sed -e 's/.*version /daily-/;s/,.*/.cvd/')
bytecode_ver=$(file bytecode.cvd | sed -e 's/.*version /bytecode-/;s/,.*/.cvd/')
popd

pushd my_dbs
cp -f main.cvd ../$main_ver
cp -f daily.cvd ../$daily_ver
cp -f bytecode.cvd ../$bytecode_ver
popd

sed -i "s|^Source10: .*|Source10:   $main_ver|" clamav.spec
sed -i "s|^Source11: .*|Source11:   $daily_ver|" clamav.spec
sed -i "s|^Source12: .*|Source12:   $bytecode_ver|" clamav.spec
