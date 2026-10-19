%global source1_hash 557b3fa99ddbd0e8d75e270c90d4e3bef568ae6265f9f2f2168a77c0a470336e
%global source0_hash a245fd13271a8d2afa03dde979af3a29eb3d4ebb1fbcad4a9b52cf67a27d05f7
Name:           paperkey
Version:        1.6
Release:        1%{?dist}
Summary:        An OpenPGP key archiver
License:        GPL-2.0-or-later
URL:            https://www.jabberwocky.com/software/paperkey/
Source0:        https://www.jabberwocky.com/software/%{name}/%{name}-%{version}.tar.gz
Source1:        https://www.jabberwocky.com/software/%{name}/%{name}-%{version}.tar.gz.sig
Source2:        gpgkey-DB698D7199242560.asc
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  grep
BuildRequires:  make
# /oreon:deps
%description
A reasonable way to achieve a long term backup of OpenPGP (PGP, GnuPG,
etc) keys is to print them out on paper.  Paper and ink have amazingly
long retention qualities - far longer than the magnetic or optical
means that are generally used to back up computer data.  A paper
backup isn't a replacement for the usual machine readable (tape, CD-R,
DVD-R, etc) backups, but rather as an if-all-else-fails method of
restoring a key.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%gpgverify -d0 -s1 -k2
%autosetup -p1

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

%make_build check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
