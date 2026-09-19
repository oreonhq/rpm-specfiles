%global source0_hash none

Name:           python-black
Version:        26.5.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        The uncompromising code formatter.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/psf/black
Source:         %{pypi_source black}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'black' generated automatically by pyp2spec.}

Patch:          https://github.com/psf/black/commit/5977532781.patch
Patch:          https://github.com/psf/black/commit/14e1de805a.patch
Patch:          https://github.com/psf/black/commit/ed64d89faa.patch
Patch:          https://github.com/psf/black/commit/b0f36f5b42.patch

%description %_description

%package -n     python3-black
Summary:        %{summary}

%description -n python3-black %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-black colorama,d,jupyter,uvloop


%prep
%autosetup -p1 -n black-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x colorama,d,jupyter,uvloop


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-black -f %{pyproject_files}
%{_bindir}/black
%{_bindir}/blackd

%changelog
%autochangelog
