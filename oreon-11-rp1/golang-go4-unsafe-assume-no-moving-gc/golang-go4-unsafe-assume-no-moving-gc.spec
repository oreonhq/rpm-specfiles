%global source0_hash 90a4022bf300ba6ff21945efda84dba61989f21a45cb9ab340096ac9ce96fd14
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         go4.org/unsafe/assume-no-moving-gc
%global forgeurl        https://github.com/go4org/unsafe-assume-no-moving-gc
%global commit          b99613f794b6b2f6d80da53bb131c5c98ea2fdd2
%global date            20231121
%gometa -L -f
%global common_description %{expand:
For playing unsafe games with Go's runtime garbage collector.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-go4-unsafe-assume-no-moving-gc
Version:        0
Release:        1%{?dist}
Summary:        For playing unsafe games with Go's runtime garbage collector
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{commit}/unsafe-assume-no-moving-gc-%{commit}.tar.gz
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
