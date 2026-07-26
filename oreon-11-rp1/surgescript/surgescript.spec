%global source0_hash 664151bb8c3d66de370ea6c2ae55f271d715f2c4b24bcc5758eb1ba33ed3a691

Name: surgescript
Summary: Scripting language for games

# All of SurgeScript's original code is licensed
# under the Apache License.
#
# There are a couple files borrowed from other projects
# that use different licenses.
#
# BSD-1-Clause:
# - src/surgescript/third_party/uthash.h
# BSD-2-Clause:
# - src/surgescript/third_party/xxhash.c
# - src/surgescript/third_party/xxhash.h
# MIT:
# - src/surgescript/third_party/gettimeofday.h
# Public Domain:
# - src/surgescript/third_party/xoroshiro128plus.c
# - src/surgescript/third_party/utf8.c
# - src/surgescript/third_party/utf8.h
License: Apache-2.0 AND BSD-1-Clause AND BSD-2-Clause AND LicenseRef-Fedora-Public-Domain

Version: 0.6.1
Release: 5%{?dist}

URL: https://opensurge2d.org
Source0: https://github.com/alemart/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make

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
# TODO: Please submit an issue to upstream (rhbz#2381469)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake \
	-DWANT_SHARED=ON  \
	-DWANT_STATIC=ON  \
	-DWANT_EXECUTABLE=ON  \
	-DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

# "make install" also installs an AppStream metainfo file and an icon
# for the surgescript interpreter, which is a terminal-based program.
# Remove those.
rm -rf %{buildroot}%{_metainfodir}
rm -rf %{buildroot}%{_datadir}/pixmaps/
rmdir %{buildroot}%{_datadir}

%files
%doc docs/
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.%{version}

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files static
%{_libdir}/lib%{name}-static.a
%{_libdir}/pkgconfig/%{name}-static.pc

%changelog
%autochangelog
