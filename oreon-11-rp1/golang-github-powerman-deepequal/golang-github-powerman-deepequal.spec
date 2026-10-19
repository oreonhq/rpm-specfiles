%global source0_hash dac9d498c41ae3ad0ddb4d48b59d05b3acd80616cbf905564dd94bf08a0fd1dd
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/powerman/deepequal
Version:                0.1.0
%gometa
%global common_description %{expand:
Go package with improved reflect.DeepEqual.}
%global golicenses      LICENSE LICENSE-go
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go package with improved reflect.DeepEqual
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/deepequal-%{version}.tar.gz
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
