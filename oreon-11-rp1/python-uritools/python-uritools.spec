%global source0_hash none

Name:           python-uritools
Version:        6.1.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        URI parsing, classification and composition

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/tkem/uritools/
Source:         %{pypi_source uritools}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'uritools' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-uritools
Summary:        %{summary}

%description -n python3-uritools %_description


%prep
%autosetup -p1 -n uritools-%{version}


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


%files -n python3-uritools -f %{pyproject_files}

%changelog
%autochangelog
