%global source0_hash c96534779554e3f0b3e2af04739e730519fda4d4476029ebbeeb84be304b8dff
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/ianbruene/go-difflib
Version:                1.3.0
%gometa
%global common_description %{expand:
Go-difflib is an as yet partial port of python 3's difflib package.
The following publicly visible classes and functions have been ported:
 - SequenceMatcher
 - Differ
 - unified_diff()
 - context_diff()}
%global golicenses      LICENSE
Name:           %{goname}
Release:        1%{?dist}
Summary:        Difflib package's Go implementation
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-difflib-%{version}.tar.gz
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
