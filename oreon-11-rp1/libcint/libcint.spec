%global source0_hash none

%global soversion 6

Name:           libcint
Version:        6.1.3
Release:        2%{?dist}
Summary:        General Gaussian-type orbitals integrals for quantum chemistry
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/sunqm/libcint
Source0:        https://github.com/sunqm/libcint/archive/v%{version}/libcint-%{version}.tar.gz

BuildRequires:  gcc-gfortran
BuildRequires:  cmake
BuildRequires:  python3-devel
BuildRequires:  python3-numpy

# For documentation
BuildRequires:  pandoc
BuildRequires:  tex(latex)
BuildRequires:  make

# ppc64 doesn't appear to have floats beyond 64 bits, so ppc64 is
# disabled as per upstream's request
ExcludeArch:    %{power64}
# Exclude x86_64 since that platform has an API compatible library
# qcint, which however is ABI incompatible with libcint. We prefer to
# use the faster implementation.
ExcludeArch:    x86_64

%description
libcint is an open source library for analytical Gaussian integrals.
It provides C/Fortran API to evaluate one-electron / two-electron
integrals for Cartesian / real-spherical / spinor Gaussian type functions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
# Replace name of build directory in test suite
for f in testsuite/*.py; do
    sed -i 's|../../build/libcint.so|../../%{_build}/libcint.so|g' $f
done

%build
export CFLAGS="%{optflags} -Wl,--as-needed"
%cmake -DENABLE_EXAMPLE=1 -DWITH_F12=1 -DWITH_COULOMB_ERF=1 -DWITH_RANGE_COULOMB=1 -DENABLE_TEST=1 -DQUICK_TEST=1 -S . -B %{_host}
%make_build -C %{_host}

# Build documentation
cd doc
bash compile.sh

%install
%make_install -C %{_host}

%check
make -C %{_host} test ARGS=-V

%files
%doc README.rst ChangeLog
%license LICENSE
%{_libdir}/libcint.so.%{soversion}*

%files devel
%doc doc/program_ref.pdf
%{_includedir}/cint.h
%{_includedir}/cint_funcs.h
%{_libdir}/libcint.so

%changelog
%autochangelog
