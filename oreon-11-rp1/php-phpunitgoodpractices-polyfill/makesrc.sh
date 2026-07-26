#!/bin/bash

NAME=$(basename $PWD)
OWNER=$(sed   -n '/^%global gh_owner/{s/.* //;p}'   $NAME.spec)
PROJECT=$(sed -n '/^%global gh_project/{s/.* //;p}' $NAME.spec)
VERSION=$(sed -n '/^Version:/{s/.* //;p}'           $NAME.spec)
COMMIT=$(sed  -n '/^%global gh_commit/{s/.* //;p}'  $NAME.spec)
SHORT=${COMMIT:0:7}

echo -e "\nCreate git snapshot\nName=$NAME, Owner=$OWNER, Project=$PROJECT, Version=$VERSION\n"
if [ -f $NAME-$VERSION-$SHORT.tgz ]; then
	echo "$PROJECT Skipped"
else
	echo "Cloning..."
	git clone https://github.com/$OWNER/$PROJECT.git $PROJECT-$COMMIT

	echo "Getting commit..."
	pushd $PROJECT-$COMMIT
		git checkout $COMMIT || exit 1
		cp composer.json ../composer-polyfill.json
	popd

	echo "Archiving..."
	tar czf $NAME-$VERSION-$SHORT.tgz --exclude .git $PROJECT-$COMMIT

	echo "Cleaning..."
	rm -rf $PROJECT-$COMMIT
fi

PROJECT=Traits
VERSION=$(sed -n '/^%global tr_version/{s/.* //;p}' $NAME.spec)
COMMIT=$(sed  -n '/^%global tr_commit/{s/.* //;p}'  $NAME.spec)
SHORT=${COMMIT:0:7}
NAME=php-phpunitgoodpractices-traits

if [ -f $NAME-$VERSION-$SHORT.tgz ]; then
	echo "$PROJECT Skipped"
else
	echo -e "\nCreate git snapshot\nName=$NAME, Owner=$OWNER, Project=$PROJECT, Version=$VERSION\n"

	echo "Cloning..."
	git clone https://github.com/$OWNER/$PROJECT.git $PROJECT-$COMMIT

	echo "Getting commit..."
	pushd $PROJECT-$COMMIT
		git checkout $COMMIT || exit 1
		cp composer.json ../composer-traits.json
	popd

	echo "Archiving..."
	tar czf $NAME-$VERSION-$SHORT.tgz --exclude .git $PROJECT-$COMMIT

	echo "Cleaning..."
	rm -rf $PROJECT-$COMMIT
fi

NAME=$(basename $PWD)
OWNER=$(sed   -n '/^%global lg_owner/{s/.* //;p}'   $NAME.spec)
PROJECT=$(sed -n '/^%global lg_project/{s/.* //;p}' $NAME.spec)
VERSION=$(sed -n '/^%global lg_version/{s/.* //;p}' $NAME.spec)
COMMIT=$(sed  -n '/^%global lg_commit/{s/.* //;p}'  $NAME.spec)
SHORT=${COMMIT:0:7}
NAME=php-$OWNER-$PROJECT

if [ -f $NAME-$VERSION-$SHORT.tgz ]; then
	echo "$PROJECT Skipped"
else
	echo -e "\nCreate git snapshot\nName=$NAME, Owner=$OWNER, Project=$PROJECT, Version=$VERSION\n"

	echo "Cloning..."
	git clone https://github.com/$OWNER/$PROJECT.git $PROJECT-$COMMIT

	echo "Getting commit..."
	pushd $PROJECT-$COMMIT
		git checkout $COMMIT || exit 1
		cp composer.json ../composer-legacy.json
	popd

	echo "Archiving..."
	tar czf $NAME-$VERSION-$SHORT.tgz --exclude .git $PROJECT-$COMMIT

	echo "Cleaning..."
	rm -rf $PROJECT-$COMMIT
fi

echo "Done."
