%global source0_hash 41ec617bb1e4163da381aaa5083a152e033631e9b5e135ccdc3466aaa1dc9001

# vim: set expandtab:
# ----------------------------------------------------------------------------
# Preamble
# ----------------------------------------------------------------------------
# fedpkg lint: W: no-documentation
# The %%doc directive below installs COPYING and uw_copy_040507.html
# as part of the main package, so this warning should not be generated; see
# https://fedoraproject.org/wiki/Common_Rpmlint_issues#no-documentation
# 'This would be rare as most packages should have some license text,
# a changelog or other information that is better placed in the main package
# instead of a -doc subpackage.'
#
# year 
# The year corresponding to this version
%define year 2026
#
# soversion
# fedora uses its own soversion number for cppad_lib where
# 1.0 corresponds to year 2020
%define soversion %[ %year - 2019 ] 
#
# This is really an out of soruce build because the source is in the
# CppAD-%%{version} sub-directory of the source. The fedora macros are 
# confused and need this defined true.
%define __cmake_in_source_build 1
# ----------------------------------------------------------------------------

# Fedora Release starts with 1; see
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Versioning/
Name:    cppad
Version: %{year}0000.0
Release: 3%{?dist}
Summary: C++ Algorithmic Differentiation (AD), %{name}-devel and %{name}-doc
#
License: EPL-2.0 OR GPL-2.0-or-later
URL:     https://github.com/coin-or/CppAD
Source:  %{url}/archive/%{version}/CppAD-%{version}.tar.gz
#
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake >= 3.10
BuildRequires: make
BuildRequires: python-xrst >= 2025.0
BuildRequires: python-sphinx_rtd_theme
BuildRequires: python-tomli
BuildRequires: python-sphinx-copybutton
BuildRequires: python-pyspellchecker
BuildRequires: python-furo

%description
C++ Algorithmic Differentiation (AD) include and library files.

# ---------------------------------------------------------------------------
%package devel
Summary: The %{name} C++ include files for Algorithmic Differentiation (AD)
Provides: %{name} = %{version}-%{release}
# Requested by bug report
#     https://bugzilla.redhat.com/show_bug.cgi?id=1197488
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
#
# 1. The debug_all is overridden for cppad_lib by the edit of
# cppad_lib/CMakeLists.txt above
#
# 2. The gnu c++ compiler seems to be generating an incorrect warning about
# array bounds in thread_alloc.hpp. Use -Wno-array-bounds to suppress it.
#
# cppad_cxx_flags
# extra C++ compiler flags
cppad_cxx_flags=\
'-Wall -pedantic-errors -std=c++11 -Wshadow -Wconversion  -Wno-array-bounds'
#
# CMake Warning:
# Manually-specified variables were not used by the project:
#    CMAKE_C_FLAGS_RELEASE
#    CMAKE_Fortran_FLAGS_RELEASE
#    CMAKE_INSTALL_DO_STRIP
#    INCLUDE_INSTALL_DIR
#    LIB_INSTALL_DIR
#    LIB_SUFFIX
#    SHARE_INSTALL_PREFIX
#    SYSCONF_INSTALL_DIR
#
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
#
# see https://docs.fedoraproject.org/en-US/packaging-guidelines/
#   parallel_make
%make_build

# -----------------------------------------------------------------------------
# Install
# -----------------------------------------------------------------------------
%install
# https://docs.fedoraproject.org/en-US/packaging-guidelines/
#   why_the_makeinstall_macro_should_not_be_used
%make_install

%files
%{_libdir}/libcppad_lib.so.%{soversion}

# These documentation files come from the source code tarball
%doc COPYING uw_copy_040507.html

%files devel
%{_includedir}/%{name}
%{_datadir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/libcppad_lib.so

# -----------------------------------------------------------------------------
# Check
# -----------------------------------------------------------------------------
# 
%check
#
# Test installed version of CppAD
g++ CppAD-%{version}/example/get_started/get_started.cpp \
   -I %{buildroot}/%{_includedir} \
   -Wl,-rpath,%{buildroot}/%{_libdir} \
   %{buildroot}/%{_libdir}/libcppad_lib.so \
   -o get_started
./get_started
#
# Test building documentation
make %{?_smp_mflags} doc_user
#
# Run the all the standard CppAD tests.
make %{?_smp_mflags} check
# ----------------------------------------------------------------------------
#
# Use %%clean with no arguments to surpress the cleanup of BUILDROOT 
# This enables one to check that the necessary files are installed.
%%clean
# ----------------------------------------------------------------------------
%changelog
%autochangelog
