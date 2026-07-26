%global source0_hash 15b5e7f711d53bf41b8687923983b8ef424563aa2f74c5195feb5b1df1aee103

Name:           R-plyr
Version:        %R_rpm_version 1.8.9
Release:        %autorelease
Summary:        Tools for Splitting, Applying and Combining Data

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
A set of tools that solves a common set of problems: you need to break a big
problem down into manageable pieces, operate on each piece and then put all the
pieces back together. For example, you might want to fit a model to each
spatial location or time point in your study, summarise data by panels or
collapse high-dimensional arrays to simpler summary statistics. The development
of plyr has been generously supported by Becton Dickinson.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f plyr/tests/testthat/test-array.r # unconditional suggest, should be fixed
rm -f plyr/tests/testthat/test-rbind.r # unconditional suggest, should be fixed

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
