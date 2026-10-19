%global source0_hash e7e94ce068878cdb8041602dc41f03e6271835df0b125066cb6fed8c367dfee4
Name:           rpmrebuild
Version:        2.21
Release:        2%{?dist}
Summary:        A tool to build rpm file from rpm database
License:        GPL-2.0-or-later
URL:            http://rpmrebuild.sourceforge.net
Source0:        http://downloads.sourceforge.net/rpmrebuild/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       rpm >= 4.0, rpm-build, coreutils, util-linux
# oreon:deps
BuildRequires:  make
# /oreon:deps
%description
A tool to build an RPM file from a package that has already been installed.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c 

%build

%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
