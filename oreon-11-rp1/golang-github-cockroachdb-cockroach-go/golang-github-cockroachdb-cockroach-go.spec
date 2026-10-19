%global source0_hash 10ad6092b85d7ccc54950a2fcbea97e970cc6d2de48cc40cd73933c0c9d7f8f0
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/cockroachdb/cockroach-go
Version:                2.4.3
%gometa
%global goname          golang-github-cockroachdb-cockroach-go
%global godevelname     golang-github-cockroachdb-cockroach-go-devel
%global goaltipaths     github.com/cockroachdb/cockroach-go/v2
%global common_description %{expand:
Testing helpers for cockroach clients.}
%global golicenses      LICENSE
%global godocs          README.md crdb/README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Testing helpers for cockroach clients.
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/cockroach-go-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/jackc/pgx/v4)
BuildRequires:  golang(github.com/jmoiron/sqlx)
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(gorm.io/gorm)
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
