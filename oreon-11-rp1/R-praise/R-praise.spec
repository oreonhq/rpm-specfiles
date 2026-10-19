%global source0_hash 5c035e74fd05dfa59b03afe0d5f4c53fbf34144e175e90c53d09c6baedf5debd
Name:           R-praise
Version:        %R_rpm_version 1.0.0
Release:        1%{?dist}
Summary:        Praise Users
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=praise&version=%{version}#/praise_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Build friendly R packages that praise their users if they have done something
good, or they just need it to feel better.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
