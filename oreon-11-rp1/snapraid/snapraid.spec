%global source0_hash 40c216979d9d9853248060497341f74feaa07c8ae15927b6b14972c4f9d143d5
Name:           snapraid
Summary:        Disk array backup for many large rarely-changed files
Version:        14.9
Release:        1%{?dist}
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.0-or-later AND Apache-2.0 AND LicenseRef-Fedora-Public-Domain AND BSD-2-Clause
URL:            https://www.snapraid.it/
Source0:        https://github.com/amadvance/snapraid/releases/download/v%{version}/snapraid-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libblkid-devel
BuildRequires:  make
# /oreon:deps
%description
SnapRAID is a backup program for disk arrays. It stores parity
information of your data and it's able to recover from up to six disk
failures. SnapRAID is mainly targeted for a home media center, with a
lot of big files that rarely change.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
mv raid/COPYING raid/COPYING-raid

%build

%configure
%make_build
%check

make check
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
