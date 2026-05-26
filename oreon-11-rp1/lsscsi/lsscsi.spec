Summary:        List SCSI devices (or hosts) and associated information
Name:           lsscsi
Version:        0.32
Release:        15%{?dist}
License:        GPL-2.0-or-later
# official git repository: https://github.com/doug-gilbert/lsscsi
Source0:        http://sg.danny.cz/scsi/%{name}-%{version}.tgz
# oreon url source checksums begin
%global source0_sha256 0a800e9e94dca2ab702d65d72777ae8cae078e3d74d0bcbed64ba0849e8029a1
%global source0_file lsscsi-0.32.tgz
# oreon url source checksums end
URL:            http://sg.danny.cz/scsi/lsscsi.html
BuildRequires:  gcc
BuildRequires:  make

%description
Uses information provided by the sysfs pseudo file system in Linux kernel
2.6 series to list SCSI devices or all SCSI hosts. Includes a "classic"
option to mimic the output of "cat /proc/scsi/scsi" that has been widely
used prior to the lk 2.6 series.

Author:
--------
    Doug Gilbert <dgilbert(at)interlog(dot)com>


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/lsscsi-0.32.tgz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "0a800e9e94dca2ab702d65d72777ae8cae078e3d74d0bcbed64ba0849e8029a1" || { echo "oreon: Source0 SHA256 mismatch for lsscsi-0.32.tgz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

%build
%configure
%make_build


%install
%make_install


%files
%doc ChangeLog INSTALL README CREDITS AUTHORS COPYING
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.32-15
- Prepare for Oreon 11 (RP1)
