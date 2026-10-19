%global source20_hash 2dbc4b277cb2261b91f015459c25eb8602ab3c9989a228cd9974b264dea45d41
%global source0_hash f48251f5c89eea6d3b43814499d558bacc4829265419ee69be49c5af98f79573
%bcond check 1
%global shortname prometheus
%global goipath         github.com/prometheus/prometheus
Version:                2.55.1
%gometa -L -f
Name:           golang-github-prometheus
Release:        1%{?dist}
Summary:        Prometheus monitoring system and time series database
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{shortname}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Source3:        %{shortname}.service
Source4:        %{shortname}.sysusers
Source5:        %{shortname}.yml
Source6:        %{shortname}.conf
Source7:        %{shortname}.logrotate
Source8:        README.consoles
Source20:       https://github.com/prometheus/prometheus/releases/download/v%{version}/prometheus-web-ui-%{version}.tar.gz
Patch:          0001-Add-default-settings-adapted-for-Debian.patch
Patch:          0001-Use-full-path-for-Fedora.patch
Patch:          0001-parser-fix-non-constant-format-string-call.patch
Requires(pre):  shadow-utils
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
The Prometheus monitoring system and time series database.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 -a20 %{forgesetupargs}
%autopatch -p1
# copy pre-generated web/ui static content and compress it
# required to create EmbedFS
cp -r static/* web/ui/static/
rm -rf static
sh scripts/compress_assets.sh

%build

%global gomodulesmode GO111MODULE=on
export BUILDTAGS="netgo builtinassets"
export LDFLAGS="-X github.com/prometheus/common/version.Version=%{version}  \
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
install -Dpm0644 %{S:4} %{buildroot}%{_sysusersdir}/%{shortname}.conf
install -Dpm0644 %{S:3} %{buildroot}%{_unitdir}/%{shortname}.service
install -Dpm0644 %{S:6} %{buildroot}%{_sysconfdir}/default/%{shortname}
install -Dpm0644 %{S:5} %{buildroot}%{_sysconfdir}/prometheus/prometheus.yml
install -Dpm0644 %{S:7} %{buildroot}%{_sysconfdir}/logrotate.d/prometheus
mkdir -vp %{buildroot}%{_sysconfdir}/prometheus/consoles
install -Dpm0644 %{S:8} %{buildroot}%{_sysconfdir}/prometheus/consoles/README.consoles
mkdir -vp %{buildroot}%{_sysconfdir}/prometheus/console_libraries
install -Dpm0644 %{S:8} %{buildroot}%{_sysconfdir}/prometheus/console_libraries/README.consoles
mkdir -vp %{buildroot}%{_sharedstatedir}/prometheus
mkdir -vp %{buildroot}/%{_mandir}/man1/
%{buildroot}%{_bindir}/%{shortname} --help-man > \
    %{buildroot}/%{_mandir}/man1/%{shortname}.1
%{buildroot}%{_bindir}/promtool --help-man > \
    %{buildroot}/%{_mandir}/man1/promtool.1
sed -i '/^  /d; /^.SH "NAME"/,+1c.SH "NAME"\nprometheus \\- The Prometheus monitoring server' \
    %{buildroot}/%{_mandir}/man1/%{shortname}.1
sed -i '/^  /d; /^.SH "NAME"/,+1c.SH "NAME"\npromtool \\- Tooling for the Prometheus monitoring system' \
    %{buildroot}/%{_mandir}/man1/promtool.1
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
for test in "TestDocumentation" "TestAutoReloadConfig_ValidToValid" "TestAutoReloadConfig_ValidToInvalidToValid" \
            "TestInvalidFileUpdate" "TestUpdateFileWithPartialWrites" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck -d github.com/prometheus/prometheus/promql \
         -d github.com/prometheus/prometheus/rules \
         -d github.com/prometheus/prometheus/scrape \
         -d github.com/prometheus/prometheus/tsdb
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
