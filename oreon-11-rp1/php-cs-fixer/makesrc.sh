#!/bin/bash

NAME=$(sed    -n '/^Name:/{s/.* //;p}'                  *.spec)
DATE=$(sed    -n '/^%global gh_date/{s/.* //;p}'    $NAME.spec)
OWNER=$(sed   -n '/^%global gh_owner/{s/.* //;p}'   $NAME.spec)
PROJECT=$(sed -n '/^%global gh_project/{s/.* //;p}' $NAME.spec)
VERSION=$(sed -n '/^Version:/{s/.* //;p}'           $NAME.spec)
COMMIT=$(sed  -n '/^%global gh_commit/{s/.* //;p}'  $NAME.spec)
SHORT=${COMMIT:0:7}

DATE=$(date -d "$DATE -4 days" +%Y-%m-%d)

if [ -f $NAME-$VERSION-$SHORT.tgz ]; then
	echo "Skip $NAME-$VERSION-$SHORT.tgz"
else
	echo -e "\nCreate git snapshot\nName=$NAME, Owner=$OWNER, Project=$PROJECT, Version=$VERSION, Commit=$COMMIT, Date=$DATE\n"

	echo "Cloning..."
	git clone --shallow-since=$DATE  https://github.com/$OWNER/$PROJECT.git $PROJECT-$COMMIT || exit 1

	echo "Getting commit..."
	pushd $PROJECT-$COMMIT
		git checkout $COMMIT || exit1
		cp composer.json ../

		composer config platform.php 8.1.99
		# see https://github.com/PHP-CS-Fixer/PHP-CS-Fixer/blob/master/dev-tools/build.sh
		# some dev dep cannot be satisfied but are not needed
		composer remove --dev infection/infection --no-update
		composer install --no-interaction --no-progress --no-dev --no-scripts --optimize-autoloader
		cp vendor/composer/installed.json ../
	popd

	echo "Archiving..."
	tar czf $NAME-$VERSION-$SHORT.tgz --exclude .git $PROJECT-$COMMIT

	echo "Cleaning..."
	rm -rf $PROJECT-$COMMIT
fi

