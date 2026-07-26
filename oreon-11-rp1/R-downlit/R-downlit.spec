%global source0_hash b696ce388a804738b44eb1ceb0e3f0531b309ea91408f40a0cb43c63541b658b

Name:           R-downlit
Version:        %R_rpm_version 0.4.5
Release:        %autorelease
Summary:        Syntax Highlighting and Automatic Linking

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Syntax highlighting of R code, specifically designed for the needs of RMarkdown
packages like pkgdown, hugodown, and bookdown. It includes linking of function
calls to their documentation on the web, and automatic translation of ANSI
escapes in output to the equivalent HTML.

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
