%global source0_hash 58b1608f6de48f2e9238d9eacc3228c871d26b9155859d0253adef5564aaf34e
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/prometheus/procfs
Version:                0.22.0
%gometa -L -f
%global common_description %{expand:
Procfs provides functions to retrieve system, kernel and process metrics from
the pseudo-filesystem proc.}
%global golicenses      LICENSE NOTICE
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md MAINTAINERS.md\\\
                        README.md SECURITY.md
Name:           golang-github-prometheus-procfs
Release:        1%{?dist}
Summary:        Retrieve system, kernel and process metrics from proc
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/procfs-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

./ttar -x -C testdata -f ./testdata/fixtures.ttar
%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
