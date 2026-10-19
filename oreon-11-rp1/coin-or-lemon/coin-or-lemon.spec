%global source0_hash 71b7c725f4c0b4a8ccb92eb87b208701586cf7a96156ebd821ca3ed855bad3c8
Name:           coin-or-lemon
Version:        1.3.1
Release:        1%{?dist}
Summary:        A C++ template library providing many common graph algorithms
License:        BSL-1.0 AND BSD-3-Clause
URL:            http://lemon.cs.elte.hu/trac/lemon
VCS:            hg:http://lemon.cs.elte.hu/hg/lemon
Source0:        http://lemon.cs.elte.hu/pub/sources/lemon-%{version}.tar.gz
Patch:          lemon-%{version}-cmake-policy.patch
Patch:          lemon-%{version}-buildfix.patch
Patch:          lemon-%{version}-template.patch
Patch:          lemon-%{version}-test.patch
Patch:          lemon-%{version}-soplex.patch
Patch:          lemon-%{version}-register.patch
Patch:          lemon-%{version}-std-allocator.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  cmake
BuildRequires:  coin-or-Cbc-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glpk-devel
BuildRequires:  help2man
BuildRequires:  libsoplex-devel
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
LEMON stands for Library for Efficient Modeling and Optimization in Networks.
It is a C++ template library providing efficient implementations of common
data structures and algorithms with focus on combinatorial optimization tasks
connected mainly with graphs and networks.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tools
Summary:        Command-line tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    tools
The %{name}-tools package contains a handful of command-line tools that
come with %{name}.

%package        doc
Summary:        Documentation for for %{name}
BuildArch:      noarch
%description    doc
The %{name}-doc package contains %{name}'s API documentation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n lemon-%{version} -p1

%conf
# Fix the library directory name on 64-bit systems
if [ "%{_lib}" = "lib64" ]; then
    sed -i 's,/lib,/lib64,' cmake/FindCOIN.cmake cmake/FindGLPK.cmake \
        cmake/LEMONConfig.cmake.in lemon/lemon.pc.in
    sed -i 's,DESTINATION lib,&64,' lemon/CMakeLists.txt
fi

# We ship a shared library, not a static library
sed -i 's/libemon\.a/libemon.so/' cmake/LEMONConfig.cmake.in

%build

export CXXFLAGS='%{build_cxxflags} -std=gnu++17 -I%{_includedir}/soplex'
%cmake \
  -DDOXYGEN_EXECUTABLE= \
  -DGHOSTSCRIPT_EXECUTABLE= \
  -DPYTHON_EXECUTABLE= \
  -DLEMON_ENABLE_COIN:BOOL=YES \
  -DLEMON_ENABLE_GLPK:BOOL=YES \
  -DLEMON_ENABLE_ILOG:BOOL=NO \
  -DLEMON_ENABLE_SOPLEX:BOOL=YES
%cmake_build
%install
%cmake_install
%global majver %(cut -d. -f1 <<< %{version})
cd %{buildroot}%{_libdir}
rm libemon.so
ln -s libemon.so.%{version} libemon.so.%{majver}
ln -s libemon.so.%{majver} libemon.so
cd -
mv %{buildroot}%{_datadir}/lemon %{buildroot}%{_libdir}/cmake
mv %{buildroot}%{_libdir}/cmake/cmake %{buildroot}%{_libdir}/cmake/lemon
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_mandir}/man1
for fil in dimacs-solver dimacs-to-lgf lgf-gen; do
  help2man -N --no-discard-stderr --version-string=%{version} \
    %{buildroot}%{_bindir}/$fil > %{buildroot}%{_mandir}/man1/$fil.1
done
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a AUTHORS NEWS README doc/html %{buildroot}%{_docdir}/%{name}
%oreon_autofiles coin-or-lemon-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles coin-or-lemon-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles coin-or-lemon-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%cmake_build --target check
%files -f %{oreon_filedir}/main.list
%files -n coin-or-lemon-devel -f %{oreon_filedir}/coin-or-lemon-devel.list
%files -n coin-or-lemon-tools -f %{oreon_filedir}/coin-or-lemon-tools.list
%files -n coin-or-lemon-doc -f %{oreon_filedir}/coin-or-lemon-doc.list

%changelog

%autochangelog
