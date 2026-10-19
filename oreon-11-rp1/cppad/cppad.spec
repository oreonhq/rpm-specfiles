%global source0_hash 41ec617bb1e4163da381aaa5083a152e033631e9b5e135ccdc3466aaa1dc9001
%define year 2026
%define soversion %[ %year - 2019 ] 
%define __cmake_in_source_build 1
Name:    cppad
Version: %{year}0000.0
Release:        1%{?dist}
Summary:        C++ Algorithmic Differentiation (AD), cppad-devel and cppad-doc
License: EPL-2.0 OR GPL-2.0-or-later
URL:     https://github.com/coin-or/CppAD
Source0:        https://github.com/coin-or/CppAD/archive/%{version}/CppAD-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python-furo
BuildRequires:  python-pyspellchecker
BuildRequires:  python-sphinx-copybutton
BuildRequires:  python-sphinx_rtd_theme
BuildRequires:  python-tomli
BuildRequires:  python-xrst
# /oreon:deps
%description
C++ Algorithmic Differentiation (AD) include and library files.

# ---------------------------------------------------------------------------
%package devel
Summary: The %{name} C++ include files for Algorithmic Differentiation (AD)
Provides: %{name} = %{version}-%{release}
Provides: coin-or-cppad = %{version}-%{release}
Provides: coin-or-cppad-devel = %{version}-%{release}
%description devel
We refer to the step by step conversion from an algorithm that computes 
function values to an algorithm that computes derivative values as 
Algorithmic Differentiation (often referred to as Automatic Differentiation.) 
Given a C++ algorithm that computes function values, %{name} generates an 
algorithm that computes its derivative values. A brief introduction to 
Algorithmic Differentiation (AD) can be found at 
     http://en.wikipedia.org/wiki/Automatic_differentiation
The documentation for the %{year} version
     https://cppad.readthedocs.io/stable-%{year}
The documentation for the most recent version of %{name} can be found at
     https://cppad.readthedocs.io/latest
# -----------------------------------------------------------------------------
# prep
# -----------------------------------------------------------------------------
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#
# Create an empty directory named cppad-%%{version}, 
# changed into that directory and unpack Source.
%setup -q -c
#
# xrst.toml
# This is not a git repository so suppress the warning that could not double
# check that all the files with xrst commands were included.
echo ''                   >> CppAD-%{version}/xrst.toml
echo '[input_files]'      >> CppAD-%{version}/xrst.toml
echo 'data = [ ]'         >> CppAD-%{version}/xrst.toml
#
# COPYING, uw_copy_040507.html
cp CppAD-%{version}/COPYING  COPYING
cp CppAD-%{version}/uw_copy_040507.html uw_copy_040507.html
#
# cppad_lib/CMakeLists.txt
# cppad_lib: replace soversion number and ensure build type is release 
sed -i.bak CppAD-%{version}/cppad_lib/CMakeLists.txt \
    -e "s|print_variable(soversion)|SET(soversion %{soversion} )\n&|" \
    -e "s|\${cppad_debug_which}|debug_none|"
#
# Print machine epsilon before any other testing
cat << EOF > temp.cpp
# include <iostream>
# include <limits>
template <class Float> void print_epsilon(const char* type_name)
{   Float epsilon = std::numeric_limits<Float>::epsilon();
    std::cout << type_name << " epsilon = " << epsilon << "\n";
}
int main(void)
{   print_epsilon<float>("float");
    print_epsilon<double>("double");
    print_epsilon<long double>("long double");
    return 0;
}
EOF
g++ -std=c++11 temp.cpp -o temp
./temp > temp.out
cat temp.out
# ----------------------------------------------------------------------------
# build
# -----------------------------------------------------------------------------
%build

cppad_cxx_flags=\
'-Wall -pedantic-errors -std=c++11 -Wshadow -Wconversion  -Wno-array-bounds'
%cmake --version
%cmake \
    -S CppAD-%{version} \
    -B . \
    \
    -D CMAKE_VERBOSE_MAKEFILE=0 \
    -G 'Unix Makefiles' \
    \
    -D cppad_prefix=%{_prefix} \
    -D cppad_postfix='' \
    \
    -D cmake_install_includedirs=include \
    -D cmake_install_libdirs=%{_lib} \
    \
    -D cmake_install_datadir=share \
    -D cmake_install_docdir='NOTFOUND' \
    \
    -D include_doc=true \
    -D cmake_defined_ok=false \
    -D cppad_static_lib=false \
    -D cppad_debug_and_release=true \
    \
    -D include_adolc=false \
    -D include_ipopt=false \
    -D include_cppadcg=false \
    \
    -D colpack_prefix='NOTFOUND' \
    -D fadbad_prefix='NOTFOUND' \
    -D sacado_prefix='NOTFOUND' \
    \
    -D cppad_cxx_flags="$cppad_cxx_flags" \
    -D cppad_profile_flag='' \
    -D cppad_testvector=cppad \
    -D cppad_max_num_threads=64 \
    -D cppad_tape_id_type=size_t \
    -D cppad_tape_addr_type='unsigned int' \
    -D cppad_debug_which='debug_all'
%make_build
%install
%make_install
%oreon_autofiles cppad-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

g++ CppAD-%{version}/example/get_started/get_started.cpp \
   -I %{buildroot}/%{_includedir} \
   -Wl,-rpath,%{buildroot}/%{_libdir} \
   %{buildroot}/%{_libdir}/libcppad_lib.so \
   -o get_started
./get_started
make %{?_smp_mflags} doc_user
make %{?_smp_mflags} check
%%clean
%files -f %{oreon_filedir}/main.list
%files -n cppad-devel -f %{oreon_filedir}/cppad-devel.list

%changelog

%autochangelog
