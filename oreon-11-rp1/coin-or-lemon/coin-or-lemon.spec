%global source0_hash 71b7c725f4c0b4a8ccb92eb87b208701586cf7a96156ebd821ca3ed855bad3c8

Name:           coin-or-lemon
Version:        1.3.1
Release:        41%{?dist}
Summary:        A C++ template library providing many common graph algorithms

License:        BSL-1.0 AND BSD-3-Clause
URL:            http://lemon.cs.elte.hu/trac/lemon
VCS:            hg:http://lemon.cs.elte.hu/hg/lemon
Source:         http://lemon.cs.elte.hu/pub/sources/lemon-%{version}.tar.gz

# https://lemon.cs.elte.hu/trac/lemon/ticket/502
Patch:          lemon-%{version}-cmake-policy.patch

# https://lemon.cs.elte.hu/trac/lemon/ticket/503
Patch:          lemon-%{version}-buildfix.patch

# Work around FTBFS due to this gcc error: non-type template parameters of
# class type only available with '-std=c++2a' or '-std=gnu++2a'.
Patch:          lemon-%{version}-template.patch

# Fix a test failure due to using references to temporary objects that go
# out of scope.
Patch:          lemon-%{version}-test.patch

# Adapt to recent versions of SoPlex
Patch:          lemon-%{version}-soplex.patch

# Fix warnings that the register storage class is not permitted in C++17
Patch:          lemon-%{version}-register.patch

# Fix errors due to std::allocator changes in C++20
Patch:          lemon-%{version}-std-allocator.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

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
# The code is incompatible with C++20 and later
export CXXFLAGS='%{build_cxxflags} -std=gnu++17 -I%{_includedir}/soplex'

# CPLEX (aka ILOG) is non-free, so don't try to detect it.
#
# We suppress detection of ghostscript, doxygen, and python to make
# the build behave the same way with and without them installed -- we
# don't actually need them, since we don't need to rebuild the docs.
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

# Fix up the symlinks the way ldconfig wants them
%global majver %(cut -d. -f1 <<< %{version})
cd %{buildroot}%{_libdir}
rm libemon.so
ln -s libemon.so.%{version} libemon.so.%{majver}
ln -s libemon.so.%{majver} libemon.so
cd -

# Put the cmake file where Fedora cmake expects to find it
mv %{buildroot}%{_datadir}/lemon %{buildroot}%{_libdir}/cmake
mv %{buildroot}%{_libdir}/cmake/cmake %{buildroot}%{_libdir}/cmake/lemon

# Make man pages
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_mandir}/man1
for fil in dimacs-solver dimacs-to-lgf lgf-gen; do
  help2man -N --no-discard-stderr --version-string=%{version} \
    %{buildroot}%{_bindir}/$fil > %{buildroot}%{_mandir}/man1/$fil.1
done

# Install the documentation
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a AUTHORS NEWS README doc/html %{buildroot}%{_docdir}/%{name}

%check
%cmake_build --target check

%files
%license LICENSE
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/NEWS
%{_docdir}/%{name}/README
%{_libdir}/libemon.so.1{,.*}

%files devel
%{_includedir}/lemon/
%{_libdir}/libemon.so
%{_libdir}/cmake/lemon
%{_libdir}/pkgconfig/lemon.pc

%files tools
%{_bindir}/*
%{_mandir}/man1/*

%files doc
%{_docdir}/%{name}/html

%changelog
%autochangelog
