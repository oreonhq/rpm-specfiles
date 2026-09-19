%global source0_hash 6e9baac8689dfd2e1502ceafabb20c62b6cd572744d240fb755503fd57c2a6af

Name:           laszip
Version:        3.5.0
Release:        3%{?dist}
Summary:        Quickly turns bulky LAS files into compact LAZ files
License:        Apache-2.0
Source0:        https://github.com/LASzip/LASzip/archive/%{version}/%{name}-%{version}.tar.gz
URL:            http://www.laszip.org/

# Restore old API for libLAS
# https://github.com/libLAS/libLAS/issues/144
Patch0:         laszip_restoreapi.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
LASzip - a free product of rapidlasso GmbH - quickly turns bulky LAS files into
compact LAZ files without information loss.

%package devel
Summary:        The development files for laszip
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and libraries for laszip

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n LASzip-%{version}

%build
%cmake -DLASZIP_LIB_INSTALL_DIR=%{_libdir} -DCMAKE_SKIP_RPATH=TRUE
%cmake_build

%install
%cmake_install

# Manually install header referenced in laszip.hpp
cp -a src/{mydefs.hpp,lasmessage.hpp} %{buildroot}%{_includedir}/laszip/

%files
%doc AUTHORS.txt CHANGES.txt NEWS.txt
%license COPYING.txt
%{_libdir}/liblaszip.so.8*
%{_libdir}/liblaszip_api.so.8*

%files devel
%{_includedir}/laszip/
%{_libdir}/liblaszip.so
%{_libdir}/liblaszip_api.so

%changelog
%autochangelog
