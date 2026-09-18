%global source0_hash none

Name:           python-autobahn
Version:        26.7.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        WebSocket client _ server library, WAMP real-time framework

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://autobahn.readthedocs.io/
Source:         %{pypi_source autobahn}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'autobahn' generated automatically by pyp2spec.}

Patch0:         remove-ubjson.patch
Patch1:         remove-unpackaged-sphinx-ext.patch

%description %_description

%package -n     python3-autobahn
Summary:        %{summary}

%description -n python3-autobahn %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-autobahn accelerate,all,asyncio,benchmark,build-tools,compress,dev,docs,encryption,nvx,scram,serialization,twisted


%prep
%autosetup -p1 -n autobahn-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x accelerate,all,asyncio,benchmark,build-tools,compress,dev,docs,encryption,nvx,scram,serialization,twisted


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-autobahn -f %{pyproject_files}
%{_bindir}/flatc
%{_bindir}/wamp

%changelog
%autochangelog
