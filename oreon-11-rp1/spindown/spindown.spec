%global source0_hash 551167e3d0a20cb56d3729ae91cf831a4faae2d1287c7f205bbc2f1d011ec37b
Summary:        Daemon that can spin idle disks down
Name:       spindown
Version:    0.4.0
Release:        1%{?dist}
License:    GPL-3.0-or-later
Url:        http://code.google.com/p/spindown
Source0:        http://spindown.googlecode.com/files/spindown-%{version}.tar.gz
Source1:    spindown.service
Source2:    01spindown
Patch0:     spindown-0.4.0-Makefile.patch
Patch1:     spindown-0.4.0-iniparser.patch
Patch2:     spindown-0.4.0-iniparser-3.0-1.patch
Patch3:     spindown-0.4.0-bz1037334.patch
Patch4:     spindown-0.4.0-gcc-14.x.patch
Requires(preun): systemd-units
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  iniparser-devel
BuildRequires:  make
BuildRequires:  systemd-units
# /oreon:deps
%description
Spindown is a daemon that can spin idle disks down and thus save energy and
improve disk lifetime. It periodically checks for read or written blocks. When
no blocks are read or written the disk is idle. When a disk stays idle long
enough, spindown uses custom command like sg_start or hdparm to spin it down.
It also works with USB disks and hot-swappable disks because it doesn't watch
the device name (hda, sdb, ...), but the device ID. This means that it doesn't
matter if the disk is swapped while the daemon is running.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
rm -rf src/ininiparser3.0b
cp -pf %{SOURCE1} spindown.service
cp -pf %{SOURCE2} 01spindown

%build

sed -i 's/sbin/bin/' Makefile
%make_build OPT="$RPM_OPT_FLAGS"
%install
%make_install
mkdir -p %{buildroot}%{_libdir}/pm-utils/sleep.d
mkdir -p %{buildroot}%{_unitdir}
install -p -m 755 01spindown %{buildroot}%{_libdir}/pm-utils/sleep.d/01spindown
install -p -m 755 spindown.service %{buildroot}%{_unitdir}/spindown.service
%oreon_autofiles main

%preun

%systemd_preun spindown.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
