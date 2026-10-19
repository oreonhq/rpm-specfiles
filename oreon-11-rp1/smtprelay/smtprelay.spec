%global source0_hash e1256d2a0eaf06331b307e41a902d5f22eb99f6d40966c4e0ece4545a5314490
%bcond check 1
%global goipath         github.com/decke/smtprelay
Version:                1.13.1
%gometa -L -f
Name:           smtprelay
Release:        1%{?dist}
Summary:        Simple Golang SMTP relay/proxy server
License:        Apache-2.0 AND BSD-3-Clause AND ISC AND MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Source3:        smtprelay.service
Source4:        smtprelay.sysusers
%{?sysusers_requires_compat}
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Simple Golang SMTP relay/proxy server.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}

%build

%global gomodulesmode GO111MODULE=on
export GO_LDFLAGS="-X main.appVersion=%{version} \
                   -X main.buildTime=$(date -d "@${SOURCE_DATE_EPOCH}" +%Y-%m-%dT%H:%M:%SZ)"
%gobuild -o %{gobuilddir}/bin/smtprelay %{goipath}
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                             %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/*         %{buildroot}%{_bindir}/
install -m 0755 -vd                             %{buildroot}%{_sysconfdir}
install -m 0750 -vd                             %{buildroot}%{_sysconfdir}/smtprelay
install -m 0640 -vp smtprelay.ini %{buildroot}/%{_sysconfdir}/smtprelay
install -D -p -m 0644 %{S:3} %{buildroot}%{_unitdir}/smtprelay.service
install -D -p -m 0644 %{S:4} %{buildroot}%{_sysusersdir}/smtprelay.conf
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%pre

%sysusers_create_compat %{S:4}
%post

%systemd_post smtprelay.service
%preun

%systemd_preun smtprelay.service
%postun

%systemd_postun_with_restart smtprelay.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
