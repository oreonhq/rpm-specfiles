%global source0_hash cb2afe191d70bfc7c339b71d6ea0e4803f765ed67e5e38dc6c8dcf42d972bd98
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/docker/go-events
%global commit          e31b211e4f1cd09aa76fe4ac244571fab96ae47f
%gometa
%global common_description %{expand:
The Docker Events package implements a composable event distribution package for
Go.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Composable event distribution for Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-events-%{commit}.tar.gz
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
