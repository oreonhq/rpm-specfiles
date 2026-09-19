%global source0_hash none

Name:           python-flufl-i18n
Version:        6.0.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A high level API for internationalizing Python libraries and applications

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://flufli18n.readthedocs.io
Source:         %{pypi_source flufl_i18n}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'flufl-i18n' generated automatically by pyp2spec.}

Patch:          flufl_i18n-no-covtest.diff

%description %_description

%package -n     python3-flufl-i18n
Summary:        %{summary}

%description -n python3-flufl-i18n %_description


%prep
%autosetup -p1 -n flufl_i18n-%{version}


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


%files -n python3-flufl-i18n -f %{pyproject_files}

%changelog
%autochangelog
