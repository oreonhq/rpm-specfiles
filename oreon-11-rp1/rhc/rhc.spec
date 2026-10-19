%global source0_hash 91c3e3b794bf5e23bf6df9948d8955ec539564d2006bcde65880b5157ed3fa49
%bcond check 0
%global goipath         github.com/redhatinsights/rhc
Version:                0.3.8
%gometa -L -f
Name:           rhc
Release:        1%{?dist}
Summary:        Tool for registering to Red Hat services
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND GPL-3.0-only AND MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
%if %{with check}
%endif
Requires: subscription-manager
Requires: yggdrasil >= 0.4
Requires: yggdrasil-worker-package-manager
# oreon:deps
BuildRequires:  /usr/bin/dbus-launch
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Client tool to register Fedora, CentOS Stream or Red Hat Enterprise Linux
to Red Hat Subscription Management and Red Hat Lightspeed.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}

%build

export GO_LDFLAGS="-X main.Version=%{version} -X main.ServiceName=yggdrasil"
%gobuild -o %{gobuilddir}/bin/rhc %{goipath}/cmd/rhc
%{gobuilddir}/bin/rhc --generate-man-page > rhc.1
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp _build/bin/*        %{buildroot}%{_bindir}/
install -m 0755 -vd                     %{buildroot}%{bash_completions_dir}/
install -m 0644 -vp data/completion/rhc.bash  %{buildroot}%{bash_completions_dir}/%{name}
install -m 0755 -vd                     %{buildroot}%{_mandir}/man1
install -m 0644 -vp rhc.1               %{buildroot}%{_mandir}/man1/rhc.1
install -m 0755 -vd                     %{buildroot}%{_unitdir}
install -m 0644 -vp data/systemd/rhc-canonical-facts.*  %{buildroot}%{_unitdir}/
install -m 0755 -vd                     %{buildroot}%{_sysconfdir}/%{name}/
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gocheck2
%endif
%post

%systemd_post rhc-canonical-facts.timer
%preun

%systemd_preun rhc-canonical-facts.timer
%postun

%systemd_postun_with_restart rhc-canonical-facts.timer
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
