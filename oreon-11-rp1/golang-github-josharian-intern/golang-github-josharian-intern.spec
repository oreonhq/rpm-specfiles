%global source0_hash 7c7df6e792ed5db0b1a63c8ec74236b70958ad36c9fe5a02b52b1a418b177b5e
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/josharian/intern
Version:                1.0.0
%gometa
%global common_description %{expand:
Intern Go strings.}
%global golicenses      license.md
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Intern Go strings
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/intern-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

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
