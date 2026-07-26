%global source0_hash ccd4c0d9432759d97690bf37a0333440f93513960c62d1f75842f090406a224d

Name:           CheMPS2
Version:        1.8.9
Release:        32%{?dist}
Summary:        A spin-adapted implementation of DMRG for ab initio quantum chemistry

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/SebWouters/CheMPS2
Source0:        https://github.com/SebWouters/CheMPS2/archive/v%{version}/%{name}-%{version}.tar.gz

# Allow to build for CMake 4.0, adapted from https://github.com/SebWouters/CheMPS2/pull/85.patch
Patch0:         CheMPS-1.8.9-cmake4.patch

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(flexiblas)
BuildRequires:  cmake
BuildRequires:  hdf5-devel
BuildRequires:  zlib-devel

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
# For directory ownership
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

%files
%doc README.md CHANGELOG.md FILES.md
%license LICENSE
%{_libdir}/libchemps2.so.*
%{_bindir}/chemps2
%{_mandir}/man1/chemps2.1.*

%files devel
%{_datadir}/cmake/CheMPS2/
%{_includedir}/chemps2/
%{_libdir}/libchemps2.so

%changelog
%autochangelog
