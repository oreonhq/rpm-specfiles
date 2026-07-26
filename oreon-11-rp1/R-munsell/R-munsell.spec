%global source0_hash 03a2fd9ac40766cded96dfe33b143d872d0aaa262a25482ce19161ca959429a6

Name:           R-munsell
Version:        %R_rpm_version 0.5.1
Release:        %autorelease
Summary:        Utilities for Using Munsell Colours

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Provides easy access to, and manipulation of, the Munsell colours.
Provides a mapping between Munsell's original notation (e.g. "5R 5/10")
and hexadecimal strings suitable for use directly in R graphics. Also
provides utilities to explore slices through the Munsell colour tree, to
transform Munsell colours and display colour palettes.

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
