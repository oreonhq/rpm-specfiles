%global source0_hash none

Name:           python-metakernel
Version:        1.0.7
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A Jupyter/IPython Kernel base class in Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/Calysto/metakernel
Source:         %{pypi_source metakernel}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'metakernel' generated automatically by pyp2spec.}

Patch0:		0001-Clear-PS0-in-bash-REPL-wrapper.patch

%description %_description

%package -n     python3-metakernel
Summary:        %{summary}

%description -n python3-metakernel %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-metakernel activity,parallel


%prep
%autosetup -p1 -n metakernel-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x activity,parallel


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-metakernel -f %{pyproject_files}

%changelog
%autochangelog
