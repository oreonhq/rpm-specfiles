%global source0_hash none

Name:           python-genshi
Version:        0.7.11
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A toolkit for generation of output for the web

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/edgewall/genshi
Source:         %{pypi_source genshi}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'genshi' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-genshi
Summary:        %{summary}

%description -n python3-genshi %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-genshi i18n,plugin


%prep
%autosetup -p1 -n genshi-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x i18n,plugin


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-genshi -f %{pyproject_files}

%changelog
%autochangelog
