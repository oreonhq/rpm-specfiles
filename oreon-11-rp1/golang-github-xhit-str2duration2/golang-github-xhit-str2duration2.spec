%global source0_hash 6f2e676f5ca8fd54179d9b0c8eb3d51433dcd7c354ac4046fc1f54529c9d101a
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/xhit/go-str2duration/v2
Version:                2.1.0
%gometa -L -f
%global common_description %{expand:
Convert string to duration in golang.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-xhit-str2duration2
Release:        1%{?dist}
Summary:        Convert string to duration in golang
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://github.com/xhit/go-str2duration/archive/v%{version}/go-str2duration-%{version}.tar.gz
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
