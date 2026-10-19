%global source0_hash 664151bb8c3d66de370ea6c2ae55f271d715f2c4b24bcc5758eb1ba33ed3a691
Name: surgescript
Summary:        Scripting language for games
License: Apache-2.0 AND BSD-1-Clause AND BSD-2-Clause AND LicenseRef-Fedora-Public-Domain
Version: 0.6.1
Release:        1%{?dist}
URL: https://opensurge2d.org
Source0:        https://github.com/alemart/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
SurgeScript is a scripting language for games. It has been designed
with the specific needs of games in mind. Its features include:
- The state-machine pattern: objects are state machines,
  making it easy to create in-game entities
- The composition approach: you may design complex objects
  and behaviors by means of composition
- The hierarchy system: objects have a parent and may have children,
  in a tree-like structure
- The game loop: it's defined implicitly
- Automatic garbage collection, object tagging and more!

SurgeScript is meant to be used in games and in interactive applications.
It's easy to integrate it into existing code, it's easy to extend,
it features a C-like syntax, and it's free and open-source software.

SurgeScript has been designed based on the experience of its developer
dealing with game engines, applications related to computer graphics and so on.
Some of the best practices have been incorporated into the language itself,
making things really easy for developers and modders.

# -- devel

%package devel
Summary: Files for developing applications using %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains files required for
developing applications using %{name}.

# -- static

%package static
Summary: Files for developing applications using %{name}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description static
This package contains files required for
developing applications using %{name},
using static linking.

# -- subpackages end

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake \
	-DWANT_SHARED=ON  \
	-DWANT_STATIC=ON  \
	-DWANT_EXECUTABLE=ON  \
	-DCMAKE_BUILD_TYPE=Release
%cmake_build
%install
%cmake_install
rm -rf %{buildroot}%{_metainfodir}
rm -rf %{buildroot}%{_datadir}/pixmaps/
rmdir %{buildroot}%{_datadir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n surgescript-devel -f %{oreon_filedir}/surgescript-devel.list
%files -n surgescript-static -f %{oreon_filedir}/surgescript-static.list

%changelog

%autochangelog
