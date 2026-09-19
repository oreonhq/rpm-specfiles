%global source0_hash da80259d5feb5701db24a8507b36f38ba9fd01e3b460e45edc378cb6930933e1

Name:           R-rversions
Version:        %R_rpm_version 3.0.0
Release:        %autorelease
Summary:        Query 'R' Versions, Including 'r-release' and 'r-oldrel'

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Query the main 'R' 'SVN' repository to find the versions 'r-release' and
'r-oldrel' refer to, and also all previous 'R' versions and their release
dates.

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
