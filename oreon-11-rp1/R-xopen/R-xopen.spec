%global source0_hash e3b278b8c324a1aa2650141dd89d01253eea5c2555007422c797915689b29aec
Name:           R-xopen
Version:        %R_rpm_version 1.0.1
Release:        1%{?dist}
Summary:        Open System Files, 'URLs', Anything
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=xopen&version=%{version}#/xopen_%{version}.tar.gz
BuildArch:      noarch
Requires:       /usr/bin/xdg-open
# oreon:deps
BuildRequires:  /usr/bin/xdg-open
BuildRequires:  R-devel
# /oreon:deps
%description
Cross platform solution to open files, directories or 'URLs' with their
associated programs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
# Depend on system executable instead.
rm xopen/inst/xdg-open

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
