%global source0_hash none

Name:           python-zope-testing
Version:        6.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Zope testing helpers

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/zope.testing
Source:         %{pypi_source zope_testing}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'zope-testing' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-zope-testing
Summary:        %{summary}

%description -n python3-zope-testing %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-zope-testing docs,test


%prep
%autosetup -p1 -n zope_testing-%{version}


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


%files -n python3-zope-testing -f %{pyproject_files}

%changelog
%autochangelog
