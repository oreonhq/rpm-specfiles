%global source0_hash ef31953e2ad6c7433459467920d3cda049d10d03145e83f6b7410bf1b7d2650d
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/jmoiron/sqlx
Version:                1.4.0
%gometa
%global common_description %{expand:
Sqlx is a library which provides a set of extensions on Go's standard
database/sql library. The sqlx versions of sql.DB, sql.TX, sql.Stmt, et al. all
leave the underlying interfaces untouched, so that their interfaces are a
superset on the standard ones. This makes it relatively painless to integrate
existing codebases using database/sql with sqlx.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        General purpose extensions to golang's database/sql
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/sqlx-%{version}.tar.gz
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
