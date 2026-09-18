%global source0_hash none

Name:           python-requests
Version:        2.34.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python HTTP for Humans.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/psf/requests
Source:         %{pypi_source requests}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'requests' generated automatically by pyp2spec.}

Patch:          system-certs.patch
Patch:          support_IPv6_CIDR_in_no_proxy.patch

%description %_description

%package -n     python3-requests
Summary:        %{summary}

%description -n python3-requests %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-requests security,socks,use-chardet-on-py3


%prep
%autosetup -p1 -n requests-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x security,socks,use-chardet-on-py3


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-requests -f %{pyproject_files}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.33.1-1
- Import
