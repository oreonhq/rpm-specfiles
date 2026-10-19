%global source0_hash 72deda78095baa3c8d2cbc59b8e0e4a165c80ee2abfe43acdea4863b4f3ad596
%global		gitcommit		483f4b3f2d9a125606d47597ae7eff3b38e5bf9d
%global		gitdate		20211016
%global		shortcommit	%(c=%{gitcommit}; echo ${c:0:7})
%global		tarballdate	20211017
%global		tarballtime	1503
%global		base_summary 	User-friendly, customizable image viewer for comic books
%global		base_description \
MComix3 is a user-friendly, customizable image viewer. \
It has been forked from the original MComix project and ported to python3.
Name:			mcomix3
Version:		0
Release:        1%{?dist}
Summary:        User-friendly, customizable image viewer for comic books
License:		GPL-2.0-or-later
URL:			https://github.com/multiSnow/mcomix3
Source0:        %{name}-%{tarballdate}T%{tarballtime}.tar.bz2
Source1:		create-mcomix3-git-bare-tarball.sh
Source2:		mcomix3starter.sh.in
Patch2:		0002-Change-domain-name-for-gettext.patch
Patch3:		0003-Search-gettext-files-in-system-wide-directory.patch
Patch4:		0004-Workaround-on-zip-archiver-for-contents-info.patch
Patch5:		0005-Rescue-when-creating-thumbnail-fails-in-load_pixbuf_.patch
Patch6:		0006-sqlite3.py-support-python-3.14.patch
Patch7:		0007-Workaround-to-restore-space-pageup-button-behavior-i.patch
BuildArch:		noarch
Requires:		%{name}-base = %{version}-%{release}
Requires:		%{name}-thumbnailer = %{version}-%{release}
Obsoletes:		mcomix < 1.2.2
Obsoletes:		comix < 4.0.5
Provides:		mcomix = 1.2.2
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-install
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  python3-devel
# /oreon:deps
%description
%base_description

%package	base
Summary:	%base_summary
Requires:		gtk3
Requires:		python3-gobject
Requires:		python3-pillow
%description	base
%base_description
This package contains base executable %{name} script.

%package	thumbnailer
Summary:	Thumbnailer for %{name}
Requires:	%{name}-base = %{version}-%{release}
%description	thumbnailer
This package contains thumbnailer for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T -a 0

# Setup source git repository
git clone ./%{name}.git
cd %{name}

git config user.name "%{name} Fedora maintainer"
git config user.email "%{name}-owner@fedoraproject.org"
git checkout -b %{version}-%{release}-fedora %{gitcommit}

# Apply patches
cat %{PATCH2} | git am
cat %{PATCH3} | git am
cat %{PATCH4} | git am
cat %{PATCH5} | git am
cat %{PATCH6} | git am
cat %{PATCH7} | git am

%build

pushd %{name}
rm -rf localroot
mkdir localroot
python3 installer.py --srcdir=mcomix --target=$(pwd)/localroot/
pushd mime
cat mcomix.appdata.xml | \
	sed -e 's|omix|omix3|' | sed -e 's|/mcomix3/|/mcomix/|' \
	> %{name}.appdata.xml
cat mcomix.desktop | sed -e 's|omix|omix3|' > %{name}.desktop
popd
pushd man
cat mcomix.1 | sed -e 's|omix|omix3|' > %{name}.1
popd
popd
cat %SOURCE2 | sed -e 's|@python3_sitelib@|%python3_sitelib|g' > mcomix3starter.sh
cat mcomix3starter.sh | sed -e 's|mcomixstarter|comicthumb|' > comicthumbstarter.sh
%install
BUILDTOPDIR=$(pwd)
pushd %{name}
cp -p [A-Z]* ..
popd # from %%name
SITETOPDIR=%{python3_sitelib}/%{name}
DSTTOPDIR=%{buildroot}${SITETOPDIR}
mkdir -p ${DSTTOPDIR}
mkdir -p ${DSTTOPDIR}/mcomix3
mkdir -p %{buildroot}%{_datadir}/locale
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/
pushd %{name}
rm -rf localroot.2
cp -a localroot localroot.2
pushd localroot.2/mcomix
install -cpm 0755 ${BUILDTOPDIR}/mcomix3starter.sh ${DSTTOPDIR}
install -cpm 0755 ${BUILDTOPDIR}/comicthumbstarter.sh ${DSTTOPDIR}
find mcomix/messages/* -type f | while read f
do
	dir=$(dirname $f)
	mv $f $dir/%{name}.mo
done
mv mcomix/messages/* %{buildroot}%{_datadir}/locale/
for dir in mcomix/images/*x*/
do
	basedir=$(basename $dir)
	mkdir -p %{buildroot}%{_datadir}/icons/hicolor/$basedir/apps
	cp -p $dir/*png %{buildroot}%{_datadir}/icons/hicolor/$basedir/apps/%{name}.png
done
mv comicthumb.py ${DSTTOPDIR}/
mv mcomixstarter.py ${DSTTOPDIR}/
mv mcomix/ ${DSTTOPDIR}/mcomix3/
popd # from localroot.2/mcomix
rmdir localroot.2/mcomix
rmdir localroot.2
popd # from %%name
mkdir %{buildroot}/%{_bindir}
ln -sf ../../${SITETOPDIR}/mcomix3starter.sh %{buildroot}%{_bindir}/mcomix3
ln -sf ../../${SITETOPDIR}/comicthumbstarter.sh %{buildroot}%{_bindir}/comicthumb
pushd %{name}
pushd mime
install -D -cpm 0644 comicthumb.thumbnailer %{buildroot}%{_datadir}/thumbnailers/comicthumb.thumbnailer
install -D -cpm 0644 %{name}.appdata.xml  %{buildroot}%{_metainfodir}/%{name}.appdata.xml
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
	--remove-category Application \
	--dir %{buildroot}%{_datadir}/applications/ \
	./%{name}.desktop
popd # from mime
pushd man
mkdir -p %{buildroot}%{_mandir}/man1
install -cpm 0644 \
	comicthumb.1 \
	%{name}.1 \
	%{buildroot}%{_mandir}/man1/
popd # from man
popd # from %%name
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n mcomix3-base -f %{oreon_filedir}/mcomix3-base.list
%files -n mcomix3-thumbnailer -f %{oreon_filedir}/mcomix3-thumbnailer.list

%changelog

%autochangelog
