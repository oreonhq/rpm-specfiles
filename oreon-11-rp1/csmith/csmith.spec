%global source0_hash cb3edbeb73b3d3261aeea18c7df12f612fd3f46a2b3179c67dba1f8c669aa055
Name:    csmith
Version: 2.4.0
Release:        15%{?dist}
Summary:        Tool to generate random C programs for compiler testing
License: LicenseRef-Callaway-BSD AND GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:     http://embed.cs.utah.edu/csmith/
Source0:        https://github.com/csmith-project/%{name}/archive/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  perl-generators
# /oreon:deps
%description
Csmith is a tool that can generate random C programs that 
statically and dynamically conform to the C99 standard. It is 
useful for stress-testing compilers, static analyzers, and 
other tools that process C code

%package devel
Summary:        Header files and libraries for Csmith development
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
%description devel 
The %{name}-devel package contains the header files
and libraries for use with the Csmith package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{name}-%{version}
sed -i 's:/lib:/%{_lib}:' runtime/CMakeLists.txt

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build
%install
%cmake_install
find %{buildroot} -name *.a  -exec rm -f {} \;
rm -v %{buildroot}%{_bindir}/compiler_test.in
rm -v %{buildroot}%{_includedir}/{custom,stdint}_*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n csmith-devel -f %{oreon_filedir}/csmith-devel.list

%changelog

%autochangelog
