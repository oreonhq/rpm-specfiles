%global source0_hash a3c2b80201b89e68616f4ad30bc66aee4927c3ce50e33929ca819d5c43538898

#
# Important for %%{ix86}:
# This rpm has to be build on a CPU with sse2 support like Pentium 4 !
#

Summary: GNU arbitrary precision library
Name: gmp
Version: 6.3.0
Release: 5%{?dist}
Epoch: 1
URL: https://gmplib.org/
Source0:        https://gmplib.org/download/gmp/gmp-%{version}.tar.xz
Source2: gmp.h
Source3: gmp-mparam.h
Patch2: gmp-6.0.0-debuginfo.patch
Patch3: gmp-intel-cet.patch
# https://gmplib.org/repo/gmp/rev/8e7bb4ae7a18
Patch4: gmp-6.3.0-c23.patch
# https://gmplib.org/list-archives/gmp-devel/2023-August/006198.html
# https://gmplib.org/repo/gmp/rev/372acfd0c33e
Patch5: gmp-6.3.0-s390x-popcount.patch
Patch6: gmp-devel-arm64-pac-bti.patch
# * Main sources are dual licensed under LGPL-3.0-or-later and GPL-2.0-or-later
#   Either only one may be active or both simultaneously.
# * Some docs are under GFDL-1.3-invariants-or-later.
# * demos are under GPL-3.0-or-later but they are NOT shipped.
# * tests are under GPL-3.0-or-later but they are NOT shipped.
License: (LGPL-3.0-or-later OR GPL-2.0-or-later OR (LGPL-3.0-or-later AND GPL-2.0-or-later)) AND GFDL-1.3-invariants-or-later

BuildRequires: autoconf automake libtool
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: git
# Generate the .hmac checksum unless --without fips is used
%bcond_without fips
%if %{with fips}
BuildRequires: fipscheck
%endif
BuildRequires: make

%description
The gmp package contains GNU MP, a library for arbitrary precision
arithmetic, signed integers operations, rational numbers and floating
point numbers. GNU MP is designed for speed, for both small and very
large operands. GNU MP is fast because it uses fullwords as the basic
arithmetic type, it uses fast algorithms, it carefully optimizes
assembly code for many CPUs' most common inner loops, and it generally
emphasizes speed over simplicity/elegance in its operations.

Install the gmp package if you need a fast arbitrary precision
library.

%package c++
Summary: C++ bindings for the GNU MP arbitrary precision library
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description c++
Bindings for using the GNU MP arbitrary precision library in C++ applications.

%package devel
Summary: Development tools for the GNU MP arbitrary precision library
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: %{name}-c++%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
The libraries, header files and documentation for using the GNU MP 
arbitrary precision library in applications.

If you want to develop applications which will use the GNU MP library,
you'll need to install the gmp-devel package.  You'll also need to
install the gmp package.

%package static
Summary: Development tools for the GNU MP arbitrary precision library
Requires: %{name}-devel = %{epoch}:%{version}-%{release}

%description static
The static libraries for using the GNU MP arbitrary precision library 
in applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git

%build
autoreconf -ifv
if as --help | grep -q execstack; then
  # the object files do not require an executable stack
  export CCAS="gcc -c -Wa,--noexecstack"
fi

%ifarch %{ix86}
  export CFLAGS=$(echo %{optflags} | sed -e "s/-mtune=[^ ]*//g" | sed -e "s/-march=[^ ]*/-march=i686/g")
  export CXXFLAGS=$(echo %{optflags} | sed -e "s/-mtune=[^ ]*//g" | sed -e "s/-march=[^ ]*/-march=i686/g")
%endif

# set baseline to z13
%ifarch s390x
  export MPN_PATH="s390_64/z13 s390_64 generic"
%endif

%configure --enable-cxx --enable-fat

sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|-lstdc++ -lm|-lstdc++|' \
    -i libtool
export LD_LIBRARY_PATH=`pwd`/.libs
%make_build

%if %{with fips}
%define __spec_install_post \
    %{?__debug_package:%{__debug_install_post}} \
    %{__arch_install_post} \
    %{__os_install_post} \
    fipshmac -d $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_libdir}/libgmp.so.10.* \
    file=`basename $RPM_BUILD_ROOT%{_libdir}/libgmp.so.10.*.hmac` && \
        mv $RPM_BUILD_ROOT%{_libdir}/$file $RPM_BUILD_ROOT%{_libdir}/.$file && \
        ln -s .$file $RPM_BUILD_ROOT%{_libdir}/.libgmp.so.10.hmac
%{nil}
%endif

%install
export LD_LIBRARY_PATH=`pwd`/.libs
%make_install 
install -m 644 gmp-mparam.h ${RPM_BUILD_ROOT}%{_includedir}
rm -f $RPM_BUILD_ROOT%{_libdir}/lib{gmp,mp,gmpxx}.la
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
/sbin/ldconfig -n $RPM_BUILD_ROOT%{_libdir}
ln -sf libgmpxx.so.4 $RPM_BUILD_ROOT%{_libdir}/libgmpxx.so

# Rename gmp.h to gmp-<arch>.h and gmp-mparam.h to gmp-mparam-<arch>.h to 
# avoid file conflicts on multilib systems and install wrapper include files
# gmp.h and gmp-mparam-<arch>.h
basearch=%{_arch}
# always use i386 for iX86
%ifarch %{ix86}
basearch=i386
%endif
# Rename files and install wrappers

mv %{buildroot}/%{_includedir}/gmp.h %{buildroot}/%{_includedir}/gmp-${basearch}.h
install -m644 %{SOURCE2} %{buildroot}/%{_includedir}/gmp.h
mv %{buildroot}/%{_includedir}/gmp-mparam.h %{buildroot}/%{_includedir}/gmp-mparam-${basearch}.h
install -m644 %{SOURCE3} %{buildroot}/%{_includedir}/gmp-mparam.h


%check
export LD_LIBRARY_PATH=`pwd`/.libs
%make_build check

%ldconfig_scriptlets

%ldconfig_scriptlets c++

%files
%license COPYING COPYING.LESSERv3 COPYINGv2 COPYINGv3
%doc NEWS README
%{_libdir}/libgmp.so.*
%if %{with fips}
%{_libdir}/.libgmp.so.*.hmac
%endif

%files c++
%{_libdir}/libgmpxx.so.*

%files devel
%{_libdir}/libgmp.so
%{_libdir}/libgmpxx.so
%{_libdir}/pkgconfig/gmp.pc
%{_libdir}/pkgconfig/gmpxx.pc
%{_includedir}/*.h
%{_infodir}/gmp.info*

%files static
%{_libdir}/libgmp.a
%{_libdir}/libgmpxx.a

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.3.0-5
- Prepare for Oreon 11 (RP1)
