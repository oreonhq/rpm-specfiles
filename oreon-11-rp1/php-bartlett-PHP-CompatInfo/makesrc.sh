#!/bin/bash

NAME=$(basename $PWD)
DATE=$(sed    -n '/^%global gh_date/{s/.* //;p}'    $NAME.spec)
OWNER=$(sed   -n '/^%global gh_owner/{s/.* //;p}'   $NAME.spec)
PROJECT=$(sed -n '/^%global gh_project/{s/.* //;p}' $NAME.spec)
VERSION=$(sed -n '/^%global upstream_version/{s/.* //;p}' $NAME.spec)
COMMIT=$(sed  -n '/^%global gh_commit/{s/.* //;p}'  $NAME.spec)
SHORT=${COMMIT:0:7}

DATE=$(date -d "$DATE -4 days" +%Y-%m-%d)

echo -e "\nCreate git snapshot\nName=$NAME, Owner=$OWNER, Project=$PROJECT, Version=$VERSION, Commit=$COMMIT\n"

echo "Cloning..."
rm -rf $HOME/.cache/bartlett
git clone --shallow-since=$DATE https://github.com/$OWNER/$PROJECT.git $PROJECT-$COMMIT

echo "Getting commit..."
	pushd $PROJECT-$COMMIT
		git checkout $COMMIT || exit 1

		cp composer.json ../
		module load php81
		composer config platform.php 8.1.99
		composer install --no-interaction --no-progress --no-dev --optimize-autoloader
		cp vendor/composer/installed.json ../

		export DATABASE_URL=sqlite:///$PWD/data/compatinfo-db.sqlite
		mkdir data
		bin/phpcompatinfo db:create
		bin/phpcompatinfo db:init
		bin/phpcompatinfo diag
	popd

echo "Archiving..."
tar czf $NAME-$VERSION-$SHORT.tgz --exclude-vcs $PROJECT-$COMMIT

echo "Cleaning..."
rm -rf $PROJECT-$COMMIT
rm -rf $HOME/.cache/bartlett

echo "Done."

