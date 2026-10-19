%global source0_hash e8af90467df271c3c8700c840ca470ca2915699c6f213c502a87d74608748f08
%global		use_release	1
%global		use_git		0
%global		use_gitbare	0
%if 0%{?use_git} < 1
%if 0%{?use_gitbare} < 1
%global		use_release	1
%endif
%endif
%global		git_version	%{nil}
%global		git_ver_rpm	%{nil}
%global		git_builddir	%{nil}
%if 0%{?use_gitbare}
%global		gittardate		20250209
%global		gittartime		1612
%global		gitbaredate	20250128
%global		git_rev		18bad9324b9e8990c73a67cee9b87d551d34be91
%global		git_short		%(echo %{git_rev} | cut -c-8)
%global		git_version	%{gitbaredate}git%{git_short}
%endif
%if 0%{?use_git} || 0%{?use_gitbare}
%global		git_ver_rpm	^%{git_version}
%global		git_builddir	-%{git_version}
%endif
%global		main_version	1.1.1
Name:           menu-cache
Version:        %{main_version}%{git_ver_rpm}
Release:        1%{?dist}
Summary:        Caching mechanism for freedesktop.org compliant menus
License:        LGPL-2.0-or-later
URL:            http://lxde.org
%if 0%{?use_gitbare}
Source0:        https://github.com/lxde/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%endif
%if 0%{?use_release}
%endif
Source1:        create-menu-cache-git-bare-tarball.sh
# oreon:deps
BuildRequires:  /usr/bin/git
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libfm-extra)
# /oreon:deps
%description
Menu-cache is a caching mechanism for freedesktop.org compliant menus to 
speed up parsing of the menu entries. It is currently used by some of 
components of the LXDE desktop environment such as LXPanel or LXLauncher.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

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
%configure --disable-static --disable-silent-rules
%make_build
%install
%if 0%{?use_gitbare}
cd %{name}
%endif
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n menu-cache-devel -f %{oreon_filedir}/menu-cache-devel.list

%changelog

%autochangelog
