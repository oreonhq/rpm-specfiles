%global source0_hash 11444e883f12f2b85c08cfa0b89b0d762966deaf634bddfd4feca8ac97845be6
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/sacloud/go-http
Version:                0.1.10
%gometa -f
%global common_description %{expand:
HTTP client library for SAKURA cloud in Go.}
%global golicenses      LICENSE includes/LICENSE
%global godocs          AUTHORS README.md includes/AUTHORS includes/README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        HTTP client library for SAKURA cloud in Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-http-%{version}.tar.gz
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
