%global source0_hash 330fef440ffeb842a7dcfffc8303743f1feae83e8d6131078b5a44ff11bc3850

Name:           R-pkgconfig
Version:        %R_rpm_version 2.0.3
Release:        %autorelease
Summary:        Private Configuration for 'R' Packages

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Set configuration options on a per-package basis. Options set by a given
package only apply to that package, other packages are unaffected.

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
