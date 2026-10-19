%global source0_hash 2f6bce4f4b2b28aec4e58fad1341f47cde9c30adb556399472a8831942057941
%bcond check 1
%global shortname prometheus-alertmanager
%global goipath         github.com/prometheus/alertmanager
Version:                0.34.1
%gometa -L -f
Name:           alertmanager
Release:        1%{?dist}
Summary:        Prometheus Alertmanager
License:        Apache-2.0 AND BSD-3-Clause AND CC0-1.0 AND ISC AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Source3:        %{shortname}.service
Source4:        %{shortname}.sysusers
Source5:        %{shortname}.conf
Source6:        %{shortname}.yml
Source7:        README.templates
Source8:        %{shortname}.logrotate
Patch:          0001-Default-paths-for-Fedora-EPEL-based-on-Debian-s.patch
Requires(pre):  shadow-utils
Obsoletes:      golang-github-prometheus-alertmanager < 0.28.1-5
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
The Alertmanager handles alerts sent by client applications such as the
Prometheus server. It takes care of deduplicating, grouping, and routing them to
the correct receiver integrations such as email, PagerDuty, or OpsGenie. It also
takes care of silencing and inhibition of alerts.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -p1
tar -xf %{S:1}

%build

%global gomodulesmode GO111MODULE=on
export GO_LDFLAGS="-X github.com/prometheus/common/version.Version=%{version}  \
         -X github.com/prometheus/common/version.Revision=%{release} \
         -X github.com/prometheus/common/version.Branch=tarball      \
         -X github.com/prometheus/common/version.BuildUser=Fedora
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
for test in "TestFinalAdvertiseAddr" "TestAlertsConcurrently" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
ln -s %{gobuilddir}/bin/amtool amtool
ln -s %{gobuilddir}/bin/alertmanager alertmanager
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
