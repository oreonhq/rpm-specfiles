%global source0_hash 8528fa3ba8d04a6e71783f01ba3e1163b5900c6b3c2bc81bad2349e220197f05

Name:           R-RUnit
Version:        %R_rpm_version 0.4.33.1
Release:        %autorelease
Summary:        R Unit test framework

License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}
Patch:          R-RUnit-0.4.25-no-buildroot-path-in-html.patch

BuildArch:      noarch
BuildRequires:  R-devel

%description
R functions implementing a standard Unit Testing framework, with additional
code inspection and report generation tools.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -p1

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
