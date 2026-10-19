%global source0_hash 9901a14e8c6af02b7333c60b21ff81f50620e8326d54827185e5617ff9b11d21
Name:           phytool
Version:        2
Release:        1%{?dist}
Summary:        CLI for Linux MDIO register access
License:        GPL-2.0-or-later
URL:            https://github.com/wkz/phytool/
Source0:        https://github.com/wkz/%{name}//releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch0:         0001-Checked-return-of-asprintf-for-lack-of-memory-and-er.patch
Patch1:         0002-Make-fixes-to-Makefile-found-in-Fedora-spec-file-rev.patch
Patch2:         0003-Add-man-pages-and-adjust-Makefile-for-man-pages.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
phytool is a command line tool for reading MDIO registers and working
with Marvell Link register access

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
%make_build
%install
%make_install PREFIX='%{_prefix}'
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
