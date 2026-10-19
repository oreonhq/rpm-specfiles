%global source0_hash ea2b079b894de85c3ab12088c9c52aec06432245047a961d5b4b8aa6889f9276
Name:           R-progress
Version:        %R_rpm_version 1.2.3
Release:        1%{?dist}
Summary:        Terminal Progress Bars
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=progress&version=%{version}#/progress_%{version}.tar.gz
BuildArch:      noarch
Obsoletes:      %{name}-devel <= 1.2.3
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Configurable Progress bars, they may include percentage, elapsed time, and/or
the estimated completion time. They work in terminals, in Emacs ESS, RStudio,
Windows Rgui and the macOS R.app. The package also provides a C++ API, that
works with or without Rcpp.

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
