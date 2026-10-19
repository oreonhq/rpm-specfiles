%global source0_hash 66bbacae9a6ecdc899c486f2fdfd828186e50e8600a000486779284edb7b0c37
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/antihax/optional
Version:                1.0.0
%gometa
%global common_description %{expand:
Optional parameters for Go.}
%global golicenses      LICENSE
Name:           %{goname}
Release:        1%{?dist}
Summary:        Optional parameters for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/optional-%{version}.tar.gz
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
