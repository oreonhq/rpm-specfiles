%global source0_hash 5006d8626ff22ad2c584b0ab09b6f20f8013b46467381519b80f9c037ad8c2b0
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/cenkalti/backoff/v4
Version:                4.3.0
%gometa -L -f
%global common_description %{expand:
The exponential backoff algorithm in Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-cenkalti-backoff4
Release:        1%{?dist}
Summary:        The exponential backoff algorithm in Go
License:        MIT
URL:            %{gourl}
Source0:        https://github.com/cenkalti/backoff/archive/v%{version}/backoff-%{version}.tar.gz
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
