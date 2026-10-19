%global source0_hash 03928a9385085de9dc7cecc809eed26839a8073cd74bd34c25abbf082cbd9867
Name:           R-rprintf
Version:        %R_rpm_version 0.2.1
Release:        1%{?dist}
Summary:        Adaptive Builder for Formatted Strings
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=rprintf&version=%{version}#/rprintf_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Provides a set of functions to facilitate building formatted strings under
various replacement rules: C-style formatting, variable-based formatting,
and number-based formatting. C-style formatting is basically identical to
built-in function 'sprintf'. Variable-based formatting allows users to put
variable names in a formatted string which will be replaced by variable
values. Number-based formatting allows users to use index numbers to
represent the corresponding argument value to appear in the string.

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
