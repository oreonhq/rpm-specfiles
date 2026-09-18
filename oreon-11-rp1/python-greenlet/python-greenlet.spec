%global source0_hash none

Name:           python-greenlet
Version:        3.5.6
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Lightweight in-process concurrent programming

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT AND PSF-2.0
URL:            https://greenlet.readthedocs.io
Source:         %{pypi_source greenlet}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'greenlet' generated automatically by pyp2spec.}

Patch:        https://patch-diff.githubusercontent.com/raw/python-greenlet/greenlet/pull/482.patch
Patch:          https://patch-diff.githubusercontent.com/raw/python-greenlet/greenlet/pull/482.patch

%description %_description

%package -n     python3-greenlet
Summary:        %{summary}

%description -n python3-greenlet %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-greenlet docs,test


%prep
%autosetup -p1 -n greenlet-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-greenlet -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.3.0-2
- Prepare for Oreon 11 (RP1)
