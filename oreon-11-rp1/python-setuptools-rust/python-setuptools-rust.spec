%global source0_hash none

Name:           python-setuptools-rust
Version:        1.13.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Setuptools Rust extension plugin

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/PyO3/setuptools-rust
Source:         %{pypi_source setuptools_rust}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'setuptools-rust' generated automatically by pyp2spec.}

Patch:          setuptools_rust-1.12.0-pyo3-0.28.patch

%description %_description

%package -n     python3-setuptools-rust
Summary:        %{summary}

%description -n python3-setuptools-rust %_description


%prep
%autosetup -p1 -n setuptools_rust-%{version}


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


%files -n python3-setuptools-rust -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.12.0-1
- Prepare for Oreon 11 (RP1)
