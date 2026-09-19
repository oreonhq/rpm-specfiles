%global source0_hash none

Name:           python-multiregex
Version:        2.0.4
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Quickly match many regexes against a string. Provides 2-10x speedups over naïve regex matching.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/quantco/multiregex
Source:         %{pypi_source multiregex}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'multiregex' generated automatically by pyp2spec.}

Patch:          https://github.com/Quantco/multiregex/pull/100.patch

%description %_description

%package -n     python3-multiregex
Summary:        %{summary}

%description -n python3-multiregex %_description


%prep
%autosetup -p1 -n multiregex-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-multiregex -f %{pyproject_files}

%changelog
%autochangelog
