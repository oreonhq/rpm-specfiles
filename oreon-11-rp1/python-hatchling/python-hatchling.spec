%global source0_hash c4468f73144c054d2aab4ef0f0378c43b9878bf07f8ffd6b79690e970d375f07

Name:           python-hatchling
Version:        1.32.4
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Modern, extensible Python build backend

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://hatch.pypa.io/latest/
Source:         %{pypi_source hatchling}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'hatchling' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-hatchling
Summary:        %{summary}

%description -n python3-hatchling %_description


%prep
%autosetup -p1 -n hatchling-%{version}


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


%files -n python3-hatchling -f %{pyproject_files}
%{_bindir}/hatchling

%changelog
%autochangelog
