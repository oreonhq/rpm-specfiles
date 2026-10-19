%global source0_hash 2b65cd604f4f608002c73f651cfddaa889b04aec33ba77c20b44fe1f0c7f452b
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/google/safehtml
Version:                0.1.0
%gometa -L -f
%global common_description %{expand:
Safe HTML for Go.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md
Name:           golang-github-google-safehtml
Release:        1%{?dist}
Summary:        Safe HTML for Go
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/safehtml-%{version}.tar.gz
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
