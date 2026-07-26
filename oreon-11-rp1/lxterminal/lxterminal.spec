%global source0_hash baecedaeea9fe9f23d3782eb20810ecd2d321672cb4f208048fb095e6cfb16fc

%global		use_release	0
%global		use_git		0
%global		use_gitbare	1

%if 0%{?use_git} < 1
%if 0%{?use_gitbare} < 1
# force
%global		use_release	1
%endif
%endif

%global		git_version	%{nil}
%global		git_ver_rpm	%{nil}
%global		git_builddir	%{nil}

%if 0%{?use_gitbare}
%global		gittardate		20250417
%global		gittartime		1433
%define		use_gitcommit_as_rel		1

%global		gitbaredate	20250415
%global		git_rev		ac5e36f496b2bf95eae790181e65c9eb54bb9c13
%global		git_short		%(echo %{git_rev} | cut -c-8)
%global		git_version	%{gitbaredate}git%{git_short}
%endif

%if 0%{?use_gitcommit_as_rel}
%global		git_ver_rpm	^%{git_version}
%global		git_builddir	-%{git_version}
%endif

%global		main_version	0.4.1

%dnl	%global		use_gcc_strict_sanitize	1

%undefine		_changelog_trimtime

%global		baserelease	3

Name:			lxterminal
Version:		%{main_version}%{git_ver_rpm}
Release:		%{baserelease}%{?dist}%{?use_gcc_strict_sanitize:.san}
Summary:		Desktop-independent VTE-based terminal emulator
Summary(de):	Desktop-unabhängiger VTE-basierter Terminal Emulator

# SPDX confirmed
License:		GPL-2.0-or-later
URL:			http://lxde.sourceforge.net/
%if 0%{?use_gitbare}
Source0:		%{name}-%{main_version}-%{gittardate}T%{gittartime}.tar.gz
%endif
%if 0%{?use_release}
Source0:		http://downloads.sourceforge.net/sourceforge/lxde/%{name}-%{main_version}.tar.xz
%endif
# Shell script to create tarball from git scm
Source100:		create-lxterminal-git-bare-tarball.sh

BuildRequires:	git

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(vte-2.91)

BuildRequires:	/usr/bin/xsltproc
BuildRequires:	docbook-utils
BuildRequires:	docbook-style-xsl

BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	gettext

%if 0%{?git_snapshot}
BuildRequires:	automake
BuildRequires:	libtool
%endif

%if 0%{?use_gcc_strict_sanitize}
BuildRequires:	libasan
BuildRequires:	libubsan
%endif

%description
LXterminal is a VTE-based terminal emulator with support for multiple tabs. 
It is completely desktop-independent and does not have any unnecessary 
dependencies. In order to reduce memory usage and increase the performance 
all instances of the terminal are sharing a single process.

%description -l de
LXTerminal ist ein VTE-basierter Terminalemulator mit Unterstützung für 
mehrere Reiter. Er ist komplett desktop-unabhängig und hat keine unnötigen 
Abhängigkeiten. Um den Speicherverbrauch zu reduzieren und die Leistung zu
erhöhen teilen sich alle Instanzen des Terminals einen einzigen Prozess.

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
%global optflags_orig %optflags
%global optflags %optflags_orig -fno-optimize-sibling-calls

%if 0%{?use_gcc_strict_sanitize}
export CC="${CC} -fsanitize=address -fsanitize=undefined"
export LDFLAGS="${LDFLAGS} -pthread"
%endif

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
	--remove-category=Utility \
	--add-category=System \
	--dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
	${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop

%if 0%{?use_gitbare}
cd ..
%endif

%find_lang %{name}

%files -f %{name}.lang
%doc	AUTHORS
%license	COPYING
%doc	NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}*.1*

%changelog
%autochangelog
