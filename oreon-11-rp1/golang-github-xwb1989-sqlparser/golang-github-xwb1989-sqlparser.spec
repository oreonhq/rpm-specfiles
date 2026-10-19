%global source0_hash 22ce465dc59d7e31515a523a2b0c7d6f5e2b0ab25289bc79a86666483799022a
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/xwb1989/sqlparser
%global commit          120387863bf27d04bc07db8015110a6e96d0146c
%gometa
%global common_description %{expand:
SQL Parser implemented in Go.}
%global golicenses      LICENSE.md
%global godocs          CONTRIBUTORS.md README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        SQL Parser implemented in Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/sqlparser-%{commit}.tar.gz
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
