%global source0_hash aeb88ad980fd87ee08b1b3e5c70977c32065115cc8152e3fc846e2d60b2a662f
%bcond check 1
%global shortname prometheus-node-exporter
%global goipath         github.com/prometheus/node_exporter
Version:                1.10.2
%gometa -L -f
%global godevelheader %{expand:
Obsoletes:      golang-github-prometheus-node-exporter-devel < 1.6.1-2
}
Name:           node-exporter
Release:        1%{?dist}
Summary:        Exporter for machine metrics
License:        Apache-2.0 AND BSD-2-Clause AND BSD-2-Clause-Views AND BSD-3-Clause AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/node_exporter-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Source3:        %{shortname}.sysusers
Source4:        %{shortname}.service
Source5:        %{shortname}.conf
Source6:        %{shortname}.logrotate
Source7:        %{shortname}-tmpfiles.conf
Patch:         0001-Set-defaults-that-make-sense-for-Fedora-RHEL-systems.patch
Requires(pre):  shadow-utils
Obsoletes:      golang-github-prometheus-node-exporter < 1.6.1-2
Provides:       node_exporter
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Prometheus exporter for hardware and OS metrics exposed by *NIX kernels, written
in Go with pluggable metric collectors.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%global gomodulesmode GO111MODULE=on
export BUILDTAGS="netgo osusergo static_build"
export GO_LDFLAGS="-X github.com/prometheus/common/version.Version=%{version}  \
         -X github.com/prometheus/common/version.Revision=%{release} \
         -X github.com/prometheus/common/version.Branch=tarball      \
         -X github.com/prometheus/common/version.BuildDate=$(date -u -d@$SOURCE_DATE_EPOCH +%%Y%%m%%d)"
%gobuild -o %{gobuilddir}/bin/node_exporter %{goipath}
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
mv %{buildroot}%{_bindir}/node_exporter %{buildroot}%{_bindir}/%{shortname}
pushd %{buildroot}%{_bindir}
ln -s %{shortname} node_exporter
popd
install -Dpm0644 %{S:3} %{buildroot}%{_sysusersdir}/%{shortname}.conf
install -Dpm0644 %{S:4} %{buildroot}%{_unitdir}/%{shortname}.service
pushd %{buildroot}%{_unitdir}
ln -s %{shortname}.service node_exporter.service
popd
install -Dpm0644 %{S:5} %{buildroot}%{_sysconfdir}/default/%{shortname}
install -Dpm0644 example-rules.yml %{buildroot}%{_datadir}/prometheus/node-exporter/example-rules.yml
install -Dpm0644 %{S:6} %{buildroot}%{_sysconfdir}/logrotate.d/%{shortname}
mkdir -vp %{buildroot}%{_sharedstatedir}/prometheus/node-exporter
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{S:7} %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -vp %{buildroot}/%{_mandir}/man1/
%{buildroot}%{_bindir}/%{shortname} --help-man > \
    %{buildroot}/%{_mandir}/man1/%{shortname}.1
sed -i '/^  /d; /^.SH "NAME"/,+1c.SH "NAME"\nprometheus-node-exporter \\- The Prometheus Node-Exporter' \
    %{buildroot}/%{_mandir}/man1/%{shortname}.1
sleep 1
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
for f in collector/fixtures/*.ttar; do
    d="${f%.ttar}"
    rm -rf "$d"
    ./ttar -C "$(dirname "$d")" -x -f "$f"
done
%gocheck2
%endif
%pre

%sysusers_create_compat %{SOURCE3}
%post

%systemd_post %{shortname}.service
%preun

%systemd_preun %{shortname}.service
%postun

%systemd_postun_with_restart %{shortname}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
