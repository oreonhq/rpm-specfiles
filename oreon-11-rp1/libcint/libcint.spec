%global source0_hash e4d977d4aeb4d5b87639ea57a2d2f1d5c1001f3f94e480b08c297a6cbc186f27
%global soversion 6
Name:           libcint
Version:        6.1.3
Release:        1%{?dist}
Summary:        General Gaussian-type orbitals integrals for quantum chemistry
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/sunqm/libcint
Source0:        https://github.com/sunqm/libcint/archive/v%{version}/libcint-%{version}.tar.gz
ExcludeArch:    %{power64}
ExcludeArch:    x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-gfortran
BuildRequires:  make
BuildRequires:  pandoc
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  tex(latex)
# /oreon:deps
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
cd doc
bash compile.sh
%install
%make_install -C %{_host}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make -C %{_host} test ARGS=-V
%files -f %{oreon_filedir}/main.list
%files -n libcint-devel -f %{oreon_filedir}/libcint-devel.list

%changelog

%autochangelog
