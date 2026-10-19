%global source0_hash 524d99f4566b5c1d483a41c4b0028ba0c5679aa65fd9c585245d9f9afd478232
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/letsencrypt/challtestsrv
Version:                1.4.2
%gometa -L -f
%global common_description %{expand:
Small TEST-ONLY server for mock DNS & responding to HTTP-01, DNS-01, and TLS-
ALPN-01 ACME challenges.}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md
Name:           golang-github-letsencrypt-challtestsrv
Release:        1%{?dist}
Summary:        Small TEST-ONLY server for mock ACME challenges
License:        MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/challtestsrv-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
