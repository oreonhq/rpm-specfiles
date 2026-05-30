%global source0_hash 8c2b6fb279b5b42e9ac92ade71832e485852647b53607c43baaafbbcecea04e4

Name:           libfido2

Version:        1.16.0
Release:        5%{?dist}
Summary:        FIDO2 library

License:        BSD-2-Clause
URL:            https://github.com/Yubico/%{name}
Source0:        https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.gz
Source1:        https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.gz.sig
#
# Yubico does not provide a central gpg keyring download file. Instead, they
# provide a list of individuals that release code and their fingerprints at
#   https://developers.yubico.com/Software_Projects/Software_Signing.html
# One must import all the keys and then export into the keyfile.
#   gpg2 --homedir /tmp/ --receive-keys "keyid0"
#   gpg2 --homedir /tmp/ --receive-keys "keyid1"
#   gpg2 --homedir /tmp/ --export --armor --output yubico-release-gpgkeys.asc
#
Source2:        yubico-release-gpgkeys.asc

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libcbor)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
%{name} is an open source library to support the FIDO2 protocol.  FIDO2 is
an open authentication standard that consists of the W3C Web Authentication
specification (WebAuthn API), and the Client to Authentication Protocol
(CTAP).  CTAP is an application layer protocol used for communication
between a client (browser) or a platform (operating system) with an external
authentication device (for example the Yubico Security Key).

################################################################################

%package devel

Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{name}-devel contains development libraries and header files for %{name}.

################################################################################

%package -n fido2-tools

Summary:        FIDO2 tools
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n fido2-tools
FIDO2 command line tools to access and configure a FIDO2 compliant
authentication device.

################################################################################


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n %{name}-%{version}


%build
%cmake
%cmake_build


%install
%cmake_install
# Remove static files per packaging guidelines
find %{buildroot} -type f -name "*.a" -delete -print


%check
%ctest \-E regress_cred


%files
%doc NEWS README.adoc
%license LICENSE
%{_libdir}/libfido2.so.1{,.*}

%files devel
%{_libdir}/pkgconfig/libfido2.pc
%{_libdir}/libfido2.so
%{_includedir}/fido.h
%{_includedir}/fido
%{_mandir}/man3/fido_*.3{,.*}
%{_mandir}/man3/eddsa_pk_*.3{,.*}
%{_mandir}/man3/es256_pk_*.3{,.*}
%{_mandir}/man3/es384_pk_*.3{,.*}
%{_mandir}/man3/rs256_pk_*.3{,.*}

%files -n fido2-tools
%{_bindir}/fido2-assert
%{_bindir}/fido2-cred
%{_bindir}/fido2-token
%{_mandir}/man1/fido2-assert.1{,.*}
%{_mandir}/man1/fido2-cred.1{,.*}
%{_mandir}/man1/fido2-token.1{,.*}


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.16.0-5
- Prepare for Oreon 11 (RP1)
