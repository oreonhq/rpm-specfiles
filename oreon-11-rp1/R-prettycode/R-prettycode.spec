%global source0_hash 4f877bef2d4ff7771a3fa0368c9b85ef058b4c06ff9c18c31d827d3d0e4cd0c5
Name:           R-prettycode
Version:        %R_rpm_version 1.1.0
Release:        1%{?dist}
Summary:        Pretty Print R Code in the Terminal
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=prettycode&version=%{version}#/prettycode_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Replace the standard print method for functions with one that performs syntax
highlighting, using ANSI colors, if the terminal supports them.

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
