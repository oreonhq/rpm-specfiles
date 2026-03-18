pushd /tmp/micropipenv/tests/data/install/$1/
python3 -m venv venv
source venv/bin/activate
micropipenv install
pip3 list
deactivate
rm -rf venv
popd
