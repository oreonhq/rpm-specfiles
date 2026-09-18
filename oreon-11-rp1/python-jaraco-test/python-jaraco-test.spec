%global source0_hash none

Name:           python-jaraco-test
Version:        5.7.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Testing support by jaraco

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/jaraco/jaraco.test
Source:         %{pypi_source jaraco_test}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'jaraco-test' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-jaraco-test
Summary:        %{summary}

%description -n python3-jaraco-test %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-jaraco-test check,cover,doc,enabler,test,type


%prep
%autosetup -p1 -n jaraco_test-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x check,cover,doc,enabler,test,type


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-jaraco-test -f %{pyproject_files}

%changelog
%autochangelog
