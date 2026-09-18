%global source0_hash none

Name:           python-jupyter-lsp
Version:        2.3.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Multi-Language Server WebSocket proxy for Jupyter Notebook/Lab server

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/jupyter-lsp/jupyterlab-lsp
Source:         %{pypi_source jupyter_lsp}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'jupyter-lsp' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-jupyter-lsp
Summary:        %{summary}

%description -n python3-jupyter-lsp %_description


%prep
%autosetup -p1 -n jupyter_lsp-%{version}


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


%files -n python3-jupyter-lsp -f %{pyproject_files}

%changelog
%autochangelog
