%global source0_hash none

Name:           python-jupyter-core
Version:        5.9.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Jupyter core package. A base package on which Jupyter projects rely.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://jupyter.org
Source:         %{pypi_source jupyter_core}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'jupyter-core' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-jupyter-core
Summary:        %{summary}

%description -n python3-jupyter-core %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-jupyter-core docs,test


%prep
%autosetup -p1 -n jupyter_core-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-jupyter-core -f %{pyproject_files}
%{_bindir}/jupyter
%{_bindir}/jupyter-migrate
%{_bindir}/jupyter-troubleshoot

%changelog
%autochangelog
