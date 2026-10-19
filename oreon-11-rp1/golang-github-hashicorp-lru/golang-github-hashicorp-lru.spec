%global source0_hash 312697d0bf6e6bb44e66a94b2a8a07955edf89af10b09e69b5a9101d30ad5149
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/hashicorp/golang-lru
Version:                2.0.7
%gometa
%global common_description %{expand:
This provides the lru package which implements a fixed-size thread safe LRU
cache. It is based on the cache in Groupcache.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Golang lru cache
License:        MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/golang-lru-%{version}.tar.gz
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
