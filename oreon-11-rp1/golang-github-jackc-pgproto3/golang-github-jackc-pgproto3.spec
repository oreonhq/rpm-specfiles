%global source0_hash 9dac3f55c63961f0365088f9b984356eb08665ba36e2a19f52d080e04dd1ed70
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/jackc/pgproto3
Version:                2.3.3
%gometa
%global goaltipaths     github.com/jackc/pgproto3/v2
%global common_description %{expand:
Package pgproto3 is a encoder and decoder of the PostgreSQL wire protocol
version 3.}
%global golicenses      LICENSE
%global godocs          example README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Eencoder and decoder of the PostgreSQL wire protocol
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/pgproto3-%{version}.tar.gz
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
