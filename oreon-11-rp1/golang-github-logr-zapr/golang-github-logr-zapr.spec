%global source0_hash 37a516aa30dd42af8be6edd8ab8ba3684b197374f763f0655078bfe9fb2e44cc
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/go-logr/zapr
Version:                1.3.0
%gometa
%global common_description %{expand:
A logr implementation using Zap.}
%global golicenses      LICENSE
%global godocs          example README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        A logr implementation using Zap
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/zapr-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/stretchr/testify)
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
