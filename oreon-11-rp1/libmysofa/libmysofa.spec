%global source0_hash 11dabd3b69d2cd7a0c01b680e9e64b3c4aa4f0b99b55e58f10a17f043d38e4c4
%global commit 4585a0ae5bc98894750baf70e7f7989360e5a376

Name:           libmysofa
Version:        1.3.3
Release:        %autorelease
Summary:        C functions for reading HRTFs

License:        BSD-3-Clause
URL:            https://github.com/hoene/libmysofa
Source0:        https://github.com/hoene/libmysofa/archive/%{commit}.tar.gz#/libmysofa-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(cunit)
BuildRequires:  pkgconfig(zlib)
BuildRequires: make
# for tests
%{?!_without_tests:BuildRequires: nodejs, /usr/bin/node}


%description
This is a simple set of C functions to read AES SOFA files, if they
contain HRTFs stored according to the AES69-2015 standard.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n mysofa
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n mysofa
Tools for %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n libmysofa-%{commit}


%build
%cmake \
  -DBUILD_STATIC_LIBS=OFF \
  -DCODE_COVERAGE=OFF \
  -DCMAKE_VERBOSE_MAKEFILE=ON

%cmake_build


%install
%cmake_install


%{?!_without_tests:
%check
export MYSOFA2JSON=%{_builddir}/%{buildsubdir}/%{_vpath_builddir}/src/mysofa2json
%ctest
}


%files
%license LICENSE
%doc README.md
%{_libdir}/libmysofa.so.1*

%files -n mysofa
%{_bindir}/mysofa2json
%dir %{_datadir}/libmysofa
%{_datadir}/libmysofa/default.sofa
%{_datadir}/libmysofa/MIT_KEMAR_normal_pinna.sofa

%files devel
%doc CODE_OF_CONDUCT.md
%{_includedir}/mysofa.h
%{_includedir}/mysofa_export.h
%{_libdir}/libmysofa.so
%{_libdir}/pkgconfig/libmysofa.pc
%dir %{_libdir}/cmake/mysofa
%{_libdir}/cmake/mysofa/mysofaConfig.cmake
%{_libdir}/cmake/mysofa/mysofaConfigVersion.cmake
%{_libdir}/cmake/mysofa/mysofaTargets-noconfig.cmake
%{_libdir}/cmake/mysofa/mysofaTargets.cmake

%changelog
%autochangelog
