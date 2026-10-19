%global source0_hash 0649f2ce39541820daee3ed408d765eddf83db5db639b493561f4e5fbf88efe0
Name:           R-clisymbols
Version:        %R_rpm_version 1.2.0
Release:        1%{?dist}
Summary:        Unicode Symbols at the R Prompt
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=clisymbols&version=%{version}#/clisymbols_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A small subset of Unicode symbols, that are useful when building command line
applications. They fall back to alternatives on terminals that do not support
Unicode. Many symbols were taken from the 'figures' 'npm' package (see
<https://github.com/sindresorhus/figures>).

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
