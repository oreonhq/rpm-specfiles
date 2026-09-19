%global source0_hash none

Name:           python-pillow
Version:        12.3.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python Imaging Library _fork_

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT-CMU
URL:            https://python-pillow.github.io
Source:         %{pypi_source pillow}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pillow' generated automatically by pyp2spec.}

Patch0:         pillow_mingw.patch

%description %_description

%package -n     python3-pillow
Summary:        %{summary}

%description -n python3-pillow %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-pillow docs,fpx,mic,test-arrow,tests,xmp


%prep
%autosetup -p1 -n pillow-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs,fpx,mic,test-arrow,tests,xmp


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-pillow -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 12.1.1-1
- Prepare for Oreon 11 (RP1)
