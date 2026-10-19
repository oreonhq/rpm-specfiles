%global source0_hash 179ca725463e7f13be8591bc285f4048da6887b1056d96848b16e137c995a2e2
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/form3tech-oss/jwt-go
Version:                3.2.2
%gometa
%global common_description %{expand:
Golang implementation of JSON Web Tokens (JWT).}
%global golicenses      LICENSE
%global godocs          MIGRATION_GUIDE.md README.md VERSION_HISTORY.md\\\
                        cmd/jwt/README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Golang implementation of JSON Web Tokens (JWT)
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/jwt-go-%{version}.tar.gz
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
