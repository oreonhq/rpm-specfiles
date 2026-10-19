%global source0_hash 1cdf6f5e2448dd4f7892c504d9dc89e31e13c3904b340c5aebf9d68d39729d78
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/zeebo/assert
Version:                1.3.1
%gometa
%global common_description %{expand:
Helpers for tests.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Helpers for tests
License:        CC0-1.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/assert-%{version}.tar.gz
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
