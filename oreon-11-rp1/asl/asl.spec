%global source0_hash 6e016ffd521099de87c4a7aaa8a6582332f8f6512c7c9e886dcf7b094e3fea88
%global commit     3d477ba78a3392b8b7b05a2fd843ae7f9df70252
Name:           asl
Version:        20251122
Release:        1%{?dist}
Summary:        AMPL Solver Library
License:        BSD-3-Clause AND SMLNJ AND dtoa
URL:            https://github.com/ampl/asl
VCS:            git:%{url}.git
Source0:        https://github.com/ampl/%{name}/archive/%{commit}/%{name}-%{version}.tar.gz
Patch:          %{name}-shared.patch
Patch:          %{name}-arch-flags.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
# /oreon:deps
%description
The AMPL Solver Library is an interface used to access a variety of solvers
from AMPL code.

%package        devel
Summary:        Header files and library links for asl
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Header files and library links for building projects that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit}

%conf
# Fix install location of ampl-asl-config
sed -i 's,share/,lib/cmake/,' CMakeLists.txt

# Fix install location on 64-bit platforms
if [ "%{_lib}" != "lib" ]; then
  sed -i '/DESTINATION/s/lib/%{_lib}/g' CMakeLists.txt
fi

export CFLAGS="%{build_cflags} -DIGNORE_BOGUS_WARNINGS"
export CXXFLAGS="%{build_cxxflags} -DIGNORE_BOGUS_WARNINGS"
%cmake \
  -DBUILD_CPP:BOOL=ON \
  -DBUILD_EXAMPLES:BOOL=OFF \
  -DBUILD_MT_LIBS:BOOL=ON \
  -DBUILD_SHARED_LIBS:BOOL=ON \
  -DGENERATE_ARITH:BOOL=ON

%build

%cmake_build
%install
%cmake_install
cp -p src/solvers/{dvalue.hd,fg_read.c} %{buildroot}%{_includedir}/asl
cp -p src/solvers2/fg_read.c %{buildroot}%{_includedir}/asl2
%fdupes %{buildroot}%{_includedir}
%oreon_autofiles asl-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n asl-devel -f %{oreon_filedir}/asl-devel.list

%changelog

%autochangelog
