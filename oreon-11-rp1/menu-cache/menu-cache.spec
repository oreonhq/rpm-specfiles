%global source0_hash e8af90467df271c3c8700c840ca470ca2915699c6f213c502a87d74608748f08

%global		use_release	1
%global		use_git		0
%global		use_gitbare	0

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
Release:        3%{?dist}
Summary:        Caching mechanism for freedesktop.org compliant menus

# SPDX confirmed
License:        LGPL-2.0-or-later
URL:            http://lxde.org
%if 0%{?use_gitbare}
Source0:        %{name}-%{gittardate}T%{gittartime}.tar.gz
%endif
%if 0%{?use_release}
Source0:        https://github.com/lxde/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%endif
Source1:        create-menu-cache-git-bare-tarball.sh

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libfm-extra)
BuildRequires:	automake
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:  /usr/bin/git

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

%files
#FIXME: add ChangeLog and NEWS if there is content
%doc AUTHORS
%license COPYING
%doc NEWS
%doc README
%{_libexecdir}/%{name}/menu-cache-gen
%{_libexecdir}/%{name}/menu-cached
%{_libdir}/libmenu-cache.so.3*
#%{_mandir}/man*/*.gz

%files devel
%dir %{_includedir}/menu-cache/
%{_includedir}/menu-cache/*.h
%{_libdir}/libmenu-cache.so
%{_libdir}/pkgconfig/libmenu-cache.pc

%changelog
%autochangelog
