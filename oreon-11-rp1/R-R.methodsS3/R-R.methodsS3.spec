%global source0_hash 822d5e61dad4c91e8883be2b38d7b89f87492046d0fe345704eb5d2658927c2e

Name:           R-R.methodsS3
Version:        %R_rpm_version 1.8.2
Release:        %autorelease
Summary:        S3 Methods Simplified

License:        LGPL-2.1-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Methods that simplify the setup of S3 generic functions and S3 methods.  Major
effort has been made in making definition of methods as simple as possible with
a minimum of maintenance for package developers.  For example, generic
functions are created automatically, if missing, and naming conflict are
automatically solved, if possible.  The method setMethodS3() is a good start
for those who in the future may want to migrate to S4.  This is a
cross-platform package implemented in pure R that generates standard S3
methods.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
sed -i 's/\r$//' R.methodsS3/inst/CITATION

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
