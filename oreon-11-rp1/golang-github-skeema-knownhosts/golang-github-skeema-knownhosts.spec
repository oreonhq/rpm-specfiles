%global source0_hash 275919987b4fc2d8735f2e706db0b393580dd79aed9a3e1913ffb64e82c0ae19
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/skeema/knownhosts
Version:                1.3.3
%gometa -L -f
%global common_description %{expand:
Go SSH known_hosts wrapper with host key lookup.}
%global golicenses      LICENSE NOTICE
%global godocs          README.md
Name:           golang-github-skeema-knownhosts
Release:        1%{?dist}
Summary:        Go SSH known_hosts wrapper with host key lookup
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/knownhosts-%{version}.tar.gz
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
