%global source0_hash 486a5d61486cf0b51ad393feaee0b9b2f3aceeb1528b44490b3a9f3c9a6f3c2a
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/gin-contrib/cors
Version:                1.7.2
%gometa -L -f
%global common_description %{expand:
CORS middleware for Gin Gonic.}
%global golicenses      LICENSE
%global godocs          _examples README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        CORS gin's middleware
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/cors-%{version}.tar.gz
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
