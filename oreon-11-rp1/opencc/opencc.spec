%global source0_hash 8e5f5cf7fe195bd9b9be851adc9738c1ef7dc5c24441dd5878a56db4087a9a70
Name:       opencc
Version:    1.4.2
Release:        1%{?dist}
Summary:        Libraries for Simplified-Traditional Chinese Conversion
License:    Apache-2.0
URL:        https://github.com/BYVoid/OpenCC
Source0:        https://github.com/BYVoid/OpenCC/archive/ver.%{version}.tar.gz#/OpenCC-ver.%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  marisa-devel
BuildRequires:  python3
BuildRequires:  rapidjson-devel
# /oreon:deps
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
%global oreon_srcdir OpenCC-ver.%{version}
%oreon_prep
%build

%cmake -DENABLE_GETTEXT:BOOL=ON -DBUILD_DOCUMENTATION:BOOL=ON -DUSE_SYSTEM_MARISA:BOOL=ON -DUSE_SYSTEM_RAPIDJSON:BOOL=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n opencc-doc -f %{oreon_filedir}/opencc-doc.list
%files -n opencc-tools -f %{oreon_filedir}/opencc-tools.list
%files -n opencc-devel -f %{oreon_filedir}/opencc-devel.list

%changelog

%autochangelog
