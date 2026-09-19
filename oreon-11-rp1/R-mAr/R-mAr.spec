%global source0_hash adf8fc0d4a3a81211dc5ac50c87c5dcb7b5f1b77c7d1f5991c2b849da6503afb

Name:           R-mAr
Version:        %R_rpm_version 1.2-0
Release:        %autorelease
Summary:        R module to evaluate functions for multivariate AutoRegressive analysis

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
R package:
An R add-on package for estimation of multivariate AR models through a
computationally-efficient stepwise least-squares algorithm (Neumaier
and Schneider, 2001); the procedure is of particular interest for
high-dimensional data without missing values such as geophysical
fields.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
