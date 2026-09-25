%global source0_hash fd8acb5c67f260dfbdcc1b2dc95ff48b2b3f90708ae595c76f591bbf3f6f8eeb

Name:           python-hypothesis
Version:        6.168.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        The property-based testing library for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MPL-2.0
URL:            https://hypothesis.works
Source:         %{pypi_source hypothesis}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'hypothesis' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-hypothesis
Summary:        %{summary}

%description -n python3-hypothesis %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-hypothesis all,cli,codemods,crosshair,dateutil,django,dpcontracts,ghostwriter,lark,numpy,pandas,pytest,pytz,redis,watchdog,zoneinfo


%prep
%autosetup -p1 -n hypothesis-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all,cli,codemods,crosshair,dateutil,django,dpcontracts,ghostwriter,lark,numpy,pandas,pytest,pytz,redis,watchdog,zoneinfo


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-hypothesis -f %{pyproject_files}
%{_bindir}/hypothesis

%changelog
%autochangelog
