%global source0_hash 195d14a178b0c7e10f8661c1dcf19e63a01129ac449c3430351518773f4b2c56
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         software.sslmate.com/src/go-pkcs12
%global forgeurl        https://github.com/SSLMate/go-pkcs12
Version:                0.4.0
%gometa -L -f
%global common_description %{expand:
Go library for encoding and decoding PKCS#12 files.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-software-sslmate-src-pkcs12
Release:        1%{?dist}
Summary:        Go library for encoding and decoding PKCS#12 files
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/go-pkcs12-%{version}.tar.gz
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
