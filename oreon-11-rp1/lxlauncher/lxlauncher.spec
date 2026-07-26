%global source0_hash 2bc21d181b1998db1ceef01d4c73786d3ef433cca9e237f1331266acf3b4f02e

# Review at https://bugzilla.redhat.com/show_bug.cgi?id=452395

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
%global		gittardate		20250329
%global		gittartime		1503
%define		use_gitcommit_as_rel		0

%global		gitbaredate	20250328
%global		git_rev		4266f49fcc519346f9f509e4eed991383eb110ad
%global		git_short		%(echo %{git_rev} | cut -c-8)
%global		git_version	%{gitbaredate}git%{git_short}
%endif

%if 0%{?use_gitcommit_as_rel}
%global		git_ver_rpm	^%{git_version}
%global		git_builddir	-%{git_version}
%endif

%global		main_version	0.2.8

Name:           lxlauncher
Version:        0.2.8
Release:        3%{?dist}
Summary:        Open source replacement for Launcher on the EeePC

# src/exo-wrap-table.c	LGPL-2.0-or-later
# Otherwise	GPL-2.0-or-later
# SPDX confirmed
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            http://lxde.org/
%if 0%{?use_gitbare}
Source0:		%{name}-%{gittardate}T%{gittartime}.tar.gz
%endif
%if 0%{?use_release}
Source0:		https://github.com/lxde/%{name}/archive/%{main_version}/%{name}-%{version}.tar.gz
%endif
Source1:		create-%{name}-git-bare-tarball.sh

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(libmenu-cache)
BuildRequires:  pkgconfig(x11)
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  intltool

%description
LXLauncher is designed as an open source replacement for the Asus Launcher
included in their EeePC. It is desktop-independent and follows 
freedesktop.org specs, so newly added applications will automatically show 
up in the launcher, and vice versa for the removed ones.
LXLauncher is part of LXDE, the Lightweight X11 Desktop Environment.

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

git config user.name "%{name} Fedora maintainer"
git config user.email "%{name}-maintainers@fedoraproject.org"

%if 0%{?use_release}
git add .
git commit -m "base" -q
%endif

sh autogen.sh

%build
%if 0%{?use_gitbare}
cd %{name}
%endif

%configure --disable-silent-rules
# workaround for FTBFS #539147 and #661008
#touch -r po/Makefile po/stamp-it
%make_build

%install
%if 0%{?use_gitbare}
cd %{name}
%endif

%make_install
mkdir -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/backgrounds
mkdir -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/icons

%if 0%{?use_gitbare}
cd ..
%endif
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS
%doc README
%license COPYING

%dir %{_sysconfdir}/xdg/lxlauncher/
%config(noreplace) %{_sysconfdir}/xdg/lxlauncher/gtkrc
%config(noreplace) %{_sysconfdir}/xdg/lxlauncher/gtk.css
%config(noreplace) %{_sysconfdir}/xdg/lxlauncher/settings.conf
%config(noreplace) %{_sysconfdir}/xdg/menus/lxlauncher-applications.menu
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/desktop-directories/lxde-*.directory
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
