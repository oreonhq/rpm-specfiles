%global source0_hash none

Name:           python-meson-python
Version:        0.21.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        The Python build backend for Meson projects

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/mesonbuild/meson-python
Source:         %{pypi_source meson_python}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'meson-python' generated automatically by pyp2spec.}

Patch100:        meson-python-0.18.0-remove-patchelf.patch

%description %_description

%package -n     python3-meson-python
Summary:        %{summary}

%description -n python3-meson-python %_description


%prep
%autosetup -p1 -n meson_python-%{version}


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


%files -n python3-meson-python -f %{pyproject_files}

%changelog
%autochangelog