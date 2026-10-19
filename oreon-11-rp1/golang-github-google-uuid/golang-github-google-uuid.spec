%global source0_hash ee63376b5675376c60e055ed66e5f3651ccc703bd580c022b8ad00cea309252d
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/google/uuid
Version:                1.6.0
%gometa -L
%global common_description %{expand:
Go package for UUIDs based on RFC 4122 and DCE 1.1: Authentication and Security
Services.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md CONTRIBUTING.md CONTRIBUTORS README.md
Name:           golang-github-google-uuid
Release:        1%{?dist}
Summary:        Go package for UUIDs based on RFC 4122 and DCE 1.1
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/uuid-%{version}.tar.gz
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
