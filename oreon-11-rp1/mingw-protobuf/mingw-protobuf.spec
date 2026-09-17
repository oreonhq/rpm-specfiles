%global source0_hash 9a301cf94a8ddcb380b901e7aac852780b826595075577bb967004050c835056

%{?mingw_package_header}

%global pkgname protobuf

Name:          mingw-%{pkgname}
Version:       3.19.6
Release:       11%{?dist}
Summary:       MinGW Windows protobuf library

BuildArch:     noarch
License:       BSD-3-Clause
URL:           https://github.com/protocolbuffers/protobuf
Source0:       https://github.com/protocolbuffers/protobuf/archive/v%{version}/%{pkgname}-%{version}-all.tar.gz

BuildRequires: autoconf automake libtool
BuildRequires: gcc-c++
BuildRequires: make

BuildRequires: mingw32-filesystem >= 102
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem >= 102
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-zlib

%description
MinGW Windows protobuf library.

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows protobuf library
# Ensure packages stay in sync
Requires:      protobuf-compiler = %{version}

%description -n mingw32-%{pkgname}
MinGW Windows protobuf library.

%package -n mingw32-%{pkgname}-static
Summary:       Static version of the MinGW Windows protobuf library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-static
Static version of the MinGW Windows protobuf library.

%package -n mingw32-%{pkgname}-tools
Summary:       MinGW Windows protobuf library tools

%description -n mingw32-%{pkgname}-tools
MinGW Windows protobuf library tools.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows protobuf library
# Ensure packages stay in sync
Requires:      protobuf-compiler = %{version}

%description -n mingw64-%{pkgname}
MinGW Windows protobuf library.

%package -n mingw64-%{pkgname}-static
Summary:       Static version of the MinGW Windows protobuf library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-static
Static version of the MinGW Windows protobuf library.

%package -n mingw64-%{pkgname}-tools
Summary:       MinGW Windows protobuf library tools

%description -n mingw64-%{pkgname}-tools
MinGW Windows protobuf library tools.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}

%build
./autogen.sh
%mingw_configure
%mingw_make_build

%install
%mingw_make_install

# Delete *.la files
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files -n mingw32-%{pkgname}
%license LICENSE
%{mingw32_bindir}/libprotobuf-30.dll
%{mingw32_bindir}/libprotobuf-lite-30.dll
%{mingw32_bindir}/libprotoc-30.dll
%dir %{mingw32_includedir}/google
%{mingw32_includedir}/google/protobuf/
%{mingw32_libdir}/pkgconfig/protobuf-lite.pc
%{mingw32_libdir}/pkgconfig/protobuf.pc
%{mingw32_libdir}/libprotobuf-lite.dll.a
%{mingw32_libdir}/libprotobuf.dll.a
%{mingw32_libdir}/libprotoc.dll.a

%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/libprotobuf-lite.a
%{mingw32_libdir}/libprotobuf.a
%{mingw32_libdir}/libprotoc.a

%files -n mingw32-%{pkgname}-tools
%{mingw32_bindir}/i686-w64-mingw32-protoc.exe

%files -n mingw64-%{pkgname}
%license LICENSE
%{mingw64_bindir}/libprotobuf-30.dll
%{mingw64_bindir}/libprotobuf-lite-30.dll
%{mingw64_bindir}/libprotoc-30.dll
%dir %{mingw64_includedir}/google
%{mingw64_includedir}/google/protobuf/
%{mingw64_libdir}/pkgconfig/protobuf-lite.pc
%{mingw64_libdir}/pkgconfig/protobuf.pc
%{mingw64_libdir}/libprotobuf-lite.dll.a
%{mingw64_libdir}/libprotobuf.dll.a
%{mingw64_libdir}/libprotoc.dll.a

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/libprotobuf-lite.a
%{mingw64_libdir}/libprotobuf.a
%{mingw64_libdir}/libprotoc.a

%files -n mingw64-%{pkgname}-tools
%{mingw64_bindir}/x86_64-w64-mingw32-protoc.exe

%changelog
%autochangelog
