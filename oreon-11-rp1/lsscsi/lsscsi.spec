%global source0_hash bdb38cd930df73b7879125fba2a63c97d3c20d46c222707243445ddf5b8a0dd0

Summary:        List SCSI devices (or hosts) and associated information
Name:           lsscsi
Version:        0.33
Release:        1%{?dist}
License:        GPL-2.0-or-later
Source0:        https://github.com/doug-gilbert/lsscsi/archive/refs/tags/r%{version}.tar.gz
URL:            http://sg.danny.cz/scsi/lsscsi.html
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
Uses information provided by the sysfs pseudo file system in Linux kernel
2.6 series to list SCSI devices or all SCSI hosts. Includes a "classic"
option to mimic the output of "cat /proc/scsi/scsi" that has been widely
used prior to the lk 2.6 series.

Author:
--------
    Doug Gilbert <dgilbert(at)interlog(dot)com>


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-r%{version}

%build
autoreconf -fi
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
