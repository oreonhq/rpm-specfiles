%global source0_hash none

Name:           python-conda-sphinx-theme
Version:        0.4.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Conda theme for Sphinx

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/conda-incubator/conda-sphinx-theme/
Source:         %{pypi_source conda_sphinx_theme}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'conda-sphinx-theme' generated automatically by pyp2spec.}

Patch:          python-conda-sphinx-theme-fonts.patch

%description %_description

%package -n     python3-conda-sphinx-theme
Summary:        %{summary}

%description -n python3-conda-sphinx-theme %_description


%prep
%autosetup -p1 -n conda_sphinx_theme-%{version}


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


%files -n python3-conda-sphinx-theme -f %{pyproject_files}

%changelog
%autochangelog
