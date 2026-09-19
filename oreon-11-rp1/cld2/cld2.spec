%global source0_hash none

%global githubproj CLD2Owners
%global githubrepo cld2

#For git snapshots, set to 0 to use release instead:
%global usesnapshot 1
%if 0%{?usesnapshot}
    %global commitdate0 20150821
    %global commit0 b56fa78a2fe44ac2851bae5bf4f4693a0644da7b
    %global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%endif

Name:           cld2
# When upstream has never chosen a version, you MUST use Version: 0.
Version:        0
Release:        0.33%{?usesnapshot:.%{commitdate0}git%{shortcommit0}}%{?dist}
Summary:        A library to detect the natural language of text
# Automatically converted from old format: ASL 2.0
License:        Apache-2.0
URL:            https://github.com/CLD2Owners/cld2/
Source0:        https://github.com/%{githubproj}/%{githubrepo}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
# CMakeLists.txt originally from https://code.google.com/p/cld2/issues/detail?id=29
# Updated version 0.0.197 from Debian at https://sources.debian.net/src/cld2/0.0.0-git20150806-5/CMakeLists.txt/
# There is no CMakeLists.txt yet at https://github.com/CLD2Owners/cld2/
# Stored CMakeLists.txt 0.0.198 at own github repo for now
Source1:        https://raw.githubusercontent.com/c72578/rpmbuild/master/SOURCES/CMakeLists.txt

# Tests fail on ppc64 and s390x
# Bug reports against associated ExcludeArch blocker bugs:
# https://bugzilla.redhat.com/show_bug.cgi?id=1484320
# https://bugzilla.redhat.com/show_bug.cgi?id=1484319
ExcludeArch:    ppc64 s390x

BuildRequires:  cmake >= 2.8
BuildRequires:  gcc-c++

%description
A library that detects over 80 languages in UTF-8 text, based largely
on groups of four letters. Also tables for 160+ language versions.

%package devel
Summary:        Development files for cld2
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
A library that detects over 80 languages in UTF-8 text, based largely
on groups of four letters. Also tables for 160+ language versions.

This sub-package contains the headers for cld2.

%prep
%if 0%{?usesnapshot}
    %autosetup -n %{name}-%{commit0}
%else
    %autosetup
%endif
cp %{SOURCE1} .

%build
# https://fedoraproject.org/wiki/Common_Rpmlint_issues#unused-direct-shlib-dependency
# Add Wl,--as-needed to CXX_FLAGS
# Fix build with gcc-6, build with -std=c++98. See Github, CLD2 issue #47
# https://github.com/CLD2Owners/cld2/issues/47
export CXXFLAGS="%{optflags} -std=c++98 -Wl,--as-needed"
%cmake -DCMAKE_BUILD_TYPE=release -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir}
%cmake_build

%install
%cmake_install

%check
cd %{_vpath_builddir}
# Tests from: internal/compile_and_test_all.sh
echo "this is some english text" | ./compact_lang_det_test_chrome_2
echo "this is some english text" | ./compact_lang_det_test_chrome_16
./cld2_unittest_chrome_2 > /dev/null
./cld2_unittest_avoid_chrome_2 > /dev/null
echo "this is some english text" | ./compact_lang_det_test_full
./cld2_unittest_full > /dev/null
./cld2_unittest_full_avoid > /dev/null
./cld2_dynamic_data_tool --dump cld2_data.bin
./cld2_dynamic_data_tool --verify cld2_data.bin
echo "this is some english text" | ./compact_lang_det_dynamic_test_chrome --data-file cld2_data.bin
./cld2_dynamic_unittest --data-file cld2_data.bin > /dev/null

%ldconfig_scriptlets

%files
%doc README.md
%license LICENSE
%{_libdir}/libcld2.so.*
%{_libdir}/libcld2_dynamic.so.*
%{_libdir}/libcld2_full.so.*

%files devel
%doc docs/*
%{_includedir}/%{name}
%{_libdir}/libcld2.so
%{_libdir}/libcld2_dynamic.so
%{_libdir}/libcld2_full.so

%changelog
%autochangelog
