%global source0_hash ff70e539fd919da757a2f3a530a053e7577cb4d7e2824fc1058d3abbefbb523e
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/json-iterator/go
Version:                1.1.12
%gometa
%global common_description %{expand:
A high-performance 100% compatible drop-in replacement of "encoding/json".}
%global golicenses      LICENSE
%global godocs          README.md fuzzy_mode_convert_table.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        A high-performance 100% compatible drop-in replacement of "encoding/json"
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-%{version}.tar.gz
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
