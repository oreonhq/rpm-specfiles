%global source0_hash f99d1c13aa5fa296898a181dff9b82fb25f6cc0933dbaa7a475d8109bd54209d

Name:           graphite2
Version:        1.3.14
Release:        20%{?dist}
Summary:        Font rendering capabilities for complex non-Roman writing systems

# As per COPYING file this library is tri-licensed
License:        LGPL-2.1-or-later OR MPL-2.0 OR GPL-2.0-or-later

URL:            https://sourceforge.net/projects/silgraphite/
Source0:        https://downloads.sourceforge.net/project/silgraphite/graphite2//graphite2-1.3.14.tgz

Patch0:         graphite-arm-nodefaultlibs.patch
Patch1:         graphite2-1.2.0-cmakepath.patch
# This fixes compilation with gcc15
Patch2:         graphite2-1.3.14-gcc15.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  freetype-devel

# needed for running the test suite
BuildRequires:  python3-fonttools

%description
Graphite2 is a project within SIL’s Non-Roman Script Initiative and Language
Software Development groups to provide rendering capabilities for complex
non-Roman writing systems. Graphite can be used to create “smart fonts” capable
of displaying writing systems with various complex behaviors. With respect to
the Text Encoding Model, Graphite handles the "Rendering" aspect of writing
system implementation.


%package devel
Summary:        Files for developing with graphite2
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Includes and definitions for developing with graphite2.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1


%build
%cmake -DGRAPHITE2_COMPARE_RENDERER=OFF
%cmake_build


%install
%cmake_install

find %{buildroot} -type f -name "*.la" -print -delete


%check
%ctest -E 'nametabletest'


%files
%license LICENSE COPYING
%doc ChangeLog README.md

%{_bindir}/gr2fonttest

%{_libdir}/libgraphite2.so.3*


%files devel
%{_includedir}/%{name}/

%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/graphite2-release.cmake
%{_libdir}/%{name}/graphite2.cmake

%{_libdir}/libgraphite2.so
%{_libdir}/pkgconfig/graphite2.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.14-20
- Prepare for Oreon 11 (RP1)
