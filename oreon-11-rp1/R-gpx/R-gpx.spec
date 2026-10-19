%global source0_hash b1582856c477fed3adfd18510209b79bfbb70e99df5b4e2848a6c6bc6c1d2b75
Name:           R-gpx
Version:        %R_rpm_version 1.1.0
Release:        1%{?dist}
Summary:        Process GPX Files into R Data Structures
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=gpx&version=%{version}#/gpx_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Process open standard GPX files into data.frames
for further use and analysis in R.

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
