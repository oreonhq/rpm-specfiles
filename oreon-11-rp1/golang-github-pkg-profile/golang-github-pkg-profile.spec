%global source0_hash 3688b8af441af9204950860d98807635e6fa5822bc7a1cc95b6b238c47cd38bb
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/pkg/profile
Version:                1.7.0
%gometa
%global common_description %{expand:
Simple profiling support package for Go}
%global golicenses      LICENSE
%global godocs          AUTHORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Simple profiling for Go
License:        BSD-2-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/profile-%{version}.tar.gz
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
