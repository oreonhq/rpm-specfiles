%global source0_hash b9e081e1edd157e0699727bd720c7390a80abbb44e2b067a8754e3825f5edb38
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/clbanning/x2j
Version:                1.1
%global tag             1.1
%gometa
%global common_description %{expand:
Unmarshal an anonymous xml doc to map[string]interface{} and json, and extract
values (using wildcards, if necessary).}
%global golicenses      LICENSE
%global godocs          examples README
Name:           %{goname}
Release:        1%{?dist}
Summary:        Unmarshal an anonymous xml doc to map[string]interface{} and json
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{version}/x2j-%{version}.tar.gz
Patch0:         0001-Remove-redundant-newlines-in-Println-statement.patch
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%patch -P0 -p1

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
