%global source0_hash none

Name:           python-beautifulsoup4
Version:        4.15.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Screen-scraping library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://www.crummy.com/software/BeautifulSoup/bs4/
Source:         %{pypi_source beautifulsoup4}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'beautifulsoup4' generated automatically by pyp2spec.}

Patch0:         0001-Skip-the-lxml-tree-builder-s-test_surrogate_in_chara.patch
Patch1:         0001-Change-the-html.parser-tree-builder-s-code-for-handl.patch
Patch11:        beautifulsoup4-4.14-disable-soupsieve.patch

%description %_description

%package -n     python3-beautifulsoup4
Summary:        %{summary}

%description -n python3-beautifulsoup4 %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-beautifulsoup4 cchardet,chardet,charset-normalizer,html5lib,lxml


%prep
%autosetup -p1 -n beautifulsoup4-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x cchardet,chardet,charset-normalizer,html5lib,lxml


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-beautifulsoup4 -f %{pyproject_files}

%changelog
%autochangelog
