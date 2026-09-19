%global source0_hash 0b6d09c741dcd1c100cdcdd8b5f5bf85cfe54bdd7bea1f96916c2471280ddf03

Name:		libaesgm
Version:	20090429
Release:	37%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
Summary:	Library implementation of AES (Rijndael) cryptographic methods
URL:		http://gladman.plushost.co.uk/oldsite/AES/index.php
Source0:	http://gladman.plushost.co.uk/oldsite/AES/aes-src-29-04-09.zip
Source1:	Makefile.aes
# Add fileencryption support
# http://www.gladman.me.uk/cryptography_technology/fileencrypt/
Patch0:		libaesgm-20090429-fileencrypt.patch
# Sync to latest code
# https://github.com/BrianGladman/AES
Patch1:		libaesgm-20090429-git8798ad829374cd5ff312f55ba3ccccfcf586fa11.patch

BuildRequires: gcc
BuildRequires: make

%description
Library implementation of AES (Rijndael) cryptographic methods.

%package devel
Summary:	Development files for libaesgm
Requires:	%{name} = %{version}-%{release}

%description devel
Development headers and libraries for libaesgm.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -n %{name}-%{version}
cp %{SOURCE1} Makefile
%patch -P0 -p1 -b .fileencrypt
%patch -P1 -p1 -b .git8798ad82
sed -i 's/\r//' *.txt

%build
make CFLAGS="%{optflags} -fPIC -DUSE_SHA1" LDFLAGS="%{build_ldflags}"

%install
make DESTDIR="%{buildroot}" LIBDIR="%{_libdir}" install

%ldconfig_scriptlets

%files
%doc *.txt
%{_libdir}/libaesgm.so.*

%files devel
%{_includedir}/aes/
%{_libdir}/libaesgm.so

%changelog
%autochangelog
