%global source0_hash ad4bcd8d87219a240a236d4a55c9decd2132a9436697d2882ead85c8939b0a99

Name:       opencc
Version:    1.1.9
Release:    7%{?dist}
Summary:    Libraries for Simplified-Traditional Chinese Conversion
License:    Apache-2.0
URL:        https://github.com/BYVoid/OpenCC
Source0:    https://github.com/BYVoid/OpenCC/archive/ver.%{version}.tar.gz#/OpenCC-ver.%{version}.tar.gz
Patch0:     opencc-fixes-compile.patch
Patch1:     opencc-fixes-crash.patch
Patch2:     opencc-fixes-cmake.patch
Patch3:     opencc-fixes-cmake-vars.patch
Patch4:     opencc-fixes-CVE.patch

BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  python3
BuildRequires:  marisa-devel
BuildRequires:  rapidjson-devel

%description
OpenCC is a library for converting characters and phrases between
Traditional Chinese and Simplified Chinese.

%package doc
Summary:    Documentation for OpenCC
Requires:   %{name} = %{version}-%{release}

%description doc
Doxygen generated documentation for OpenCC.

%package tools
Summary:    Command line tools for OpenCC
Requires:   %{name} = %{version}-%{release}

%description tools
Command line tools for OpenCC, including tools for conversion via CLI and
for building dictionaries.

%package devel
Summary:    Development files for OpenCC
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n OpenCC-ver.%{version} -p1

%build
%cmake -DENABLE_GETTEXT:BOOL=ON -DBUILD_DOCUMENTATION:BOOL=ON -DUSE_SYSTEM_MARISA:BOOL=ON -DUSE_SYSTEM_RAPIDJSON:BOOL=ON
%cmake_build

%install
%cmake_install

%check
%ctest

#%find_lang %{name}

%files
%doc AUTHORS LICENSE README.md
%{_libdir}/lib*.so.*
%{_datadir}/opencc/
%exclude %{_datadir}/opencc/doc

%files doc
%{_datadir}/opencc/doc

%files tools
%{_bindir}/*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/opencc/OpenCC*.cmake

%changelog
%autochangelog
