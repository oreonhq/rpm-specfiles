%global source0_hash 5b0423567b1b0c622872fd53e4ebe87675a41c1dbc9741d16030baad6ca0334a
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/gocql/gocql
%global commit          e49edf966d9036342234c0f42c9643fbffdefaf5
%gometa
%global common_description %{expand:
Package Gocql implements a fast and robust cassandra client for Go.}
%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTING.md README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Fast and robust cassandra client for the Go
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/gocql-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/golang/snappy)
BuildRequires:  golang(github.com/hailocab/go-hostpool)
BuildRequires:  golang(gopkg.in/inf.v0)
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
