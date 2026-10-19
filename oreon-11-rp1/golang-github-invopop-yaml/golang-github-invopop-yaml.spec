%global source0_hash ed413049f082f8a487b70634550b87fc50ca35514fc9711605945b4c79924a45
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/invopop/yaml
Version:                0.3.1
%gometa -f
%global common_description %{expand:
A better way to marshal and unmarshal YAML in Golang.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        A better way to marshal and unmarshal YAML in Golang
License:        MIT AND BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/yaml-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

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
