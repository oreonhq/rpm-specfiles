%global source0_hash none

Name:           python-ase
Version:        3.29.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Atomic Simulation Environment

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        LGPL-2.1-or-later
URL:            https://ase-lib.org/
Source:         %{pypi_source ase}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ase' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-ase
Summary:        %{summary}

%description -n python3-ase %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-ase docs,lint,spglib,test


%prep
%autosetup -p1 -n ase-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs,lint,spglib,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-ase -f %{pyproject_files}
%{_bindir}/ase

%changelog
%autochangelog
