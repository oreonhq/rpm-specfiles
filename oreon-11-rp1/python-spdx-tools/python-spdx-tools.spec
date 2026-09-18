%global source0_hash none

Name:           python-spdx-tools
Version:        0.8.5
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        SPDX parser and tools.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/spdx/tools-python
Source:         %{pypi_source spdx_tools}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'spdx-tools' generated automatically by pyp2spec.}

Patch:          0001-Update-excepted-typecheck-error-after-beartype-updat.patch
Patch:          0002-relationship_writer-properly-access-__annotations__-.patch

%description %_description

%package -n     python3-spdx-tools
Summary:        %{summary}

%description -n python3-spdx-tools %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-spdx-tools code-style,development,graph-generation,test


%prep
%autosetup -p1 -n spdx_tools-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x code-style,development,graph-generation,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-spdx-tools -f %{pyproject_files}
%{_bindir}/pyspdxtools
%{_bindir}/pyspdxtools3

%changelog
%autochangelog
