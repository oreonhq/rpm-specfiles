%global source0_hash 8f5d8dcfc7ac4ff1187f88480d46e65eec8740746837ca0ff2b7be5038fd250d
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/cloudflare/circl
Version:                1.6.5
%gometa -L -f
%global common_description %{expand:
CIRCL: Cloudflare Interoperable Reusable Cryptographic Library.}
%global golicenses      LICENSE ecc-p384-LICENSE
%global godocs          README.md
Name:           golang-github-cloudflare-circl
Release:        1%{?dist}
Summary:        CIRCL: Cloudflare Interoperable Reusable Cryptographic Library
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/circl-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

# This package has arch specific files, so it cannot be noarch like the rest of
# the golang-*-devel packages. %%gopkg does not currently support this usecase,
# so we create a manual subpackage definition
%package        devel
Summary:        %{summary}
BuildRequires:  go-rpm-macros
%description    devel %{common_description}

This package contains the source code needed for building packages that
reference the following Go import paths:
 – %{goipath}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%if %{without bootstrap}
%install
%gopkginstall
mv ecc/p384/LICENSE ecc-p384-LICENSE
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{without bootstrap}
%if %{with check}
%check

%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n golang-github-cloudflare-circl-devel -f %{oreon_filedir}/golang-github-cloudflare-circl-devel.list

%changelog

%autochangelog
%endif
