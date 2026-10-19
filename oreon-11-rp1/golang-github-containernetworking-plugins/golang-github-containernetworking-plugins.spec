%global source0_hash 34bd82d47e981940751619c9cc44c095bb90bfcaf8d71865cbb822c37690a764
%global debug_package %{nil}
%bcond check 1
%global goipath         github.com/containernetworking/plugins
Version:                1.9.1
%gometa
%global common_description %{expand:
Some CNI network plugins, maintained by the containernetworking team.}
%global golicenses      LICENSE
%global godocs          RELEASING.md CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Standard networking plugins, maintained by the CNI team
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/plugins-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

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
