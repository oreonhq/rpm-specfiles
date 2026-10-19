%global source0_hash da38706603fce9345062d156e1d2ac6b1598108675d305cf2220bd12af4bd413
%global debug_package %{nil}
%bcond check 1
%global goipath         github.com/montanaflynn/stats
Version:                0.12.7
%gometa
%global common_description %{expand:
A well tested and comprehensive Golang statistics library package with no
dependencies.}
%global golicenses      LICENSE
%global godocs          examples CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Well tested and comprehensive Golang statistics library package
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/stats-%{version}.tar.gz
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
