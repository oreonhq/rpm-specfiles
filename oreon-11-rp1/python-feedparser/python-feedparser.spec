%global source0_hash none

Name:           python-feedparser
Version:        6.0.14
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Universal feed parser, handles RSS 0.9x, RSS 1.0, RSS 2.0, CDF, Atom 0.3, and Atom 1.0 feeds

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-2-Clause
URL:            https://github.com/kurtmckee/feedparser
Source:         %{pypi_source feedparser}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'feedparser' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-feedparser
Summary:        %{summary}

%description -n python3-feedparser %_description


%prep
%autosetup -p1 -n feedparser-%{version}


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


%files -n python3-feedparser -f %{pyproject_files}

%changelog
%autochangelog
