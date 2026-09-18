%global source0_hash none

Name:           python-ipykernel
Version:        7.3.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        IPython Kernel for Jupyter

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://ipython.org
Source:         %{pypi_source ipykernel}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ipykernel' generated automatically by pyp2spec.}

Patch:          https://github.com/ipython/ipykernel/commit/a7d66a.patch
Patch:          https://github.com/ipython/ipykernel/pull/1248.patch

%description %_description

%package -n     python3-ipykernel
Summary:        %{summary}

%description -n python3-ipykernel %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-ipykernel cov,docs,pyqt5,pyside6,test


%prep
%autosetup -p1 -n ipykernel-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x cov,docs,pyqt5,pyside6,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-ipykernel -f %{pyproject_files}

%changelog
%autochangelog
