%global source0_hash none

Name:           python-aw-client
Version:        0.5.15
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Client library for ActivityWatch

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MPL-2.0
URL:            https://github.com/ActivityWatch/aw-client/
Source:         %{pypi_source aw_client}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'aw-client' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-aw-client
Summary:        %{summary}

%description -n python3-aw-client %_description


%prep
%autosetup -p1 -n aw_client-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-aw-client -f %{pyproject_files}
%{_bindir}/aw-client

%changelog
%autochangelog
