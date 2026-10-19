%global source0_hash 3e74a0685541efb5ea763b92cfd5c859df71c46b0605967a0b5dbb7326e9da69
Name:           R-crayon
Version:        %R_rpm_version 1.5.3
Release:        1%{?dist}
Summary:        Colored Terminal Output
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=crayon&version=%{version}#/crayon_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Colored terminal output on terminals that support 'ANSI' color and highlight
codes. It also works in 'Emacs' 'ESS'. 'ANSI' color support is automatically
detected. Colors and highlighting can be combined and nested. New styles can
also be created easily. This package was inspired by the 'chalk'
'JavaScript' project.

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
