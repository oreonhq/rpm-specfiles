%global source0_hash 600bb093f443579ecf7ee6e4baf0ec4405d6d592d3bf0ce09206d5de52658246
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/sebdah/goldie
Version:                1.0.0
%gometa -f
%global goname %{goname}-1
%global godevelname %{goname}-devel
%global common_description %{expand:
Golden file testing for Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Golden file testing for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/goldie-%{version}.tar.gz
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
