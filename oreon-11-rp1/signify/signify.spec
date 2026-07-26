%global source0_hash 6dd1b97fd9273d268b70c1be3c2592cbbe1488bca5e45c12c58f8c74362758d5

Name:     signify
Version:  32
Release:  5%{?dist}
Summary:  Sign and verify signatures on files

# signify itself is ISC but uses other source codes, breakdown:
# Beerware: helper.c
# BSD-3-Clause: blf.h and blowfish.c and sha2.[ch]
# MIT: explicit_bzero.h
# LicenseRef-Fedora-Public-Domain: crypto_api.[ch] and explicit_bzero.c and
#                                  {fe,sc}25519.[ch] ge25519{.h,_base.data}
#                                  and mod_{ed,ge}25519.c
License:  ISC AND Beerware AND BSD-3-Clause AND MIT AND LicenseRef-Fedora-Public-Domain
URL:      https://github.com/aperezdc/%{name}
Source0:  %url/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:  %url/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:  https://keys.openpgp.org/vks/v1/by-fingerprint/5AA3BC334FD7E3369E7C77B291C559DBE4C9123B

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(libmd)

%description
The signify utility creates and verifies cryptographic signatures, as used
by the OpenBSD release maintainers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
# Remove upstream bundled optional libraries from source
rm -rf libbsd libwaive

%build
%set_build_flags
%make_build

%install
%make_install PREFIX=%{_prefix}

%check
make check

%files
%license COPYING
%doc CHANGELOG.md README.md
%{_bindir}/signify
%{_mandir}/man1/signify.*

%changelog
%autochangelog
