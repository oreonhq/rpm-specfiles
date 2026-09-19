%global source0_hash none

Name:           python-sphinx-autoapi
Version:        3.8.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Sphinx API documentation generator

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            http://github.com/readthedocs/sphinx-autoapi
Source:         %{pypi_source sphinx_autoapi}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sphinx-autoapi' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-sphinx-autoapi
Summary:        %{summary}

%description -n python3-sphinx-autoapi %_description


%prep
%autosetup -p1 -n sphinx_autoapi-%{version}


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


%files -n python3-sphinx-autoapi -f %{pyproject_files}

%changelog
%autochangelog
