%global source0_hash none

Name:           python-chardet
Version:        7.6.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Universal character encoding detector

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        0BSD
URL:            https://github.com/chardet/chardet
Source:         %{pypi_source chardet}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'chardet' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-chardet
Summary:        %{summary}

%description -n python3-chardet %_description


%prep
%autosetup -p1 -n chardet-%{version}


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


%files -n python3-chardet -f %{pyproject_files}
%{_bindir}/chardetect

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.0.0.post1-1
- Import
