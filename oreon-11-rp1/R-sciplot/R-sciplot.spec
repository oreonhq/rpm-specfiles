%global source0_hash 738fa4ddc1c1d20f5467376d9278f6461a405617904b871a378e94ade563ff24
Name:           R-sciplot
Version:        %R_rpm_version 1.2-0
Release:        1%{?dist}
Summary:        Scientific Graphing Functions for Factorial Designs
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=sciplot&version=1.2-0#/sciplot_1.2-0.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A collection of functions that creates graphs with error bars for data collected 
from one-way or higher factorial designs

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
