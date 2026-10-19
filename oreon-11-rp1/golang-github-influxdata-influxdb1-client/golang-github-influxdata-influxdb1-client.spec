%global source0_hash 8fdac08f8852adf713e3d5dd85fbee6d22234d38c3ba141c73ed3399a7a129ed
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/influxdata/influxdb1-client
%global commit          b269163b24ab8e62026d13a92aa988a7389c3b4e
%gometa
%global common_description %{expand:
Influxdb1-clientv2 is the current Go client API for InfluxDB 1.x.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Old clientv2 for InfluxDB 1.x
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/influxdb1-client-%{commit}.tar.gz
Patch:          https://github.com/influxdata/influxdb1-client/pull/60.patch#/fix-test-failures.patch
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
