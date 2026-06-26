%global source0_hash ac15ffb8430502fbaccdec66c5a82ee0eab0b0f36220df56710feadfeb13d0a0

Name:           libmd
Version:        1.2.0
Release:        1%{?dist}
Summary:        Library that provides message digest functions from BSD systems
License:        BSD-2-Clause AND BSD-3-Clause AND ISC AND Beerware AND LicenseRef-Fedora-Public-Domain
URL:            https://www.hadrons.org/software/libmd/
Source0:        https://libbsd.freedesktop.org/releases/%{name}-%{version}.tar.xz
Source1:        https://libbsd.freedesktop.org/releases/%{name}-%{version}.tar.xz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/4F3E74F436050C10F5696574B972BF3EA4AE57A3

BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  make

%description
The libmd library provides a few message digest ("hash") functions, as
found on various BSD systems, either on their libc or on a library with
the same name, and with a compatible API.

%package devel
Summary:        Development files for the message digest library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description devel
The libmd-devel package includes header files and libraries necessary
for developing programs which use the message digest library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%build
%configure --disable-static
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.la

%check
make check

%ldconfig_scriptlets

%files
%license COPYING
%doc ChangeLog README
%{_libdir}/%{name}.so.0*
%{_mandir}/man7/%{name}.7*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/md2.h
%{_includedir}/md4.h
%{_includedir}/md5.h
%{_includedir}/ripemd.h
%{_includedir}/rmd160.h
%{_includedir}/sha.h
%{_includedir}/sha1.h
%{_includedir}/sha2.h
%{_includedir}/sha256.h
%{_includedir}/sha512.h
%{_includedir}/sha3.h
%{_mandir}/man3/MD2*.3*
%{_mandir}/man3/MD4*.3*
%{_mandir}/man3/MD5*.3*
%{_mandir}/man3/RMD160*.3*
%{_mandir}/man3/SHA1*.3*
%{_mandir}/man3/SHA224*.3*
%{_mandir}/man3/SHA256*.3*
%{_mandir}/man3/SHA384*.3*
%{_mandir}/man3/SHA512*.3*
%{_mandir}/man3/SHA3_*.3*
%{_mandir}/man3/SHAKE128*.3*
%{_mandir}/man3/SHAKE256*.3*
%{_mandir}/man3/md2.3*
%{_mandir}/man3/md4.3*
%{_mandir}/man3/md5.3*
%{_mandir}/man3/ripemd.3*
%{_mandir}/man3/rmd160.3*
%{_mandir}/man3/sha1.3*
%{_mandir}/man3/sha224.3*
%{_mandir}/man3/sha256.3*
%{_mandir}/man3/sha384.3*
%{_mandir}/man3/sha512.3*
%{_mandir}/man3/sha3_*.3*
%{_mandir}/man3/shake128.3*
%{_mandir}/man3/shake256.3*

%changelog
%autochangelog
