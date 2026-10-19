%global source0_hash 6ed0c5a0c62a89ec4bc3efdec255be3f61f0d78f89cc394d03999b82e07ab94d
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/fsnotify/fsnotify
Version:                1.10.1
%gometa -L -f
%global common_description %{expand:
Cross-platform file system notifications for Go.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md CONTRIBUTING.md README.md
Name:           golang-github-fsnotify
Release:        1%{?dist}
Summary:        Cross-platform file system notifications for Go
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/fsnotify-%{version}.tar.gz
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
