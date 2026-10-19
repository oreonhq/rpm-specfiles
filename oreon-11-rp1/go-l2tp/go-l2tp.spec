%global source0_hash e3c636098b1eef2cf4b83f871c7526d4ed27d2af239f98d7740d5fcdffab95b3
%bcond check 1
%global goipath         github.com/katalix/go-l2tp
Version:                0.1.8
%gometa -L -f
Name:           go-l2tp
Release:        1%{?dist}
Summary:        Go library for building L2TP applications on Linux systems
License:        Apache-2.0 AND BSD-3-Clause AND MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Provides:       golang-github-katalix-l2tp = %{version}-%{release}
Obsoletes:      golang-github-katalix-l2tp < 0.1.8-5
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
# /oreon:deps
%description
Go library for building L2TP applications on Linux systems.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -p1
tar -xf %{S:1}

%build

%global gomodulesmode GO111MODULE=on
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_sbindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_sbindir}/
install -m 0755 -vd                     %{buildroot}%{_mandir}/man8
install -m 0644 -vp doc/kl2tpd.8        %{buildroot}%{_mandir}/man8
install -m 0644 -vp doc/kpppoed.8       %{buildroot}%{_mandir}/man8
install -m 0644 -vp doc/ql2tpd.8        %{buildroot}%{_mandir}/man8
install -m 0755 -vd                     %{buildroot}%{_mandir}/man5
install -m 0644 -vp doc/kl2tpd.toml.5   %{buildroot}%{_mandir}/man5
install -m 0644 -vp doc/ql2tpd.toml.5   %{buildroot}%{_mandir}/man5
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gocheck2
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
