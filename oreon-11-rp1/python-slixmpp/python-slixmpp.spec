%global source0_hash none

Name:           python-slixmpp
Version:        1.17.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Slixmpp is an elegant Python library for XMPP _aka Jabber_.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            ...
Source:         %{pypi_source slixmpp}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'slixmpp' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-slixmpp
Summary:        %{summary}

%description -n python3-slixmpp %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-slixmpp safer-xml-parsing,xep-0363,xep-0444-compliance,xep-0454


%prep
%autosetup -p1 -n slixmpp-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x safer-xml-parsing,xep-0363,xep-0444-compliance,xep-0454


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-slixmpp -f %{pyproject_files}

%changelog
%autochangelog
