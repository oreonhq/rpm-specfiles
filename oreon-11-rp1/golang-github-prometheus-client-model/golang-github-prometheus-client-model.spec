%global source0_hash 77b46a8f9924c42095422fe7d51ac2df3a2cae6d354e14ce1b70a16b52ae3983
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/prometheus/client_model
Version:                0.6.3
%gometa -L
%global common_description %{expand:
Data model artifacts for Prometheus.}
%global golicenses      LICENSE NOTICE
%global godocs          CONTRIBUTING.md MAINTAINERS.md README.md
Name:           golang-github-prometheus-client-model
Release:        1%{?dist}
Summary:        Data model artifacts for Prometheus
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/client_model-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
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
