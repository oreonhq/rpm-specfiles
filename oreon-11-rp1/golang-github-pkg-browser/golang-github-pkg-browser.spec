%global source0_hash baba47802d2e32b1405bb8c6357089ac41e73f9c048ca81f49caa7a3ba5d7223
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/pkg/browser
%global commit          0426ae3fba23d90b7f89ec6bef10e9c3ca607212
%gometa
%global common_description %{expand:
Helpers to open files, readers, and urls in a browser}
%global golicenses      LICENSE
%global godocs          examples README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Helpers to open files, readers, and urls in a browser
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/browser-%{commit}.tar.gz
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
