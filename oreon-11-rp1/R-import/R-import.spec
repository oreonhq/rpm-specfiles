%global source0_hash 0f18a1e952f96c8a577c4a169089e28b3ba8838c7ecce7d0fcf0bc2821ad0745

Name:           R-import
Version:        %R_rpm_version 1.3.4
Release:        %autorelease
Summary:        An Import Mechanism for R

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Alternative mechanism for importing objects from packages and R modules.
The syntax allows for importing multiple objects with a single command in
an expressive way. The import package bridges some of the gap between using
library (or require) and direct (single-object) imports. Furthermore the
imported objects are not placed in the current environment.

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
