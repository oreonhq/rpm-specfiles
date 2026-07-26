%global source0_hash aa13effa3a27bee2fecf0eb228b631b0323bc2e085c88bbdc7f4518f8fedcee3

Name: par2cmdline
Version: 1.1.1
Release: %autorelease
Summary: PAR 2.0 compatible file verification and repair tool

License: GPL-2.0-or-later
URL: https://github.com/Parchive/par2cmdline/
Source0: %{url}/releases/download/v%{version}/par2cmdline-%{version}.tar.bz2
Source1: %{url}/releases/download/v%{version}/par2cmdline-%{version}.tar.bz2.sig
# GitHub releases are signed by GitHub user https://github.com/BlackIkeEagle
# which has verified his GitHub handle via his Keybase.io profile
# https://keybase.io/blackikeeagle.
Source2: https://keybase.io/blackikeeagle/pgp_keys.asc?fingerprint=db2277bcd500aa3825610bdddb323392796ca067#/gpg-db2277bcd500aa3825610bdddb323392796ca067.asc

BuildRequires: make
BuildRequires: gcc-c++
# Needed for source file verification.
BuildRequires: gnupg2

%description
par2cmdline is a program for creating and using PAR2 files to detect damage
in data files and repair them if necessary. PAR2 files are usually
published in binary newsgroups on Usenet; they apply the data-recovery
capability concepts of RAID-like systems to the posting and recovery of
multi-part archives.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

# Remove executable permission from text files.
chmod -x configure.ac

%build
%configure
%make_build

%install
%make_install

%check
make check-TESTS

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_bindir}/par2
%{_bindir}/par2create
%{_bindir}/par2repair
%{_bindir}/par2verify
%{_mandir}/man1/par2.1*
%{_mandir}/man1/par2create.1*
%{_mandir}/man1/par2repair.1*
%{_mandir}/man1/par2verify.1*

%changelog
%autochangelog
