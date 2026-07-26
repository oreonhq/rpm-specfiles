%global source0_hash 2098940c2452ac8c88ed2fcaddec91753d287c3cd34578f4422e422072832115

%global		use_release	0
%global		use_git		0
%global		use_gitbare	1

%if 0%{?use_gitbare} < 1
# force
%global		use_release	1
%endif

%global		git_version	%{nil}
%global		git_ver_rpm	%{nil}
%global		git_builddir	%{nil}

%if 0%{?use_gitbare}
%global		gittardate		20250327
%global		gittartime		1528
%define		use_gitcommit_as_rel		0

%global		gitbaredate	20250326
%global		git_rev		69715abaa2e9089c69c96d61ad69f8e431c52fb8
%global		git_short		%(echo %{git_rev} | cut -c-8)
%global		git_version	%{gitbaredate}git%{git_short}
%endif

%if 0%{?use_gitcommit_as_rel}
%global		git_ver_rpm	^%{git_version}
%global		git_builddir	-%{git_version}
%endif

%global		main_version	0.3.3

Name:			lxrandr
Version:		%{main_version}%{git_ver_rpm}
Release:		3%{?dist}
Summary:		Simple monitor configuration tool

# SPDX confirmed
License:		GPL-2.0-or-later
URL:			http://lxde.org/
%if 0%{?use_gitbare}
Source0:		%{name}-%{gittardate}T%{gittartime}.tar.gz
%endif
%if 0%{?use_release}
Source0:		http://downloads.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.xz
%endif
Source1:		create-%{name}-git-bare-tarball.sh

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	/usr/bin/xsltproc
BuildRequires:	docbook-utils
BuildRequires:	docbook-style-xsl

BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	/usr/bin/git

Requires:		xrandr

%description
LXRandR is a simple monitor configuration tool utilizing X RandR extension. 
It's a GUI frontend of the command line program xrandr and manages screen 
resolution and external monitors. When you run LXRandR with an external 
monitor or projector connected, its GUI will change and show you some options 
to quickly configure the external device.

LXRandR is the standard screen manager of LXDE, the Lightweight X11 Desktop 
Environment, but can be used in other desktop environments as well.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?use_release}
%setup -q -n %{name}-%{main_version}%{git_builddir}

git init
%endif

%if 0%{?use_gitbare}
%setup -q -c -T -n %{name}-%{main_version}%{git_builddir} -a 0
git clone ./%{name}.git/
cd %{name}

git checkout -b %{main_version}-fedora %{git_rev}

# Restore timestamps
set +x
echo "Restore timestamps"
git ls-tree -r --name-only HEAD | while read f
do
	unixtime=$(git log -n 1 --pretty='%ct' -- $f)
	touch -d "@${unixtime}" $f
done
set -x

cp -a [A-Z]* ..
%endif

git config user.name "lxrandr Fedora maintainer"
git config user.email "lxrandr-maintainers@fedoraproject.org"

%if 0%{?use_release}
git add .
git commit -m "base" -q
%endif

sh autogen.sh

%build
%if 0%{?use_gitbare}
cd %{name}
%endif

%configure \
	--enable-gtk3 \
	--enable-man \
	--disable-silent-rules \
	%{nil}
%make_build

%install
%if 0%{?use_gitbare}
cd %{name}
%endif

%make_install
desktop-file-install \
	--delete-original \
	--add-category="HardwareSettings;GTK;" \
	--dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
	${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop
%if 0%{?use_gitbare}
cd ..
%endif
%find_lang %{name}

%files -f %{name}.lang
%doc	AUTHORS
%license	COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog
