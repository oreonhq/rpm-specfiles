%global source0_hash e37517fcad5249d7b1918a8207c04f40b2ab9f41267bea2af3a73a1f934a0a10
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/clbanning/mxj
Version:                2.5.5
%gometa
%global common_description %{expand:
Decode / encode XML to/from map[string]interface{} (or JSON); extract values
with dot-notation paths and wildcards.  Replaces x2j and j2x packages.}
%global golicenses      LICENSE x2j-wrapper/LICENSE
%global godocs          examples readme.md x2j-wrapper/README
Name:           %{goname}
Release:        1%{?dist}
Summary:        Decode / encode XML to/from map[string]interface{} (or JSON)
License:        BSD and MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/mxj-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
rm -rf deprecate/

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
