%global source0_hash 5daf8e0e5f4b4b0072309e45ddf887901fa5edda06f8d44c73f42cfe5ba68d7d
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/go-logfmt/logfmt
Version:                0.6.1
%gometa -L -f
%global common_description %{expand:
Package logfmt marshals and unmarshals logfmt messages.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md
Name:           golang-github-logfmt
Release:        1%{?dist}
Summary:        Package logfmt marshals and unmarshals logfmt messages
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/logfmt-%{version}.tar.gz
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
