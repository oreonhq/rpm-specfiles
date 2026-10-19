%global source0_hash ecedeca2b4f27a2a6fa2ba7f1473a5f8c16aaa9f2f9fc7f68bceb5a4d94089ef
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/MaxHalford/halfgone
Version:                0.0.1
%global commit          482157b86ccb239d6172d85b15dd0025c51f605d
%gometa -f
%global common_description %{expand:
Black and white digital halftoning.}
%global golicenses      LICENSE
%global godocs          examples README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Black and white digital halftoning
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/halfgone-%{commit}.tar.gz
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
