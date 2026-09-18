%global source0_hash none

Name:           python-fido2
Version:        2.2.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        FIDO2/WebAuthn library for implementing clients and servers.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/Yubico/python-fido2
Source:         %{pypi_source fido2}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'fido2' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-fido2
Summary:        %{summary}

%description -n python3-fido2 %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-fido2 pcsc


%prep
%autosetup -p1 -n fido2-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x pcsc


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-fido2 -f %{pyproject_files}

%changelog
%autochangelog
