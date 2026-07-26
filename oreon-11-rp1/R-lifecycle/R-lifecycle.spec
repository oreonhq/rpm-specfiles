%global source0_hash 61841e3e6edba056a88355a3f1d6698ab8d5d9cb3c05f2af0ec5a44ab516f8ee

Name:           R-lifecycle
Version:        %R_rpm_version 1.0.5
Release:        %autorelease
Summary:        Manage the Life Cycle of your Package Functions

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Manage the life cycle of your exported functions with shared conventions,
documentation badges, and user-friendly deprecation warnings.

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
