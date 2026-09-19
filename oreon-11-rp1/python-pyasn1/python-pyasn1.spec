%global source0_hash none

Name:           python-pyasn1
Version:        0.6.4
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Pure-Python implementation of ASN.1 types and DER/BER/CER codecs _X.208_

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-2-Clause
URL:            https://github.com/pyasn1/pyasn1
Source:         %{pypi_source pyasn1}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyasn1' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pyasn1
Summary:        %{summary}

%description -n python3-pyasn1 %_description


%prep
%autosetup -p1 -n pyasn1-%{version}


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


%files -n python3-pyasn1 -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.2-1
- Prepare for Oreon 11 (RP1)
