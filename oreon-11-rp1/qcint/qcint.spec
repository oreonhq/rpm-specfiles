%global source0_hash none

%global soversion 6

Name:           qcint
Version:        6.1.3
Release:        2%{?dist}
Summary:        An optimized libcint branch for X86 platform with SSE3 intrinsics
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/sunqm/qcint
Source0:        https://github.com/sunqm/qcint/archive/v%{version}/qcint-%{version}.tar.gz

# This package uses AVX/AVX2/AVX-512 extensions
ExclusiveArch:  x86_64
# qcint is a drop-in replacement of libcint with architecture
# dependent optimizations. The libraries are API compatible, but ABI
# incompatible.
Provides:       libcint = %{version}-%{release}
Obsoletes:      libcint < %{version}-%{release}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake 

%description    
Qcint is a branch of the libcint library.  It provides exactly the
same APIs as libcint. However, the code is optimized using AVX
instructions. On x86_64 platform, qcint can be 5 ~ 50% faster than
libcint. Please refer to libcint for more details of the features.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       libcint-devel = %{version}-%{release}
Obsoletes:      libcint-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
# Fix to https://github.com/sunqm/qcint/issues/22
find . -name *.c -exec sed -i 's|//ALL_CINT_FORTRAN_(cint|ALL_CINT_FORTRAN_(int|g' {} \;

%build
export CFLAGS="%{optflags} -msse3 -Wl,--as-needed"
%cmake -DENABLE_EXAMPLE=1 -DWITH_F12=1 -DWITH_COULOMB_ERF=1 -DWITH_RANGE_COULOMB=1 -DQUICK_TEST=1 -DBUILD_MARCH_NATIVE=OFF -S . -B %{_host}
%make_build -C %{_host}

%install
%make_install -C %{_host}

%ldconfig_scriptlets

%files
%doc README.md ChangeLog
%license LICENSE
%{_libdir}/libcint.so.%{soversion}*

%files devel
%{_includedir}/cint.h
%{_includedir}/cint_funcs.h
%{_libdir}/libcint.so

%changelog
%autochangelog
