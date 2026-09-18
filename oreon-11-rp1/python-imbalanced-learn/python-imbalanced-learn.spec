%global source0_hash none

Name:           python-imbalanced-learn
Version:        0.14.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Toolbox for imbalanced dataset in machine learning

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://imbalanced-learn.org/
Source:         %{pypi_source imbalanced_learn}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'imbalanced-learn' generated automatically by pyp2spec.}

Patch:          fix-scikit-learn-1.8-compat.patch

%description %_description

%package -n     python3-imbalanced-learn
Summary:        %{summary}

%description -n python3-imbalanced-learn %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-imbalanced-learn dev,docs,keras,linters,optional,tensorflow,tests


%prep
%autosetup -p1 -n imbalanced_learn-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,docs,keras,linters,optional,tensorflow,tests


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-imbalanced-learn -f %{pyproject_files}

%changelog
%autochangelog
