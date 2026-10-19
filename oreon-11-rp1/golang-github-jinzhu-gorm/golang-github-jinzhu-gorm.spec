%global source0_hash c7ea6db55ab5226b6eb71e5654d14690459d02304df50cdf4adbe70db0308cab
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/jinzhu/gorm
Version:                1.9.16
%gometa
%global common_description %{expand:
The fantastic ORM library for Golang, aims to be developer friendly.}
%global golicenses      License
%global godocs          README.md
%global gosupfiles      glide.lock glide.yaml
Name:           %{goname}
Release:        1%{?dist}
Summary:        The fantastic ORM library for Golang, aims to be developer friendly
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/gorm-%{version}.tar.gz
Source1:        glide.yaml
Source2:        glide.lock
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/denisenkom/go-mssqldb)
BuildRequires:  golang(github.com/erikstmartin/go-testdb)
BuildRequires:  golang(github.com/go-sql-driver/mysql)
BuildRequires:  golang(github.com/jinzhu/inflection)
BuildRequires:  golang(github.com/jinzhu/now)
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/lib/pq/hstore)
BuildRequires:  golang(github.com/mattn/go-sqlite3)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
cp %{S:1} %{S:2} .

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
