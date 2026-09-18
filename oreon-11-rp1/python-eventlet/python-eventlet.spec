%global source0_hash none

Name:           python-eventlet
Version:        0.41.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Highly concurrent networking library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/eventlet/eventlet
Source:         %{pypi_source eventlet}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'eventlet' generated automatically by pyp2spec.}

Patch0: 0001-Update-pyzmq-and-psycopg2-binary-versions.patch

%description %_description

%package -n     python3-eventlet
Summary:        %{summary}

%description -n python3-eventlet %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-eventlet dev


%prep
%autosetup -p1 -n eventlet-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-eventlet -f %{pyproject_files}

%changelog
%autochangelog
