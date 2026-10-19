%global source0_hash 3d1c5209e390d25d7c8f19ab38d9d1e094e0ddc14cb734c5f5c3dcbaba79d5e5
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/shiena/ansicolor
Version:                0.1
%gometa
%global common_description %{expand:
Ansicolor library provides color console in Windows as ANSICON for Golang.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Color console in Windows for Golang
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/ansicolor-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

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
