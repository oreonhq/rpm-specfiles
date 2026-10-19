%global source0_hash 30c7b31f47371a8f5af3d573d096200218cfcb39234306ce8ef999c7ba1fda2a
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/djherbis/atime
Version:                1.1.0
%gometa
%global common_description %{expand:
Access Times for files in Golang}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Access Times for files
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/atime-%{version}.tar.gz
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
