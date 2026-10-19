%global source0_hash 54468da73dd78fc9e7c565c41cfe3331802c2134b2e61a9ad197215317092f26
Name:           R-desc
Version:        %R_rpm_version 1.4.3
Release:        1%{?dist}
Summary:        Manipulate DESCRIPTION Files
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=desc&version=%{version}#/desc_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Tools to read, write, create, and manipulate DESCRIPTION files. It is
intended for packages that create or manipulate other packages.

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
