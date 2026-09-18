%global source0_hash none

Name:           python-zope-testrunner
Version:        8.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Zope testrunner script.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/zope.testrunner
Source:         %{pypi_source zope_testrunner}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'zope-testrunner' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-zope-testrunner
Summary:        %{summary}

%description -n python3-zope-testrunner %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-zope-testrunner docs,subunit,test


%prep
%autosetup -p1 -n zope_testrunner-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs,subunit,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-zope-testrunner -f %{pyproject_files}
%{_bindir}/zope-testrunner

%changelog
%autochangelog
