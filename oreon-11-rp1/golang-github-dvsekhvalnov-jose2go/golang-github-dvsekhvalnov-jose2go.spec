%global source0_hash bc28c4db52f2a616741d4e8d063c0115bfa5a40d083a9bf77a421e958e6e849f
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/dvsekhvalnov/jose2go
Version:                1.11.0
%gometa -L
%global common_description %{expand:
Pure Go library for generating, decoding and encrypting JSON Web Tokens. Zero
dependency, relies only on standard library.
Supports full suite of signing, encryption and compression algorithms defined by
JSON Web Algorithms as of July 4, 2014 version.
Extensively unit tested and cross tested (100+ tests) for compatibility with
jose.4.j, Nimbus-JOSE-JWT, json-jwt and jose-jwt libraries.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-dvsekhvalnov-jose2go
Release:        1%{?dist}
Summary:        Go implementation of Javascript Object Signing and Encryption specification
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/jose2go-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

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
