%global source0_hash none

Name:           python-pyongc
Version:        1.2.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python interface to OpenNGC database data

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT AND CC-BY-SA-4.0
URL:            https://github.com/mattiaverga/PyOngc
Source:         %{pypi_source pyongc}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyongc' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pyongc
Summary:        %{summary}

%description -n python3-pyongc %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-pyongc data,development,docs


%prep
%autosetup -p1 -n pyongc-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x data,development,docs


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-pyongc -f %{pyproject_files}
%{_bindir}/ongc

%changelog
%autochangelog
