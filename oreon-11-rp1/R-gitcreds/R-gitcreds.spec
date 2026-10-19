%global source0_hash 41c6abcca5635062b123ffb5af2794770eca5ebd97b05c5a64b24fa1c803c75d
Name:           R-gitcreds
Version:        %R_rpm_version 0.1.2
Release:        1%{?dist}
Summary:        Query 'git' Credentials from 'R'
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=gitcreds&version=%{version}#/gitcreds_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Query, set, delete credentials from the git credential store. Manage
GitHub tokens and other git credentials. This package is to be used by
other packages that need to authenticate to GitHub and/or other git
repositories.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-tests
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
