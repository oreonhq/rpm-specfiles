%global source0_hash none

Name:           python-ua-parser
Version:        1.0.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python port of Browserscope_s user agent parser

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/ua-parser/uap-python
Source:         %{pypi_source ua_parser}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ua-parser' generated automatically by pyp2spec.}

Patch0:         ua_parser-no-ua_parse_rs.patch

%description %_description

%package -n     python3-ua-parser
Summary:        %{summary}

%description -n python3-ua-parser %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-ua-parser re2,regex,yaml


%prep
%autosetup -p1 -n ua_parser-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x re2,regex,yaml


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-ua-parser -f %{pyproject_files}

%changelog
%autochangelog
