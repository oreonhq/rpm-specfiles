%global source0_hash 9a301cf94a8ddcb380b901e7aac852780b826595075577bb967004050c835056
%{?mingw_package_header}
%global pkgname protobuf
Name:          mingw-%{pkgname}
Version:       3.19.6
Release:        1%{?dist}
Summary:        MinGW Windows protobuf library
BuildArch:     noarch
License:       BSD-3-Clause
URL:           https://github.com/protocolbuffers/protobuf
Source0:        https://github.com/protocolbuffers/%{pkgname}/archive/v%{version}/%{pkgname}-%{version}-all.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-zlib
# /oreon:deps
%description
MinGW Windows protobuf library.

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows protobuf library
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
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-protobuf -f %{oreon_filedir}/mingw32-protobuf.list
%files -n mingw32-protobuf-static -f %{oreon_filedir}/mingw32-protobuf-static.list
%files -n mingw32-protobuf-tools -f %{oreon_filedir}/mingw32-protobuf-tools.list
%files -n mingw64-protobuf -f %{oreon_filedir}/mingw64-protobuf.list
%files -n mingw64-protobuf-static -f %{oreon_filedir}/mingw64-protobuf-static.list
%files -n mingw64-protobuf-tools -f %{oreon_filedir}/mingw64-protobuf-tools.list

%changelog

%autochangelog
