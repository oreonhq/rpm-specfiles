%global source0_hash 075920b826834ac4ddf97661cc73491047855859affd671d52079c6867c1c6c0

Name:           libjpeg-turbo
Version:        3.1.3
Release:        1%{?dist}
Summary:        A MMX/SSE2/SIMD accelerated library for manipulating JPEG image files
License:        Zlib AND BSD-3-Clause AND MIT AND IJG
URL:            https://github.com/%{name}/%{name}

Source0:        https://github.com/libjpeg-turbo/libjpeg-turbo/releases/download/3.1.3/libjpeg-turbo-3.1.3.tar.gz
Patch0:         libjpeg-turbo-cmake.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  libtool
BuildRequires:  nasm

Obsoletes:      libjpeg < 6b-47
# add provides (even if it not needed) to workaround bad packages, like
# java-1.6.0-openjdk (#rh607554) -- atkac
Provides:       libjpeg = 6b-47%{?dist}
%if "%{?_isa}" != ""
Provides:       libjpeg%{_isa} = 6b-47%{?dist}
%endif

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
%autosetup -p1 -S gendiff

#rm -rf doc

%build
# NASM object files are missing GNU Property note for Intel CET,
# force it on the resulting library
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

# Remove tjbench
rm -f %{buildroot}/%{_bindir}/tjbench

# Fix perms
chmod -x README.md

# multilib header hack
# we only apply this to known Red Hat multilib arches, per bug #1264675
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
#ifndef JCONFIG_H_MULTILIB
#define JCONFIG_H_MULTILIB

#include <bits/wordsize.h>

# if __WORDSIZE == 32
# include "jconfig-32.h"
#elif __WORDSIZE == 64
# include "jconfig-64.h"
#else
# error "unexpected value for __WORDSIZE macro"
# endif

# endif
EOF

fi

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest

%ldconfig_scriptlets
%ldconfig_scriptlets -n turbojpeg

%files
%license LICENSE.md
%doc README.md README.ijg ChangeLog.md
%{_libdir}/libjpeg.so.62*

%files devel
%doc doc/coderules.txt src/jconfig.txt doc/libjpeg.txt doc/structure.txt
%{_includedir}/jconfig*.h
%{_includedir}/jerror.h
%{_includedir}/jmorecfg.h
%{_includedir}/jpegint.h
%{_includedir}/jpeglib.h
%{_libdir}/libjpeg.so
%{_libdir}/pkgconfig/libjpeg.pc
%{_libdir}/cmake/%{name}/%{name}*.cmake

%files utils
%doc doc/usage.txt doc/wizard.txt
%{_bindir}/cjpeg
%{_bindir}/djpeg
%{_bindir}/jpegtran
%{_bindir}/rdjpgcom
%{_bindir}/wrjpgcom
%{_mandir}/man1/cjpeg.1*
%{_mandir}/man1/djpeg.1*
%{_mandir}/man1/jpegtran.1*
%{_mandir}/man1/rdjpgcom.1*
%{_mandir}/man1/wrjpgcom.1*

%files -n turbojpeg
%license LICENSE.md
%doc README.md README.ijg ChangeLog.md
%{_libdir}/libturbojpeg.so.0*

%files -n turbojpeg-devel
%{_includedir}/turbojpeg.h
%{_libdir}/libturbojpeg.so
%{_libdir}/pkgconfig/libturbojpeg.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1.3-1
- Prepare for Oreon 11 (RP1)
