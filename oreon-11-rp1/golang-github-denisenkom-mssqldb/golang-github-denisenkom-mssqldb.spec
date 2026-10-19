%global source0_hash a7f37c85fc2348a50a574cfe30b821d59ccea2224732735fbfcf50e826fbb692
%ifnarch %{ix86} %{arm}
%bcond check 0
%endif
%global debug_package %{nil}
%global goipath         github.com/denisenkom/go-mssqldb
%global commit          36b6ff1bbc103b7b9497bb3c0c6f2788015ea02f
Version:                0.12.3
%global tag             0.9.0
%gometa
%global common_description %{expand:
Package Mssql implements the TDS protocol used to connect to MS SQL Server
database servers.}
%global golicenses      LICENSE.txt
%global godocs          doc examples README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Microsoft SQL server driver written in Go language
License:        BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{tag}/go-mssqldb-%{tag}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/adal)
BuildRequires:  golang(github.com/golang-sql/civil)
BuildRequires:  golang(golang.org/x/crypto/md4)
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
