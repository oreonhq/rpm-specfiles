package=redhat-lsb
branch=main
commit=HEAD

if [ ! -d redhat-lsb.pagure ]; then
    git clone ssh://git@pagure.io/redhat-lsb.git redhat-lsb.pagure
fi

pushd redhat-lsb.pagure
tag=$(git rev-list HEAD -n 1 | cut -c 1-8)
date=$(git log -1 --format=%cd --date=short | tr -d \-)
git archive --prefix="${package}-${date}git${tag}/" --format=tar ${branch} | gzip > ../${package}-${date}git${tag}.tar.gz
popd

echo \# globals for ${package}-${date}git${tag}.tar.gz
echo %global gitdate ${date}
echo %global gitversion ${tag}

sed -i "s|^# globals for .*|# globals for ${package}-${date}git${tag}.tar.gz|" redhat-lsb.spec
sed -i "s|^%global gitdate .*|%global gitdate ${date}|" redhat-lsb.spec
sed -i "s|^%global gitversion .*|%global gitversion ${tag}|" redhat-lsb.spec

echo fedpkg new-sources $(spectool -l --sources redhat-lsb.spec | sed 's/.*: //;s/.*\///')
echo \MSG="\"Update README.md with actual status\""
echo rpmdev-bumpspec  -c \"\$MSG\" $(basename $(pwd)).spec
