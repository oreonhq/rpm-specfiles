%global source0_hash 5f2033bef15cfb6078d3b9e3e7f099f678a134a45ddc2ec918346a9c1b7dbf4a
%define __cmake_in_source_build 1
Name:           target-isns
License:        GPL-2.0-or-later
Summary:        An iSNS client for the Linux LIO iSCSI target
Version:        0.6.8
Release:        1%{?dist}
URL:            https://github.com/cvubrugier/target-isns
Source0:        https://github.com/open-iscsi/target-isns/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-disable-stringop-overflow-and-stringop-truncation-er.patch
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd-units
# /oreon:deps
%description
Target-isns is an Internet Storage Name Service (iSNS) client for the Linux
LIO iSCSI target. It allows registering LIO iSCSI targets with an iSNS server.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build

%cmake -DSUPPORT_SYSTEMD=ON .
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
install -m 644 target-isns.service %{buildroot}%{_unitdir}
%oreon_autofiles main

%post

%systemd_post target-isns.service
%preun

%systemd_preun target-isns.service
%postun

%systemd_postun_with_restart target-isns.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
