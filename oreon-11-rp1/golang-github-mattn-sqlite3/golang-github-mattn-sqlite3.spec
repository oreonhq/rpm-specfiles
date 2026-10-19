%global source0_hash 2c7dfec993ed0dc1fb94a7c7a8168c3604e932d6a37463fb5a1e95f0cf374f83
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/mattn/go-sqlite3
Version:                1.14.14
%gometa
%global common_description %{expand:
Package Sqlite3 provides interface to SQLite3 databases.}
%global golicenses      LICENSE
%global godocs          _example README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Sqlite3 driver for go using database/sql
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-sqlite3-%{version}.tar.gz
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
