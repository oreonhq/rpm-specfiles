%global source0_hash 45a36e5473ee9400751ef45f5a8fd3a3680df80c902a8f4194b7963c86b26bbb
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/agnivade/levenshtein
Version:                1.1.1
%gometa -f
%global common_description %{expand:
Go implementation to calculate Levenshtein Distance.}
%global godocs          README.md
%global golicenses      License.txt
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go implementation to calculate Levenshtein Distance
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/levenshtein-%{version}.tar.gz
Patch:          0001-Remove-benchmarking-tests.patch
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
