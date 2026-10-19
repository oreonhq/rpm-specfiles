%global source0_hash cfe258c20d71ac4dbf0f716a23ed00c332b7f281180651e2a67ad40a8b0772cc
%bcond check 0
%global debug_package %{nil}
%global goipath         go.uber.org/atomic
%global forgeurl        https://github.com/uber-go/atomic
Version:                1.11.0
%gometa
%global common_description %{expand:
Wrapper types for sync/atomic which enforce atomic access.}
%global golicenses      LICENSE.txt
%global godocs          CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Wrapper types for sync/atomic which enforce atomic access
License:        MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/atomic-%{version}.tar.gz
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
