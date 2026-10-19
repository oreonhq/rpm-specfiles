%global source0_hash e0d5359b1419d3e9509eea117c75ef4f8a22fc8e721856ce40ff956633d648a1
%bcond check 1
%global goipath         github.com/subpop/mqttcli
Version:                0.2.8
%gometa -L -f
Name:           mqttcli
Release:        1%{?dist}
Summary:        A simple MQTT command-line client
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND EPL-2.0 AND GPL-3.0-only AND MIT AND Unlicense
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  /usr/bin/a2x
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
# /oreon:deps
%description
mqttcli provides two programs (pub and sub) that allow command-line access to an
MQTT broker.

sub subscribes to a topic and prints messages received to standard output.
pub publishes the provided message to the provided topic. Both programs
accept flags that can be provided as a config file.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%global gomodulesmode GO111MODULE=on
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
  a2x --doctype manpage --format manpage --destination-dir %{gobuilddir} doc/$(basename $cmd).adoc
done
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd                     %{buildroot}%{_mandir}/man1
install -m 0644 -vp %{gobuilddir}/*.1   %{buildroot}%{_mandir}/man1/
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
