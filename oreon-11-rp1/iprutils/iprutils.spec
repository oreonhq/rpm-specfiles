%global source0_hash 027031d2101e448fadf74e1f75852dcc96d017f11758e6b270e10d9737f98c4e

%global gitver rel-2-4-19

Summary: Utilities for the IBM Power Linux RAID adapters
Name:    iprutils
Version: 2.4.19
Release: 17%{?dist}
License: CPL-1.0
URL:     https://github.com/bjking1/iprutils
Source0:        https://github.com/bjking1/iprutils/archive/%{gitver}/%{name}-%{version}.tar.gz#/iprutils-2.4.19.tar.gz

# missing man page
Source1:        iprdbg.8.gz

Patch10: iprutils-2.4.19-covscan.patch

ExclusiveArch: ppc64le

BuildRequires: libtool
BuildRequires: ncurses-devel
BuildRequires: libcap-devel
BuildRequires: kernel-headers
BuildRequires: systemd
BuildRequires: zlib-devel
BuildRequires: make


%description
Provides a suite of utilities to manage and configure SCSI devices
supported by the ipr SCSI storage device driver.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{gitver}

autoreconf -vif


%build
%configure --with-systemd --without-initscripts --disable-static --disable-sosreport
%{make_build}


%install
%{make_install}

# missing man page
install -p -m 0644 %SOURCE1 %{buildroot}%{_mandir}/man8/

#install bash completion
mv %{buildroot}/%{_sysconfdir}/bash_completion.d/{iprconfig-bash-completion.sh,iprconfig}

# Remove temporary files and scripts that will not be packaged.
rm %{buildroot}/%{_sysconfdir}/ha.d/resource.d/iprha


%post
%systemd_post iprinit.service
%systemd_post iprdump.service
%systemd_post iprupdate.service
%systemd_post iprutils.target

%preun
%systemd_preun iprinit.service
%systemd_preun iprdump.service
%systemd_preun iprupdate.service
%systemd_preun iprutils.target

%files
%license LICENSE
%doc README
%{_sbindir}/*
%{_sysconfdir}/bash_completion.d/
%{_mandir}/man*/*
%{_unitdir}/iprinit.service
%{_unitdir}/iprdump.service
%{_unitdir}/iprupdate.service
%{_unitdir}/iprutils.target
%{_udevrulesdir}/90-iprutils.rules


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4.19-17
- Import
