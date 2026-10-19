%global source0_hash ba5e02e82cb70d6d7cb7970a8f81535df3266cfeae2b2d3b9e38de7ca2d76b4a
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/armon/consul-api
%global commit          eb2c6b5be1b66bab83016e0b05f01b8d5496ffbd
%gometa
%global common_description %{expand:
This package provides the consulapi package which attempts to provide
programmatic access to the full Consul API.
Currently, all of the Consul APIs included in version 0.4 are supported.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Golang API client for Consul
License:        MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/consul-api-%{commit}.tar.gz
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
