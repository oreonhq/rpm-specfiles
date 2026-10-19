%global source0_hash c5fa1f3b2c687c6157507fe62a1e0aff50d0ca974138c98ded8160bea39fb06c
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/tomb.v1
%global forgeurl        https://github.com/go-tomb/tomb
Version:                1
%global commit          dd632973f1e7218eb1089048e0798ec9ae7dceb8
%gometa
%global common_description %{expand:
The Tomb package handles clean goroutine tracking and termination.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Clean goroutine termination in the Go language
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{commit}/tomb-%{commit}.tar.gz
Patch:          https://patch-diff.githubusercontent.com/raw/go-tomb/tomb/pull/8.patch
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

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
