%global source0_hash 9dc7ea5faef300ab80bbd90d1811b59255475703c4d643ea6f800d356d518d15
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/golang-jwt/jwt/v4
Version:                4.2.0
%gometa
%global common_description %{expand:
Golang implementation of JSON Web Tokens.}
%global golicenses      LICENSE
%global godocs          MIGRATION_GUIDE.md README.md VERSION_HISTORY.md\\\
                        cmd/jwt/README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Golang implementation of JSON Web Tokens
License:        MIT
URL:            %{gourl}
Source0:        https://github.com/golang-jwt/jwt/archive/v%{version}/jwt-%{version}.tar.gz
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
