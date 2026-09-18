%global source0_hash none

Name:           python-fontconfig
Version:        0.6.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python bindings for Fontconfig library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL-3.0
URL:            https://github.com/Vayn/python-fontconfig
Source:         %{pypi_source python_fontconfig}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'python-fontconfig' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-python-fontconfig
Summary:        %{summary}

%description -n python3-python-fontconfig %_description


%prep
%autosetup -p1 -n python_fontconfig-%{version}


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


%files -n python3-python-fontconfig -f %{pyproject_files}

%changelog
%autochangelog
