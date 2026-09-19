%global source0_hash db73e62a5c536fd16b6549a61d0dd109eff4f94ac6236c52de53bde2230f81d6

Name:           R-packrat
Version:        %R_rpm_version 0.9.3
Release:        %autorelease
Summary:        Dependency Management System for R Projects

License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Manage the R packages your project depends on in an isolated, portable, and
reproducible way.

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
%R_check \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
