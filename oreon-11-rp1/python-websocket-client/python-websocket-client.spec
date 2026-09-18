%global source0_hash none

Name:           python-websocket-client
Version:        1.9.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        WebSocket client for Python with low level API options

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/websocket-client/websocket-client/
Source:         %{pypi_source websocket_client}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'websocket-client' generated automatically by pyp2spec.}

Patch:              0001-Include-pytest-in-test-extra.patch

%description %_description

%package -n     python3-websocket-client
Summary:        %{summary}

%description -n python3-websocket-client %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-websocket-client docs,optional,test


%prep
%autosetup -p1 -n websocket_client-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs,optional,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-websocket-client -f %{pyproject_files}
%{_bindir}/wsdump

%changelog
%autochangelog
