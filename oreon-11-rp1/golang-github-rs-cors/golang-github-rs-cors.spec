%global source0_hash 9dfa637cfee4547e7bd30b8216cb89de3a41e485ff19e63172b509e407f519cb
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/rs/cors
Version:                1.11.1
%gometa
%global common_description %{expand:
CORS is a net/http handler implementing Cross Origin Resource Sharing W3
specification in Golang.}
%global golicenses      LICENSE
%global godocs          examples README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go net/http configurable handler to handle CORS requests
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/cors-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/gin-gonic/gin)
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
