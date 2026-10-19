%global source0_hash df8904662382e1d0064ec7a5a8c36c49264d7128cea923d597802ada8c5b9603
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/jackc/pgpassfile
Version:                1.0.0
%gometa
%global common_description %{expand:
Package Pgpassfile is a parser for PostgreSQL .pgpass files.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Parser for PostgreSQL .pgpass files
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/pgpassfile-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
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
