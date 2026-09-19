NAME=vdr-streamdev
REPO=git://projects.vdr-developer.org/vdr-plugin-streamdev.git
TMPDIR=`mktemp -d`

pushd $TMPDIR
	git clone $REPO $NAME
	pushd $NAME
		if [ -z $1 ]; then
			GITVER=`git rev-parse HEAD`
		else
			GITVER=$1
		fi
		git archive --format=tar --prefix=${NAME}-${GITVER:0:8}/ ${GITVER} | xz > ${NAME}-${GITVER:0:8}.tar.xz
	popd
popd
mv $TMPDIR/$NAME/${NAME}-${GITVER:0:8}.tar.xz .
rm -rf $TMPDIR
