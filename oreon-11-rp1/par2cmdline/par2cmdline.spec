%global source2_hash 58a0cdbf59a0741cffd70c3272a2c4a93efc523682124e13a8b42837830bc18c
%global source0_hash aa13effa3a27bee2fecf0eb228b631b0323bc2e085c88bbdc7f4518f8fedcee3
Name: par2cmdline
Version: 1.5.0
Release:        1%{?dist}
Summary:        PAR 2.0 compatible file verification and repair tool
License: GPL-2.0-or-later
URL: https://github.com/Parchive/par2cmdline/
Source0:        https://github.com/Parchive/%{name}//releases/download/v%{version}/%{name}-%{version}.tar.bz2
Source1: %{url}/releases/download/v%{version}/par2cmdline-%{version}.tar.bz2.sig
Source2: https://keybase.io/blackikeeagle/pgp_keys.asc?fingerprint=db2277bcd500aa3825610bdddb323392796ca067#/gpg-db2277bcd500aa3825610bdddb323392796ca067.asc
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main

%check

make check-TESTS
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
