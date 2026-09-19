%global source0_hash none

Name:           python-pandas-datareader
Version:        0.11.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Pandas-compatible data readers. Formerly a component of pandas.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://pandas.pydata.org
Source:         %{pypi_source pandas_datareader}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pandas-datareader' generated automatically by pyp2spec.}

Patch: pandas-datareader-python312.patch

%description %_description

%package -n     python3-pandas-datareader
Summary:        %{summary}

%description -n python3-pandas-datareader %_description


%prep
%autosetup -p1 -n pandas_datareader-%{version}


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


%files -n python3-pandas-datareader -f %{pyproject_files}

%changelog
%autochangelog
