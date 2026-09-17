%global source0_hash 54e0f234ace310a4256dc7d4fc707837f532a509cc3ef2940dacbdc4ebd9ce15

Name:           osmpbf
Version:        1.6.1
Release:        %autorelease
Summary:        C library to read and write OpenStreetMap PBF files

License:        LGPL-3.0-or-later
URL:            https://github.com/openstreetmap/OSM-binary
Source0:        https://github.com/openstreetmap/OSM-binary/archive/v%{version}/OSM-binary-%{version}.tar.gz

BuildRequires:  cmake make gcc-c++
BuildRequires:  protobuf-devel protobuf-compiler
BuildRequires:  zlib-devel zlib-static

%description
Osmpbf is a Java/C library to read and write OpenStreetMap PBF files.
PBF (Protocol buffer Binary Format) is a binary file format for OpenStreetMap
data that uses Google Protocol Buffers as low-level storage.

%package tools
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
This package contains tools that use %{name}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n OSM-binary-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install
rm %{buildroot}/%{_libdir}/libosmpbf.a

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_libdir}/libosmpbf.so.1
%{_libdir}/libosmpbf.so.1.*

%files tools
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%{_includedir}/osmpbf
%{_libdir}/libosmpbf.so

%changelog
%autochangelog
