%global source0_hash b12964c46fcd77d235e98af10586e103e50a4109affa9ede547c9ee75cffca06
Name:           R-lintr
Version:        %R_rpm_version 3.3.0-1
Release:        1%{?dist}
Summary:        A 'Linter' for R Code
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=lintr&version=3.3.0-1#/lintr_3.3.0-1.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Checks adherence to a given style, syntax errors and possible semantic
issues.  Supports on the fly checking of R code edited with 'RStudio IDE',
'Emacs', 'Vim', 'Sublime Text' and 'Atom'.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-tests
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
