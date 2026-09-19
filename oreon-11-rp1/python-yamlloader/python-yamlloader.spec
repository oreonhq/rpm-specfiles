%global source0_hash none

Name:           python-yamlloader
Version:        1.6.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Ordered YAML loader and dumper for PyYAML.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/Phynix/yamlloader
Source:         %{pypi_source yamlloader}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'yamlloader' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-yamlloader
Summary:        %{summary}

%description -n python3-yamlloader %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-yamlloader dev,doc,test


%prep
%autosetup -p1 -n yamlloader-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,doc,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-yamlloader -f %{pyproject_files}

%changelog
%autochangelog
