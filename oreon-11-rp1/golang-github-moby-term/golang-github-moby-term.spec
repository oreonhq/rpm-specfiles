%global source0_hash 312893ff882f1fcb40aa9e99743f82c4a08cbc90551a2f4b398a2e76a7706f5f
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/moby/term
%global commit          1aeaba8785877a66f57739be9fccb6f5cfab429e
%gometa
%global common_description %{expand:
Go utilities for dealing with terminals
Package term provides structures and helper functions to work with terminal
(state, sizes).}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        None
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/term-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

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
