%global source0_hash 89e0f12df2ddc1d9ee9c992a7c595d63c673943c7d970b573072eae33bca9314

# NOTE: upstream does not make releases and has no version numbering scheme.
# We check the code out of git and use the date of the last commit as the
# version number.
%global gittag   5a127dbbcf9a0f822768e783dbf892ee90c435d5
%global shorttag %(cut -b -7 <<< %{gittag})

Name:           lfsc
Version:        0.20230914
Release:        5%{?dist}
Summary:        SMT proof checker

License:        BSD-3-Clause
URL:            https://github.com/cvc5/LFSC
VCS:            git:%{url}.git
Source0:        %{url}/archive/%{gittag}/%{name}-%{shorttag}.tar.gz
# The next few sources contain commonly used proof definitions
Source1:        http://clc.cs.uiowa.edu/lfsc/euf_interpolation.plf
Source2:        http://clc.cs.uiowa.edu/lfsc/sat.plf
Source3:        http://clc.cs.uiowa.edu/lfsc/smt.plf
Source4:        http://clc.cs.uiowa.edu/lfsc/th_base.plf
Source5:        http://clc.cs.uiowa.edu/lfsc/th_real.plf
Source6:        http://clc.cs.uiowa.edu/lfsc/th_lra.plf
Source7:        http://clc.cs.uiowa.edu/lfsc/th_lra-cvc3.plf
Source8:        http://clc.cs.uiowa.edu/lfsc/color_base.plf
Source9:        http://clc.cs.uiowa.edu/lfsc/color_euf.plf
# Use std::unordered_map instead of the deprecated __gnu_cxx::hash_map
Patch:          %{name}-map.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  python3-devel

%description
This package contains an SMT proof checker.

%package devel
Summary:        Files needed to compile side conditions
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the files needed to compile a version of %{name} that
can execute a side condition.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n LFSC-%{gittag}

%conf
# We want to know about use of deprecated interfaces
sed -i '/Wno-deprecated/d' CMakeLists.txt

# Build a shared library instead of a static library, and give it an soname
sed -e 's/STATIC/SHARED/' \
    -e '/^[[:blank:]]*OUTPUT_NAME lfscc/i\  VERSION 0.0.0\n  SOVERSION 0' \
    -e 's/ARCHIVE DESTINATION/LIBRARY DESTINATION/' \
    -e '/^set_target_properties/iTARGET_LINK_LIBRARIES(liblfscc gmp)' \
    -i src/CMakeLists.txt

# Fix the library install path
if [ "%{_lib}" = "lib64" ]; then
  sed -i 's,/lib,/lib64,' src/CMakeLists.txt
fi

# Fix the test script
%py3_shebang_fix tests/run_test.py

%build
%cmake
%cmake_build

%install
%cmake_install

# Install the proof files
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} \
   %{SOURCE7} %{SOURCE8} %{SOURCE9} %{buildroot}%{_datadir}/%{name}

# Generate a man page
cd %{_vpath_builddir}/src
mkdir -p %{buildroot}%{_mandir}/man1
export LD_LIBRARY_PATH=$PWD
help2man -N --version-string=%{version} -n 'SMT proof checker' ./lfscc > \
  %{buildroot}%{_mandir}/man1/lfscc.1
# Fix line breaks in the man page
sed -i 's/\\fB/.TP\n&/;s/\\fR: /\\fR\n/' %{buildroot}%{_mandir}/man1/lfscc.1

# Help the debuginfo generator
cp -p ../../src/lexer.flex .
cd -

%check
%ctest

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/lfscc
%{_datadir}/%{name}/
%{_libdir}/liblfscc.so.0{,.*}
%{_mandir}/man1/lfscc.1*

%files devel
%{_includedir}/lfscc.h
%{_libdir}/liblfscc.so

%changelog
%autochangelog
