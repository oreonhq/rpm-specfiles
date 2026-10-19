%global source0_hash 6f7418aeab872de7a5f098a2e539ed725c6c46a1ae144e48f1be0a4a4e495caa
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/chzyer/test
%global commit          a1ea475d72b168a29f44221e0ad031a842642302
%gometa
%global common_description %{expand:
Golang test utility.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Golang test utility
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/test-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/chzyer/logex)
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
