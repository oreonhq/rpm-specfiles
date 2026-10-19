%global source0_hash daf0b060fe701adf72aab0d525323d2e2e1bde9aa6aa9713ff1a5ef1e768d703
Name:		rply
Version:	1.1.4
Release:        1%{?dist}
Summary:        A library to read and write PLY files
License:	MIT
URL:		https://www.tecgraf.puc-rio.br/~diego/professional/rply/
Source0:        https://www.tecgraf.puc-rio.br/~diego/professional/rply/%{name}-%{version}.tar.gz
Source1:	rply_CMakeLists.txt
Source2:	RPLYConfig.cmake.in
Source3:	rply_cmake_export_cmakelists.txt
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
# /oreon:deps
%description
RPly is a library that lets applications read and write PLY files.
The PLY file format is widely used to store geometric information, such as 3D
models, but is general enough to be useful for other purposes.

RPly is easy to use, well documented, small, free, open-source, ANSI C,
efficient, and well tested. The highlights are:

* A callback mechanism that makes PLY file input straightforward;
* Support for the full range of numeric formats;
* Binary (big and little endian) and text modes are fully supported;
* Input and output are buffered for efficiency;
* Available under the MIT license for added freedom.

%package	devel
Summary:	Libraries and headers for rply
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
Rply Library Header Files and Link Libraries

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Add CMakeLists.txt file
cp %{SOURCE1} CMakeLists.txt

# Add CMake detection modules
mkdir -p CMake/export
mkdir -p CMake/Modules
cp %{SOURCE2} CMake/Modules/
cp %{SOURCE3} CMake/export/CMakeLists.txt

%build

%cmake -DCMAKE_BUILD_TYPE:STRING="Release" \
       -DCMAKE_VERBOSE_MAKEFILE=ON
%cmake_build
iconv -f iso8859-1 -t utf-8 LICENSE > LICENSE.conv && mv -f LICENSE.conv LICENSE
%install
%cmake_install
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/rplyConfig.cmake
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n rply-devel -f %{oreon_filedir}/rply-devel.list

%changelog

%autochangelog
