%global source0_hash 26452207db6dd62b3820008265cc14ad5c576286172b69d7db06238ba34a43bd
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/go-task/slim-sprig
Version:                3.2.0
%global commit          afa1e2071829e4db655eb448d6c7c16eb0bc5766
%gometa
%global common_description %{expand:
Useful template functions for Go templates.}
%global golicenses      LICENSE.txt
%global godocs          docs CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Useful template functions for Go templates
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/slim-sprig-%{commit}.tar.gz
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

rm -vf network_test.go
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
