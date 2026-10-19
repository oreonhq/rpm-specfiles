%global source0_hash 89b9f6135110f186a63944b9a9d74acc5caf655abd2afa3540aa3d1a28919e9f
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/Masterminds/vcs
Version:                1.13.3
%gometa
%global common_description %{expand:
Package Vcs provides the ability to work with varying version control systems
(VCS), also known as source control systems (SCM) though the same interface.}
%global golicenses      LICENSE.txt
%global godocs          CHANGELOG.md README.md
%global gosupfiles      glide.lock glide.yaml
Name:           %{goname}
Release:        1%{?dist}
Summary:        VCS Repo management through a common interface in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/vcs-%{version}.tar.gz
Source1:        glide.yaml
Source2:        glide.lock
# oreon:deps
BuildRequires:  bzr
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

%gocheck -d .
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
