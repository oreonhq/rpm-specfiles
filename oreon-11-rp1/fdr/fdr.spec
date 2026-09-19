%global source0_hash 164a1ca81f17fcf24f12f66af60de76fba47b9b0941e89d8544985ca78dcfa2c

Summary:	A daemon which enables ftrace probes and harvests the data
Name:		fdr
URL:		https://github.com/oracle/fdr.git
Version:	1.3
Release:	11%{?dist}
# Automatically converted from old format: UPL - review is highly recommended.
License:	UPL-1.0
Source0:	http://people.redhat.com/steved/fdr/%{name}-%{version}.tar.xz

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	sed
BuildRequires:	systemd-rpm-macros
Requires:	systemd

%description
The flight data recorder, a daemon which enables ftrace probes
and harvests the data

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
sed -i -e "s:^CFLAGS.*:CFLAGS = %{optflags}:" Makefile
%make_build

%install
mkdir -p %{buildroot}/%{_sbindir}
install -m 755 fdrd %{buildroot}/%{_sbindir}

mkdir -p %{buildroot}%{_datadir}/fdr/samples
install -m 644 samples/nfs %{buildroot}/%{_datadir}/fdr/samples
install -m 644 samples/nfs.logrotate %{buildroot}/%{_datadir}/fdr/samples

mkdir -p %{buildroot}/%{_unitdir}
install -m 644 %{name}.service %{buildroot}/%{_unitdir}/%{name}.service

mkdir -p %{buildroot}/%{_mandir}/man8
install -m 644 fdrd.man %{buildroot}/%{_mandir}/man8/fdrd.8

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%{_sbindir}/fdrd
%{_unitdir}/fdr.service
%{_datadir}/fdr/samples/nfs
%{_datadir}/fdr/samples/nfs.logrotate
%{_mandir}/man8/*
%doc README.md
%license LICENSE

%changelog
%autochangelog
