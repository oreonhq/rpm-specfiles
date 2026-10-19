%global source0_hash f5f0b13b15e9afce536dfa2afa7b2c93ea23160cc238825dd15b406ee2992346
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/d4l3k/go-bfloat16
%global commit          690c3bdd05f13e639d272b6b05061ea57e639d2d
%global date            20211004
%gometa -L -f
%global common_description %{expand:
Bfloat16 conversion utilities for Go/Golang.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-d4l3k-bfloat16
Version:        0
Release:        1%{?dist}
Summary:        Bfloat16 conversion utilities for Go/Golang
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-bfloat16-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A

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
