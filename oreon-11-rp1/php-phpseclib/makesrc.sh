#!/bin/bash

NAME=$(basename $PWD)
OWNER=$(sed   -n '/^%global github_owner/{s/.* //;p}'   $NAME.spec)
PROJECT=$(sed -n '/^%global github_name/{s/.* //;p}' $NAME.spec)
VERSION=$(sed -n '/^Version:/{s/.* //;p}'           $NAME.spec)
COMMIT=$(sed  -n '/^%global github_commit/{s/.* //;p}'  $NAME.spec)
SHORT=${COMMIT:0:7}

echo -e "\nCreate git snapshot\nName=$NAME, Owner=$OWNER, Project=$PROJECT, Version=$VERSION\n"

echo "Cloning..."
rm -rf $PROJECT-$COMMIT
git clone --revision "${COMMIT}" --depth 1 https://github.com/$OWNER/$PROJECT.git $PROJECT-$COMMIT

echo "Saving a copy of composer.json..."
pushd $PROJECT-$COMMIT
cp composer.json ../composer-$VERSION.json
popd

echo "Archiving..."
tar czf $NAME-$VERSION-$SHORT.tgz --exclude .git $PROJECT-$COMMIT

echo "Cleaning..."
rm -rf $PROJECT-$COMMIT

echo "Done."
