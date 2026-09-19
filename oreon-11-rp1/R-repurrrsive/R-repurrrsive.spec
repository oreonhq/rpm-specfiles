%global source0_hash a9c109889293a4f2ba1defc198f2c1f2590feb3744105e97f4926808f1717088

Name:           R-repurrrsive
Version:        %R_rpm_version 1.1.0
Release:        %autorelease
Summary:        Examples of Recursive Lists and Nested or Split Data Frames

License:        CC0-1.0
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Recursive lists in the form of R objects, JSON, and XML, for use in teaching
and examples. Examples include color palettes, Game of Thrones characters,
GitHub users and repositories, music collections, and entities from the Star
Wars universe. Data from the gapminder package is also included, as a simple
data frame and in nested and split forms.

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
