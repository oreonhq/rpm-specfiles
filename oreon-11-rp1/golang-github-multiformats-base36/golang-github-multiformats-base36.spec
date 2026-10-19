%global source0_hash e1ebd02850c99a87a103fa4a11528493e4b18939a363848937bd0001928f99d6
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/multiformats/go-base36
Version:                0.1.0
%gometa
%global common_description %{expand:
Optimized codec for []byte <=> base36 string conversion.}
%global golicenses      LICENSE.md
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Optimized codec for []byte <=> base36 string conversion
License:        Apache-2.0 OR LicenseRef-Callaway-MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-base36-%{version}.tar.gz
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
