%global source0_hash 509e846afd76e84bc5994b244e2ce0b986b4a9e99a8e80d5f31e691ce2efb6f4
%bcond check 0
%global goipath         code.forgejo.org/forgejo/runner/v12
%global forgeurl        https://code.forgejo.org/forgejo/runner
%global archivename     %{name}-%{version}
Version:                13.1.0
%gometa -L -f
Name:           forgejo-runner
Release:        1%{?dist}
Summary:        A daemon that fetches workflows to run from a Forgejo instance.
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND GPL-3.0-only AND ISC AND MIT AND MPL-2.0
URL:            https://code.forgejo.org/forgejo/runner
Source0:        %{forgeurl}/archive/v%{version}.tar.gz#/%{archivename}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Source3:        forgejo-runner.sysusers.conf
Patch:          0000-forgejo_runner-unit_fix.patch
%{?sysusers_requires_compat}
Requires:       git-core
Requires:       git-lfs
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
The Forgejo Runner is a daemon that fetches workflows to run from a Forgejo instance, executes them,
sends back with the logs and ultimately reports its success or failure.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%if 0%{?epel} && 0%{?epel} <= 10
%autosetup -n runner -a1 -p1
%else
%autosetup -a1 -p1
%endif

%build

%global gomodulesmode GO111MODULE=on
export GO_LDFLAGS=" \
    -X \"code.forgejo.org/forgejo/runner/v12/internal/pkg/ver.version=v%{version}\" \
"
%gobuild -o %{gobuilddir}/bin/forgejo-runner %{goipath}
%{gobuilddir}/bin/forgejo-runner generate-config > config.yml
%install
%go_vendor_license_install -c %{S:2}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sysusersdir}
install -d %{buildroot}%{_sysconfdir}/forgejo-runner/
install -d %{buildroot}%{_unitdir}
install -d %{buildroot}%{_sharedstatedir}/forgejo-runner/
install -m 755 -p %{gobuilddir}/bin/forgejo-runner %{buildroot}%{_bindir}/forgejo-runner
install -m 644 -p config.yml %{buildroot}%{_sysconfdir}/forgejo-runner/config.yml
install -m 644 -p %{S:3} %{buildroot}%{_sysusersdir}/forgejo-runner.conf
install -m 644 -p contrib/forgejo-runner.service %{buildroot}%{_unitdir}/forgejo-runner.service
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%pre

%sysusers_create_compat %{S:3}
%post

%systemd_post forgejo-runner.service
%preun

%systemd_preun forgejo-runner.service
%postun

%systemd_postun_with_restart forgejo-runner.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
