%global source0_hash none

Name:           python-charset-normalizer
Version:        3.5.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/jawah/charset_normalizer/blob/master/CHANGELOG.md
Source:         %{pypi_source charset_normalizer}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'charset-normalizer' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-charset-normalizer
Summary:        %{summary}

%description -n python3-charset-normalizer %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-charset-normalizer unicode-backport


%prep
%autosetup -p1 -n charset_normalizer-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x unicode-backport


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-charset-normalizer -f %{pyproject_files}
%{_bindir}/normalizer

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.4.6-1
- Prepare for Oreon 11 (RP1)
