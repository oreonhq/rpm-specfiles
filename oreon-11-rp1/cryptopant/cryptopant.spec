%global source1_hash edaef632cbb643e4e7a221717a6c441a4c1a7c918e6e4d56debc3d8739b233f6
%global source0_hash 049b98da835a356230259e68684165fbfa08bf6540424a6f4d815660ae55f278
%global sover   1
%global libname libcryptopant%{sover}
%global upname cryptopANT
Version:        1.3.2
Name:           cryptopant
Release:        1%{?dist}
Summary:        IP address anonymization library shared library
License:        GPL-2.0-only
URL:            http://ant.isi.edu/software/cryptopANT
Source0:        http://ant.isi.edu/software/%{upname}/%{upname}-%{version}.tar.gz
Source1:        https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt#/LICENSE
Provides:       %{libname}%{?_isa} = %{version}-%{release}
Provides:       %{upname}%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
# /oreon:deps
%description
cryptopANT is a library for IP address anonymization. It implements
a widely used prefix-preserving technique known as "cryptopan".
This is ANT's project implementation of this technique for
anonymization of ipv4 and ipv6 addresses.

%package devel
Summary:        IP address anonymization library development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       openssl-devel
Provides:       %{upname}-devel%{?_isa} = %{version}-%{release}
%description devel
cryptopANT is a library for IP address anonymization. It implements
a widely used prefix-preserving technique known as "cryptopan".
This is ANT's project implementation of this technique for
anonymization of ipv4 and ipv6 addresses.

%package utils
Summary:        IP address anonymization library development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description utils
cryptopANT is a library for IP address anonymization. It implements
a widely used prefix-preserving technique known as "cryptopan".
This is ANT's project implementation of this technique for
anonymization of ipv4 and ipv6 addresses.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{upname}-%{version}
[ -f LICENSE ] || install -p -m 0644 %{SOURCE1} LICENSE # < TODO: remove this

%build

autoreconf -fsi
%configure --with-scramble_ips
%make_build
%install
%make_install
rm -f %{buildroot}%{_libdir}/lib%{upname}.{a,la}
%oreon_autofiles cryptopant-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cryptopant-utils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%make_build test
%files -f %{oreon_filedir}/main.list
%files -n cryptopant-devel -f %{oreon_filedir}/cryptopant-devel.list
%files -n cryptopant-utils -f %{oreon_filedir}/cryptopant-utils.list

%changelog

%autochangelog
