%global source0_hash 1a3a110f0b7809f42fba543c7264421ddec3c8b9f576dcf21df9fe97df307b6e
Name:           R-highlight
Version:        %R_rpm_version 0.5.2
Release:        1%{?dist}
Summary:        R Syntax Highlighter
License:	    GPL-3.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=highlight&version=%{version}#/highlight_%{version}.tar.gz
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Syntax highlighter for R code based on the results of the R parser.
Rendering in HTML and latex markup. Custom Sweave driver performing
syntax highlighting of R code chunks.

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
