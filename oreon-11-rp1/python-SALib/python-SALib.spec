%global source0_hash none

Name:           python-salib
Version:        1.5.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Tools for global sensitivity analysis. Contains Sobol_, Morris, FAST, DGSM, PAWN, HDMR, Moment Independent and fractional factorial methods

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/SALib/SALib
Source:         %{pypi_source salib}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'salib' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-salib
Summary:        %{summary}

%description -n python3-salib %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-salib dev,distributed,doc,test


%prep
%autosetup -p1 -n salib-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,distributed,doc,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-salib -f %{pyproject_files}
%{_bindir}/salib

%changelog
%autochangelog
