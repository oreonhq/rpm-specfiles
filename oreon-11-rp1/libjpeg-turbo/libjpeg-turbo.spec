%global source0_hash 6f30092cef9fb839779646608f4ee14ae3cbac989c47fa05e841b0841f09878e
Name:           libjpeg-turbo
Version:        3.2.0
Release:        1%{?dist}
Summary:        A MMX/SSE2/SIMD accelerated library for manipulating JPEG image files
License:        Zlib AND BSD-3-Clause AND MIT AND IJG
URL:            https://github.com/%{name}/%{name}
Source0:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:         libjpeg-turbo-cmake.patch
Obsoletes:      libjpeg < 6b-47
Provides:       libjpeg = 6b-47%{?dist}
%if "%{?_isa}" != ""
Provides:       libjpeg%{_isa} = 6b-47%{?dist}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  nasm
# /oreon:deps
%description
The libjpeg-turbo package contains a library of functions for manipulating JPEG
images.

%package devel
Summary:        Headers for the libjpeg-turbo library
Obsoletes:      libjpeg-devel < 6b-47
Provides:       libjpeg-devel = 6b-47%{?dist}
%if "%{?_isa}" != ""
Provides:       libjpeg-devel%{_isa} = 6b-47%{?dist}
%endif
Requires:       libjpeg-turbo%{?_isa} = %{version}-%{release}
Obsoletes:      libjpeg-turbo-static < 1.3.1
Provides:       libjpeg-turbo-static = 1.3.1%{?dist}
%description devel
This package contains header files necessary for developing programs which will
manipulate JPEG files using the libjpeg-turbo library.

%package utils
Summary:        Utilities for manipulating JPEG images
Requires:       libjpeg-turbo%{?_isa} = %{version}-%{release}
%description utils
The libjpeg-turbo-utils package contains simple client programs for accessing
the libjpeg functions. It contains cjpeg, djpeg, jpegtran, rdjpgcom and
wrjpgcom. Cjpeg compresses an image file into JPEG format. Djpeg decompresses a
JPEG file into a regular image file. Jpegtran can perform various useful
transformations on JPEG files. Rdjpgcom displays any text comments included in a
JPEG file. Wrjpgcom inserts text comments into a JPEG file.

%package -n turbojpeg
Summary:        TurboJPEG library
%description -n turbojpeg
The turbojpeg package contains the TurboJPEG shared library.

%package -n turbojpeg-devel
Summary:        Headers for the TurboJPEG library
Requires:       turbojpeg%{?_isa} = %{version}-%{release}
%description -n turbojpeg-devel
This package contains header files necessary for developing programs which will
manipulate JPEG files using the TurboJPEG library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%ifarch %{ix86} x86_64
export LDFLAGS="$RPM_LD_FLAGS -Wl,-z,ibt -Wl,-z,shstk"
%endif
%{cmake} -DCMAKE_SKIP_RPATH:BOOL=YES \
         -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
%ifarch s390x riscv64
         -DFLOATTEST:STRING="fp-contract" \
%endif
         -DENABLE_STATIC:BOOL=NO
%cmake_build
%install
%cmake_install
find %{buildroot} -name "*.la" -delete
rm -f %{buildroot}/%{_bindir}/tjbench
chmod -x README.md
case `uname -i` in
  i386 | ppc | s390 | sparc )
    wordsize="32"
    ;;
  x86_64 | ppc64 | s390x | sparc64 )
    wordsize="64"
    ;;
  *)
    wordsize=""
    ;;
esac
if test -n "$wordsize"
then
  mv $RPM_BUILD_ROOT%{_includedir}/jconfig.h \
     $RPM_BUILD_ROOT%{_includedir}/jconfig-$wordsize.h
  cat >$RPM_BUILD_ROOT%{_includedir}/jconfig.h <<EOF
EOF
fi
%oreon_autofiles turbojpeg usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles turbojpeg-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest
%ldconfig_scriptlets
%ldconfig_scriptlets -n turbojpeg
%files -f %{oreon_filedir}/main.list
%files -n libjpeg-turbo-devel -f %{oreon_filedir}/libjpeg-turbo-devel.list
%files -n libjpeg-turbo-utils -f %{oreon_filedir}/libjpeg-turbo-utils.list
%files -n turbojpeg -f %{oreon_filedir}/turbojpeg.list
%files -n turbojpeg-devel -f %{oreon_filedir}/turbojpeg-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1.3-1
- Prepare for Oreon 11 (RP1)
