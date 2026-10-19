%global source0_hash 2185b2383e84bec9a892cf5c1f4fb74ffbf8ccaa85c63045883e94da9b4ee30a
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/docker/go-metrics
Version:                0.1.0
%gometa
%global common_description %{expand:
This package is small wrapper around the prometheus Go client to help enforce
convention and best practices for metrics collection in Docker projects.}
%global golicenses      LICENSE LICENSE.docs NOTICE
%global godocs          CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Package for metrics collection in Docker projects
License:        Apache-2.0 and CC-BY-SA-4.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-metrics-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

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
