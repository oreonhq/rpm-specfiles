%global source0_hash efc525f797b62b3740d06c6fa8202593ab5aa4fc1edeefb76b6eb9be89e87b94

Name:           R-hms
Version:        %R_rpm_version 1.1.4
Release:        %autorelease
Summary:        Pretty Time of Day

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Implements an S3 class for storing and formatting time-of-day values, based
on the 'difftime' class.

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
%R_check

%files -f %{R_files}

%changelog
%autochangelog
