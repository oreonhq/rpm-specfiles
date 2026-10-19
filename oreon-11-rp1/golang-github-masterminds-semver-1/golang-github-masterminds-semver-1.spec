%global source0_hash c9140eddfb03dc862f826e7761561260b9a840afa7519cc0919e89a43b5be5ba
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/Masterminds/semver
Version:                1.5.0
%gometa
%global goname          golang-github-masterminds-semver-1
%global godevelname     golang-github-masterminds-semver-1-devel
%global common_description %{expand:
The Semver package provides the ability to work with Semantic Versions in Go.
Specifically it provides the ability to:
 - Parse semantic versions
 - Sort semantic versions
 - Check if a semantic version fits within a set of constraints
 - Optionally work with a v prefix}
%global golicenses      LICENSE.txt
%global godocs          CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Work with Semantic Versions in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/semver-%{version}.tar.gz
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
