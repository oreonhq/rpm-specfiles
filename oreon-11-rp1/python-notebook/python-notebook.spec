%global source0_hash none

Name:           python-notebook
Version:        7.6.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Jupyter Notebook - A web-based notebook environment for interactive computing

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/jupyter/notebook
Source:         %{pypi_source notebook}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'notebook' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-notebook
Summary:        %{summary}

%description -n python3-notebook %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-notebook dev,docs,test


%prep
%autosetup -p1 -n notebook-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,docs,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-notebook -f %{pyproject_files}
%{_bindir}/jupyter-notebook

%changelog
%autochangelog
