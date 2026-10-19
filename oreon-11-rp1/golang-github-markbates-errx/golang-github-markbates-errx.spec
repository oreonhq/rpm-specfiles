%global source0_hash adbe12dff4269f0ba7333fd61fe0d0d68420c63e603c3e9a4afdec47e34380e0
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/markbates/errx
Version:                1.1.0
%gometa
%global common_description %{expand:
Errx for Go.}
%global golicenses      LICENSE
%global godocs          SHOULDERS.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Errx for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/errx-%{version}.tar.gz
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
