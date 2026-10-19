%global source0_hash 7536d8fcff10870d68662efaa4e583207e1a311509d589764c26264dccb4a241
%global debug_package %{nil}
%bcond check 0
%global goipath         github.com/emicklei/go-restful
Version:                3.13.0
%gometa
%global goaltipaths     github.com/emicklei/go-restful/v3
%global common_description %{expand:
Package for building REST-style Web Services using Go.}
%global golicenses      LICENSE
%global godocs          examples CHANGES.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Package for building REST-style Web Services using Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-restful-%{version}.tar.gz
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
