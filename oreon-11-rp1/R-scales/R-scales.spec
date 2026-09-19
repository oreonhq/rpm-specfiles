%global source0_hash d55ef5f08c92652d7a95cfa27584024723ab17873f1b2577dd488cb7c883ceee

Name:           R-scales
Version:        %R_rpm_version 1.4.0
Release:        %autorelease
Summary:        Scale Functions for Visualization

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Graphical scales map data to aesthetics, and provide methods for
automatically determining breaks and labels for axes and legends.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f scales/tests/testthat/test-label-date.R # unconditional suggest, should be fixed
rm -f scales/tests/testthat/test-full-seq.R # unconditional suggest, should be fixed

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
