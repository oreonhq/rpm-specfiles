%global source0_hash 530a7435640e86c34db16bcc4c8a38b5046ac79512a86e7b97f66a9d57813cbc

Name:           R-Biobase
Version:        %R_rpm_version 2.70.0
Release:        %autorelease
Summary:        Base functions for Bioconductor

License:        Artistic-2.0
URL:            %{bioc_url}
Source:         %{bioc_source}

BuildRequires:  R-devel

%description
Base functions for Bioconductor (bioconductor.org). Biobase provides
functions that are needed by many other Bioconductor packages or which
replace R functions.

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
