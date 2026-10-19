%global source0_hash ba59a69fcaea38ec40470cac08620dd2cca1980355d9b10e90e37b3b3ac2eb46
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/agext/levenshtein
Version:                1.2.3
%gometa
%global common_description %{expand:
Levenshtein distance and similarity metrics with customizable edit costs and
Winkler-like bonus for common prefix.}
%global golicenses      LICENSE NOTICE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Levenshtein distance and similarity metrics
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/levenshtein-%{version}.tar.gz
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
