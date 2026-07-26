%global source0_hash 002ae9d86ae94fe4d9fe94d1bddf16884c7c37df441a3ddb0d8ee1633ffcc096

Name:           ufiformat
Version:        0.9.8
Release:        31%{?dist}
Summary:        Disk formatting utility for USB floppy devices

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.geocities.jp/tedi_world/format_usbfdd_e.html
Source0:        http://www.geocities.jp/tedi_world/ufiformat-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  e2fsprogs-devel

%description
ufiformat is a disk formatting utility for USB floppy devices.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%files
%doc COPYING README AUTHORS ChangeLog
%{_bindir}/ufiformat
%{_mandir}/man8/ufiformat.8*

%changelog
%autochangelog
