%global source0_hash aad33227b648bad50412849d7e0fed00fd07f1d1d4a14fa015b4b9f939b04a11

Name:           R-randomForest
Version:        %R_rpm_version 4.7-1.2
Release:        %autorelease
Summary:        Breiman and Cutler's Random Forests for Classification and Regression

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Classification and regression based on a forest of trees using random
inputs, based on Breiman (2001) <DOI:10.1023/A:1010933404324>.

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
