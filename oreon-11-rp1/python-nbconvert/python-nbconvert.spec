%global source0_hash none

Name:           python-nbconvert
Version:        7.17.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Convert Jupyter Notebooks _.ipynb files_ to other formats.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://jupyter.org
Source:         %{pypi_source nbconvert}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'nbconvert' generated automatically by pyp2spec.}

Patch1:         backport-mistune-3.1.0-support.patch

%description %_description

%package -n     python3-nbconvert
Summary:        %{summary}

%description -n python3-nbconvert %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-nbconvert all,docs,qtpdf,qtpng,serve,test,webpdf


%prep
%autosetup -p1 -n nbconvert-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all,docs,qtpdf,qtpng,serve,test,webpdf


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-nbconvert -f %{pyproject_files}
%{_bindir}/jupyter-dejavu
%{_bindir}/jupyter-nbconvert

%changelog
%autochangelog
