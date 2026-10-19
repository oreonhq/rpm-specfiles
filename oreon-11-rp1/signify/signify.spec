%global source2_hash 2cf9526061070ecaf1629130b57db96a05c0b27714f29000d6a2930b655b5a3f
%global source1_hash dfd18dab51a8994f587ff3c60fbe975f09db33f447db9cbd477f7077b372ab86
%global source0_hash 61635e45abcf1c78e28fbe3534a4224a2251c39295bb70bb211f699ef5f6eb27
Name:     signify
Version:  33
Release:        1%{?dist}
Summary:        Sign and verify signatures on files
License:  ISC AND Beerware AND BSD-3-Clause AND MIT AND LicenseRef-Fedora-Public-Domain
URL:      https://github.com/aperezdc/%{name}
Source0:        https://src.fedoraproject.org/repo/pkgs/signify/signify-33.tar.xz/sha512/e58cc314c19553cd8d02a64c50ece38f3159bba7fb4e58c2d736593a475995a6e5f1c7da45a649e17e88b76246cb307377689caa16b5b186b674be3e57d04a76/signify-33.tar.xz
Source1:  https://src.fedoraproject.org/repo/pkgs/signify/signify-33.tar.xz.asc/sha512/cbd39d36335917f6c450a60fd55952125ef32fb1a8ea7f66f2067c36a1f33a51f6a349ac4829c036f433feacca1b39f6aef7b1258d2f6d9fb7dcd2182dd0a17b/signify-33.tar.xz.asc
Source2:  https://keys.openpgp.org/vks/v1/by-fingerprint/5AA3BC334FD7E3369E7C77B291C559DBE4C9123B
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(libmd)
# /oreon:deps
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
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
