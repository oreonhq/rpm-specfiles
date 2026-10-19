%global source1_hash 559a7fa47f4762204c7fe5e070e6a425fc38b1f2b3111cd63f9b70d4137e1a49
%global source0_hash 2bd0f8aa344698c0ce6b2c89f5540af10e69e92d4c74f9fe66ffe25281be1111
%global githubproj CLD2Owners
%global githubrepo cld2
%global usesnapshot 1
%if 0%{?usesnapshot}
    %global commitdate0 20150821
    %global commit0 b56fa78a2fe44ac2851bae5bf4f4693a0644da7b
    %global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%endif
Name:           cld2
Version:        0
Release:        1%{?dist}
Summary:        A library to detect the natural language of text
License:        Apache-2.0
URL:            https://github.com/CLD2Owners/cld2/
Source0:        https://github.com/%{githubproj}/%{name}/archive/b56fa78a2fe44ac285%{usesnapshot}bae5bf4f4693a%{version}644da7b.tar.gz#/%{name}-b56fa78.tar.gz
Source1:        https://raw.githubusercontent.com/c72578/rpmbuild/master/SOURCES/CMakeLists.txt
ExcludeArch:    ppc64 s390x
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
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

export CXXFLAGS="%{optflags} -std=c++98 -Wl,--as-needed"
%cmake -DCMAKE_BUILD_TYPE=release -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir}
%cmake_build
%install
%cmake_install
%oreon_autofiles cld2-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

cd %{_vpath_builddir}
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
%files -f %{oreon_filedir}/main.list
%files -n cld2-devel -f %{oreon_filedir}/cld2-devel.list

%changelog

%autochangelog
