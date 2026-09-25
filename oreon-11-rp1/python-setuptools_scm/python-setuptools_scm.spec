%global source0_hash a69f28bfc245608781205e912faae437c2b2165773afa4e7b979d77447a69dd2

Name:           python-setuptools-scm
Version:        10.3.4
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        the blessed package to manage your versions by scm tags

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pypa/setuptools-scm/
Source:         %{pypi_source setuptools_scm}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'setuptools-scm' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-setuptools-scm
Summary:        %{summary}

%description -n python3-setuptools-scm %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-setuptools-scm rich,simple,toml


%prep
%autosetup -p1 -n setuptools_scm-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x rich,simple,toml


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-setuptools-scm -f %{pyproject_files}
%{_bindir}/setuptools-scm

%changelog
%autochangelog
