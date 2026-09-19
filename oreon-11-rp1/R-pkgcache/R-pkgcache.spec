%global source0_hash 13183ca5b21450e4190b4f7d571b2d8ce9d9e84823916b04f1d28407cf389e02

Name:           R-pkgcache
Version:        %R_rpm_version 2.2.4
Release:        %autorelease
Summary:        Cache 'CRAN'-Like Metadata and R Packages

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Metadata and package cache for CRAN-like repositories. This is a utility
package to be used by package management tools that want to take advantage
of caching.

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
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
