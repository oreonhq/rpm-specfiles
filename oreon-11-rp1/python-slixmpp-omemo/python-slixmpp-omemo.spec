%global source0_hash none

Name:           python-slixmpp-omemo
Version:        2.2.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        OMEMO plugin for Slixmpp

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        AGPL-3.0-only
URL:            https://github.com/Syndace/slixmpp-omemo
Source:         %{pypi_source slixmpp_omemo}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'slixmpp-omemo' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-slixmpp-omemo
Summary:        %{summary}

%description -n python3-slixmpp-omemo %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-slixmpp-omemo dev,docs,lint,test


%prep
%autosetup -p1 -n slixmpp_omemo-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,docs,lint,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-slixmpp-omemo -f %{pyproject_files}

%changelog
%autochangelog
