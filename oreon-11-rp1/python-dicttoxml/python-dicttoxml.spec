%global source0_hash none

Name:           python-dicttoxml
Version:        1.7.16
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Converts a Python dictionary or other native data type into a valid XML string.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/quandyfactory/dicttoxml
Source:         %{pypi_source dicttoxml}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'dicttoxml' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-dicttoxml
Summary:        %{summary}

%description -n python3-dicttoxml %_description


%prep
%autosetup -p1 -n dicttoxml-%{version}


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


%files -n python3-dicttoxml -f %{pyproject_files}

%changelog
%autochangelog
