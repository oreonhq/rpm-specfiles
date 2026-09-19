%global source0_hash none

Name:           python-nbformat
Version:        5.11.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        The Jupyter Notebook format

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://jupyter.org
Source:         %{pypi_source nbformat}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'nbformat' generated automatically by pyp2spec.}

Patch0:         nbformat-build-test.patch
Patch1:         https://github.com/jupyter/nbformat/pull/408.patch

%description %_description

%package -n     python3-nbformat
Summary:        %{summary}

%description -n python3-nbformat %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-nbformat docs,test


%prep
%autosetup -p1 -n nbformat-%{version}


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


%files -n python3-nbformat -f %{pyproject_files}
%{_bindir}/jupyter-trust

%changelog
%autochangelog
