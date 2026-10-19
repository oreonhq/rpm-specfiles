%global source0_hash cdbdd5ca01a1c82f98f57c0a73b05371527e47acad242fb6801adecd71483b1c
%ifarch x86_64
%bcond check 0
%endif
%global debug_package %{nil}
%global goipath         github.com/mdlayher/genetlink
Version:                1.4.0
%gometa -f
%global common_description %{expand:
Package genetlink implements generic netlink interactions and data types. MIT
Licensed.}
%global golicenses      LICENSE.md
%global godocs          CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Package genetlink implements generic netlink interactions and data types. MIT Licensed
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/genetlink-%{version}.tar.gz
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
