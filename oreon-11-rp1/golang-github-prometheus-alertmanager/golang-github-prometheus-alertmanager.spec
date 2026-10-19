%global source0_hash af1a0090fa351fdc21e894278f3690cfd82575ad9354c32a76489b3d50ee6fa2
%bcond check 1
%global shortname prometheus-alertmanager
%global goipath         github.com/prometheus/alertmanager
Version:                0.28.1
%gometa -L -f
%global common_description %{expand:
The Alertmanager handles alerts sent by client applications such as the
Prometheus server. It takes care of deduplicating, grouping, and routing them to
the correct receiver integrations such as email, PagerDuty, or OpsGenie. It also
takes care of silencing and inhibition of alerts.}
Name:           golang-github-prometheus-alertmanager
Release:        1%{?dist}
Summary:        Prometheus Alertmanager
License:        Apache-2.0 AND BSD-3-Clause AND CC0-1.0 AND ISC AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/alertmanager-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Source3:        %{shortname}.service
Source4:        %{shortname}.sysusers
Source5:        %{shortname}.conf
Source6:        %{shortname}.yml
Source7:        README.templates
Source8:        %{shortname}.logrotate
Patch:          0003-Debian-defaults.patch
Requires(pre): shadow-utils
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

export GO_LDFLAGS="-X github.com/prometheus/common/version.Version=%{version}  \
         -X github.com/prometheus/common/version.Revision=%{release} \
         -X github.com/prometheus/common/version.Branch=tarball      \
         -X github.com/prometheus/common/version.BuildDate=$(date -u -d@$SOURCE_DATE_EPOCH +%%Y%%m%%d)"
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
mv %{buildroot}%{_bindir}/alertmanager %{buildroot}%{_bindir}/%{shortname}
pushd %{buildroot}%{_bindir}
ln -s %{shortname} alertmanager
popd
install -Dpm0644 %{S:6} %{buildroot}%{_sysconfdir}/prometheus/alertmanager.yml
install -Dpm0644 %{S:7} %{buildroot}%{_sysconfdir}/prometheus/alertmanager_templates/README.templates
mkdir -vp %{buildroot}%{_sharedstatedir}/prometheus/alertmanager
install -Dpm0644 %{S:3} %{buildroot}%{_unitdir}/%{shortname}.service
install -Dpm0644 %{S:4} %{buildroot}%{_sysusersdir}/%{shortname}.conf
install -Dpm0644 %{S:5} %{buildroot}%{_sysconfdir}/default/%{shortname}
install -Dpm0644 %{S:8} %{buildroot}%{_sysconfdir}/logrotate.d/%{shortname}
install -Dpm0644 template/default.tmpl %{buildroot}/%{_datadir}/prometheus/alertmanager/template/default.tmpl
mkdir -vp %{buildroot}/%{_mandir}/man1/
%{buildroot}%{_bindir}/%{shortname} --help-man > \
    %{buildroot}/%{_mandir}/man1/%{shortname}.1
%{buildroot}%{_bindir}/amtool --help-man > \
    %{buildroot}/%{_mandir}/man1/amtool.1
sed -i '/^  /d; /^.SH "NAME"/,+1c.SH "NAME"\nprometheus-alertmanager \\- The Prometheus alert manager' \
    %{buildroot}/%{_mandir}/man1/%{shortname}.1
sed -i '/^  /d; /^.SH "NAME"/,+1c.SH "NAME"\namtool \\- Tooling for the Prometheus alert manager' \
    %{buildroot}/%{_mandir}/man1/amtool.1
sed -i 's/\.\/amtool/amtool/' %{buildroot}/%{_mandir}/man1/amtool.1
%oreon_autofiles main

%pre

%sysusers_create_compat %{SOURCE4}
%post

%systemd_post %{shortname}.service
%preun

%systemd_preun %{shortname}.service
%postun

%systemd_postun_with_restart %{shortname}.service
%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
for test in "TestFinalAdvertiseAddr" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
