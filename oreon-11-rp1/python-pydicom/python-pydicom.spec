%global source0_hash none

Name:           python-pydicom
Version:        3.0.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A pure Python package for reading and writing DICOM data

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pydicom/pydicom
Source:         %{pypi_source pydicom}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pydicom' generated automatically by pyp2spec.}

Patch:          pydicom-3.0.1-endian-numpy.patch
Patch:          pydicom-3.0.1-endian-pillow.patch
Patch:          https://github.com/pydicom/pydicom/pull/2173/commits/016abf0fa18a6f578a55d9816084f901a9809367.patch

%description %_description

%package -n     python3-pydicom
Summary:        %{summary}

%description -n python3-pydicom %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-pydicom basic,dev,docs,gpl-license,pixeldata


%prep
%autosetup -p1 -n pydicom-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x basic,dev,docs,gpl-license,pixeldata


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-pydicom -f %{pyproject_files}
%{_bindir}/pydicom

%changelog
%autochangelog
