%global source0_hash none

Name:           python-enthought-sphinx-theme
Version:        0.7.5
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Sphinx theme for Enthought products

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/enthought/enthought-sphinx-theme
Source:         %{pypi_source enthought_sphinx_theme}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'enthought-sphinx-theme' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-enthought-sphinx-theme
Summary:        %{summary}

%description -n python3-enthought-sphinx-theme %_description


%prep
%autosetup -p1 -n enthought_sphinx_theme-%{version}


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


%files -n python3-enthought-sphinx-theme -f %{pyproject_files}

%changelog
%autochangelog
