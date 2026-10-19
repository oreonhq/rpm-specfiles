%global source0_hash 186da1d21c3ac58699eb7bf5602bdf19944fee0d4c647076a4ebb22e9b69f418
Name:           R-ggplot2movies
Version:        %R_rpm_version 0.0.1
Release:        1%{?dist}
Summary:        Movies Data
License:        GPL-3.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=ggplot2movies&version=%{version}#/ggplot2movies_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A dataset about movies. This was previously contained in ggplot2, but has been
moved its own package to reduce the download size of ggplot2.

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
