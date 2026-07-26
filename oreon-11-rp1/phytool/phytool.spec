%global source0_hash 9901a14e8c6af02b7333c60b21ff81f50620e8326d54827185e5617ff9b11d21

Name:           phytool
Version:        2
Release:        7%{?dist}
Summary:        CLI for Linux MDIO register access

License:        GPL-2.0-or-later
URL:            https://github.com/wkz/phytool/
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz

## Patches go here.
## https://github.com/wkz/phytool/pull/14
Patch0:         0001-Checked-return-of-asprintf-for-lack-of-memory-and-er.patch
## https://github.com/wkz/phytool/pull/15
# Fix Makefile to create PREFIXdir
# Fix Makefile to use sha512sum instead of md5sum for FIPS systems
Patch1:         0002-Make-fixes-to-Makefile-found-in-Fedora-spec-file-rev.patch
## https://github.com/wkz/phytool/pull/16
# Fix Makefile to create manpage
# Add man pages written by Ben Beasley
Patch2:         0003-Add-man-pages-and-adjust-Makefile-for-man-pages.patch

BuildRequires:  make
BuildRequires:  gcc

%description
phytool is a command line tool for reading MDIO registers and working
with Marvell Link register access

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%set_build_flags
%make_build

%install
%make_install PREFIX='%{_prefix}'

%files
%license LICENSE
%doc README.md
%{_bindir}/phytool
%{_bindir}/mv6tool
%{_mandir}/man8/phytool.8*
%{_mandir}/man8/mv6tool.8*

%changelog
%autochangelog
