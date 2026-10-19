%global source0_hash ec56d12ec9ffdb9877c12692ea6e51620b1ae44473d3d253b27fc31ed9ebb4dd
Summary:        A program for recovering corrupt partition tables
Name:           gpart
Version:        0.3
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://github.com/baruch/%{name}/
Source0:        https://github.com/baruch/%{name}//archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         fsf_address.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Gpart is a small tool which tries to guess what partitions are on a PC
type harddisk in case the primary partition table was damaged.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
autoreconf -f -i

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
