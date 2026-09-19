%global source0_hash none

Name:           python-pycurl
Version:        7.48.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        PycURL -- A Python Interface To The cURL library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        LGPL-2.1-only OR MIT
URL:            https://pycurl.github.io/
Source:         %{pypi_source pycurl}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pycurl' generated automatically by pyp2spec.}

Patch1:         0001-python-pycurl-7.45.1-tls-backend.patch
Patch2:         ea92e3ca230a3ff3d464cb6816102fa157177aca.patch

%description %_description

%package -n     python3-pycurl
Summary:        %{summary}

%description -n python3-pycurl %_description


%prep
%autosetup -p1 -n pycurl-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-pycurl -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.45.7-2
- Prepare for Oreon 11 (RP1)
