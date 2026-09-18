%global source0_hash none

Name:           python-pendulum
Version:        3.2.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python datetimes made easy

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://pendulum.eustace.io
Source:         %{pypi_source pendulum}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pendulum' generated automatically by pyp2spec.}

Patch:          0001-Allow-PyO3-0.26-until-we-have-0.27-RHBZ-2404994.patch

%description %_description

%package -n     python3-pendulum
Summary:        %{summary}

%description -n python3-pendulum %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-pendulum test


%prep
%autosetup -p1 -n pendulum-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-pendulum -f %{pyproject_files}

%changelog
%autochangelog
