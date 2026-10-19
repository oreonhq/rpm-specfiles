%global source0_hash 091d90c479401bc9047454c25f91a97a6707e6a279ce778e4881cf6b0191a47f
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/hashicorp/go-cleanhttp
Version:                0.5.2
%gometa -L -f
%global common_description %{expand:
Convenience utilities for acquiring "clean" http.Transport and http.Client
structs}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-hashicorp-cleanhttp
Release:        1%{?dist}
Summary:        Convenience utilities for "clean" http.Transport and http.Client structs
License:        MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-cleanhttp-%{version}.tar.gz
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

%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
