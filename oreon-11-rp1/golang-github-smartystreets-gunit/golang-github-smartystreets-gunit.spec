%global source0_hash fcdbb67d8360514f67027b991046c58e197f6c3c4258db07a62fe60f3fd64fa7
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/smartystreets/gunit
Version:                2.2.0
%gometa
%global common_description %{expand:
xUnit-style test fixture adapter for Go test.}
%global golicenses      LICENSE.md
%global godocs          CONTRIBUTING.md README.md advanced_examples basic_examples
Name:           %{goname}
Release:        1%{?dist}
Summary:        xUnit-style test fixture adapter for Go test
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/gunit-%{version}.tar.gz
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

%gocheck -d .
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
