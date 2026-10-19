%global source0_hash 7556a83218de6ff10897ed5d54d77f0fc141032bc70d452b8110bd027186cd77
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/Azure/go-autorest
Version:                14.2.0
%global tag             autorest/v0.11.30
%global distprefix      %{nil}
%gometa
%global common_description %{expand:
This package implements an HTTP request pipeline suitable for use across
multiple go-routines and provides the shared routines relied on by AutoRest
generated Go code.}
%global golicenses      LICENSE
%global godocs          README.md CHANGELOG.md example
Name:           %{goname}
Release:        1%{?dist}
Summary:        HTTP request client for use with Autorest-generated API client packages
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{tag}/go-autorest-autorest-v0.11.30.tar.gz
%if %{with check}
%endif
Patch: format-error.patch
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(contrib.go.opencensus.io/exporter/ocagent)
BuildRequires:  golang(github.com/dimchansky/utfbom)
BuildRequires:  golang(github.com/form3tech-oss/jwt-go)
BuildRequires:  golang(github.com/golang-jwt/jwt/v4)
BuildRequires:  golang(github.com/mitchellh/go-homedir)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(go.opencensus.io/plugin/ochttp)
BuildRequires:  golang(go.opencensus.io/plugin/ochttp/propagation/tracecontext)
BuildRequires:  golang(go.opencensus.io/stats/view)
BuildRequires:  golang(go.opencensus.io/trace)
BuildRequires:  golang(golang.org/x/crypto/pkcs12)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -v -p1

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d tracing -d logger
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
