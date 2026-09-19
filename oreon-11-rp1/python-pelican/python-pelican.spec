%global source0_hash none

Name:           python-pelican
Version:        4.12.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Static site generator supporting Markdown and reStructuredText

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        AGPL-3.0-or-later
URL:            https://getpelican.com
Source:         %{pypi_source pelican}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pelican' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pelican
Summary:        %{summary}

%description -n python3-pelican %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-pelican markdown


%prep
%autosetup -p1 -n pelican-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x markdown


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-pelican -f %{pyproject_files}
%{_bindir}/pelican
%{_bindir}/pelican-import
%{_bindir}/pelican-plugins
%{_bindir}/pelican-quickstart
%{_bindir}/pelican-themes

%changelog
%autochangelog
