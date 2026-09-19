%global source0_hash add7a107ff6a3185f68511cfcc45832f018917870eae06a8044f41de84ff0907

Name:           R-bslib
Version:        %R_rpm_version 0.9.0
Release:        %autorelease
Summary:        Custom Bootstrap Sass Themes for shiny and rmarkdown

# See `LICENSE.note` for breakdown.
License:        MIT AND BSD-3-Clause
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Simplifies custom CSS styling of both shiny and rmarkdown via Bootstrap Sass.
Supports both Bootstrap 3 and 4 as well as their various Bootswatch themes. An
interactive widget is also provided for previewing themes in real time.

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
%R_check \--no-examples \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
