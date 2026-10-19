%global source0_hash 6660b00538ebb0e0ade120371f2a891c692650e9126bd45a805b8f4d65293127
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/jinzhu/now
Version:                1.1.5
%gometa
%global common_description %{expand:
Now is a time toolkit for Go.}
%global golicenses      License
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Time toolkit for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/now-%{version}.tar.gz
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
