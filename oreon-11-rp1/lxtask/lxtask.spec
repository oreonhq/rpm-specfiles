%global source0_hash a97c4e5f48e078cf6e93ce86061f31b6ff84bafddeef4eb8d993bdb74606a547

# Review: https://bugzilla.redhat.com/show_bug.cgi?id=445140

%global		use_release	0
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
%global		gittartime		1511
%define		use_gitcommit_as_rel		0

%global		gitbaredate	20250325
%global		git_rev		33d3f23801089589e3e866fd43c4c96fd0b9d325
%global		git_short		%(echo %{git_rev} | cut -c-8)
%global		git_version	%{gitbaredate}git%{git_short}
%endif

%if 0%{?use_gitcommit_as_rel}
%global		git_ver_rpm	^%{git_version}
%global		git_builddir	-%{git_version}
%endif

%global		main_version	0.1.12

Name:			lxtask
Version:		%{main_version}%{git_ver_rpm}
Release:		3%{?dist}
Summary:		Lightweight and desktop independent task manager

# SPDX confirmed
License:		GPL-2.0-or-later
URL:			http://lxde.sourceforge.net/
%if 0%{?use_gitbare}
Source0:		%{name}-%{gittardate}T%{gittartime}.tar.gz
%endif
%if 0%{?use_release}
Source0:		https://github.com/lxde/%{name}/archive/%{main_version}/%{name}-%{version}.tar.gz
%endif
Source100:		create-lxtask-git-bare-tarball.sh

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	git
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	automake
BuildRequires:	libtool

%description
LXTask is a lightweight task manager derived from xfce4 task manager with all
xfce4 dependencies removed, some bugs fixed, and some improvement of UI. 
Although being part of LXDE, the Lightweight X11 Desktop Environment, it's 
totally desktop independent and only requires pure gtk+.

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

git config user.name "lxpanel Fedora maintainer"
git config user.email "lxpanel-owner@fedoraproject.org"

%if 0%{?use_release}
git add .
git commit -m "base" -q
%endif

%build
%if 0%{?use_gitbare}
cd %{name}
%endif

bash autogen.sh
%configure \
	--enable-gtk3 \
	%{nil}
%make_build

%install
%if 0%{?use_gitbare}
cd %{name}
%endif

%make_install

desktop-file-install \
	--delete-original \
	--dir=%{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?use_gitbare}
cd ..
%endif

%find_lang %{name}

%files -f %{name}.lang
%doc	AUTHORS
%doc	ChangeLog
%doc	README
%doc	TODO
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_mandir}/man1/lxtask.1*

%changelog
%autochangelog
