%global source0_hash none

Name:           python-mutagen
Version:        1.48.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        read and write audio tags for many formats

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL-2.0-or-later
URL:            https://mutagen.readthedocs.io
Source:         %{pypi_source mutagen}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'mutagen' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-mutagen
Summary:        %{summary}

%description -n python3-mutagen %_description


%prep
%autosetup -p1 -n mutagen-%{version}


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


%files -n python3-mutagen -f %{pyproject_files}
%{_bindir}/mid3cp
%{_bindir}/mid3iconv
%{_bindir}/mid3v2
%{_bindir}/moggsplit
%{_bindir}/mutagen-inspect
%{_bindir}/mutagen-pony

%changelog
%autochangelog
