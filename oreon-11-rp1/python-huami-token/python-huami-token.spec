%global source0_hash none

Name:           python-huami-token
Version:        0.8.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        This script retrieves the Bluetooth access token for the watch or band from Huami servers. Additionally, it downloads the AGPS data packs, cep_alm_pak.zip and cep_7days.zip.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://codeberg.org/argrento/huami-token
Source:         %{pypi_source huami_token}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'huami-token' generated automatically by pyp2spec.}

Patch:          %{name}-deps.patch
Patch:          %{name}-entrypoint.patch
Patch:          %{name}-headers.patch

%description %_description

%package -n     python3-huami-token
Summary:        %{summary}

%description -n python3-huami-token %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-huami-token dev


%prep
%autosetup -p1 -n huami_token-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-huami-token -f %{pyproject_files}
%{_bindir}/huami-token

%changelog
%autochangelog
