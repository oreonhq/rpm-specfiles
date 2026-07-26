%global source0_hash a9f22335ea39039de25bb27bccd5ff1ffb2b743579b31d150b6b91c9ea81d0b8

Name:           R-brio
Version:        %R_rpm_version 1.1.5
Release:        %autorelease
Summary:        Basic R Input Output

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Functions to handle basic input output, these functions always read and write
UTF-8 (8-bit Unicode Transformation Format) files and provide more explicit
control over line endings.

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
