%global source0_hash b22605ad3b20d460308d8c9c18116e56c4d6ff10577608eaf58802998171f099
Name:           R-debugme
Version:        %R_rpm_version 1.2.0
Release:        1%{?dist}
Summary:        Debug R Packages
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=debugme&version=%{version}#/debugme_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Specify debug messages as special string constants, and control debugging
of packages via environment variables.

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
