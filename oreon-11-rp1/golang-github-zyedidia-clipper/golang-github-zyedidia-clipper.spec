%global source0_hash c55be53467bb557eaf067e168ac4a0e5b032f3ab5a09d96979ca42a1203f6359
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/zyedidia/clipper
Version:                0.1.0
%gometa -f
%global common_description %{expand:
Cross-platform clipboard access in Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Cross-platform clipboard access in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/clipper-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
# winapi.go is under a different license, so remove it to keep our license
# field simple.
rm winapi.go LICENSE-EXTRA

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
