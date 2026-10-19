%global source0_hash eef1b92d74ac07fde58c043f64e8cac02b5400c209c44dcbb51641f86e0c7c83
Name:           CheMPS2
Version:        1.8.12
Release:        1%{?dist}
Summary:        A spin-adapted implementation of DMRG for ab initio quantum chemistry
License:        GPL-2.0-or-later
URL:            https://github.com/SebWouters/CheMPS2
Source0:        https://github.com/SebWouters/CheMPS2/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         CheMPS-1.8.9-cmake4.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  pkgconfig(flexiblas)
BuildRequires:  zlib-devel
# /oreon:deps
%description    
The CheMPS2 library provides a free open-source spin-adapted 
implementation of the density matrix renormalization group (DMRG) for ab initio 
quantum chemistry. This method allows to obtain numerical accuracy in active 
spaces beyond the capabilities of full configuration interaction. For the 
input Hamiltonian and targeted symmetry sector, the library performs successive 
DMRG sweeps according to a user-defined convergence scheme. As output, the 
library returns the minimal encountered energy as well as the 2-RDM of the 
active space. The latter allows to calculate various properties, as well as 
the gradient and Hessian for orbital rotations or nuclear displacements.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p 1 -b .cmake4

%build

export CXXFLAGS="%{optflags} -Wl,--as-needed"
%cmake -DMKL=OFF -DLAPACK_LIBRARIES="-lflexiblas" -DENABLE_XHOST=OFF -DSHARED_ONLY=ON
%cmake_build
%install
%cmake_install
install -D -p -m 644 chemps2.1 %{buildroot}%{_mandir}/man1/chemps2.1
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles CheMPS2-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n CheMPS2-devel -f %{oreon_filedir}/CheMPS2-devel.list

%changelog

%autochangelog
