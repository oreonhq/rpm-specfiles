%global source0_hash 8b55b87731e13816f2dbc6aa70faf85fdc950e213d2ed81fb50e9a5b5addf05f
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/go-martini/martini
Version:                1.0
%global commit          22fa46961aabd2665cf3f1343b146d20028f5071
%gometa
%global common_description %{expand:
Martini is a powerful package for quickly writing modular web
applications/services in Golang.}
%global golicenses      LICENSE
%global godocs          README.md translations/*.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Classy web framework for go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/martini-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/codegangsta/inject)
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
