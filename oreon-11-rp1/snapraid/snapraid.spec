%global source0_hash 0282a9eec3301cd608dc45d9182b6d207f9fd4d25828c9deb329a015c77cb4e2

Name:           snapraid
Summary:        Disk array backup for many large rarely-changed files
Version:        13.0
Release:        2%{?dist}
# snapraid itself is GPL-3.0-or-later but uses other source codes, breakdown:
# Apache-2.0 AND GPL-3.0-or-later: cmdline/metro.c
# BSD-2-Clause: tommyds/*
# GPL-2.0-or-later: raid/*
# GPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain: cmdline/murmur3.c
# LGPL-2.0-or-later: cmdline/fnmatch.[ch]
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.0-or-later AND Apache-2.0 AND LicenseRef-Fedora-Public-Domain AND BSD-2-Clause

URL:            https://www.snapraid.it/
Source0:        https://github.com/amadvance/snapraid/releases/download/v%{version}/snapraid-%{version}.tar.gz

BuildRequires:  gcc make libblkid-devel

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

%files
%license COPYING tommyds/LICENSE raid/COPYING-raid
%doc AUTHORS HISTORY README
%{_bindir}/snapraid
%{_mandir}/man1/snapraid.1*

%changelog
%autochangelog
