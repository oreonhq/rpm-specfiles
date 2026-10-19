%global source0_hash 5c3d1316e90ffec6ac0b56601147136e767daf4efbd94d669b747e1c3cb54714
%bcond check 0
%global debug_package %{nil}
%global debug_package %{nil}
%global goipath         github.com/Masterminds/semver
Version:                3.5.0
%gometa
%global goaltipaths     github.com/Masterminds/semver/v3
%global common_description %{expand:
The semver package provides the ability to work with Semantic Versions in Go.
Specifically it provides the ability to:
 - Parse semantic versions
 - Sort semantic versions
 - Check if a semantic version fits within a set of constraints
 - Optionally work with a v prefix}
%global golicenses      LICENSE.txt
%global godocs          CHANGELOG.md README.md
%global gosupfiles glide.lock glide.yaml
Name:           %{goname}
Release:        1%{?dist}
Summary:        Work with semantic versions in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/semver-%{version}.tar.gz
Source1:        glide.yaml
Source2:        glide.lock
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
cp %{S:1} %{S:2} .

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
