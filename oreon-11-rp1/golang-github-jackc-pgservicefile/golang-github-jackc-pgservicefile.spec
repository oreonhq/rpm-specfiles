%global source0_hash 6697d21c93468cb7552265b8064f53a4a83125aad2f2adf97598f4c8f8b5dd5c
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/jackc/pgservicefile
%global commit          091c0ba34f0a65a78ab8d0e313fde0695c0f7186
%gometa
%global common_description %{expand:
Pgservicefile is a parser PostgreSQL for service files (e.g. .pg_service.conf).}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Parser PostgreSQL for service files
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/pgservicefile-%{commit}.tar.gz
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
