%global source0_hash none

Name:           python-scikit-learn
Version:        1.9.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A set of python modules for machine learning and data mining

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://scikit-learn.org
Source:         %{pypi_source scikit_learn}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'scikit-learn' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-scikit-learn
Summary:        %{summary}

%description -n python3-scikit-learn %_description


%prep
%autosetup -p1 -n scikit_learn-%{version}


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


%files -n python3-scikit-learn -f %{pyproject_files}

%changelog
%autochangelog

