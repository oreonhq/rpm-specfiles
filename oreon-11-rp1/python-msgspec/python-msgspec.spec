%global source0_hash none

Name:           python-msgspec
Version:        0.21.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A fast serialization and validation library, with builtin support for JSON, MessagePack, YAML, and TOML.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://jcristharif.com/msgspec/
Source:         %{pypi_source msgspec}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'msgspec' generated automatically by pyp2spec.}

Patch:          https://github.com/jcrist/msgspec/pull/852.patch

%description %_description

%package -n     python3-msgspec
Summary:        %{summary}

%description -n python3-msgspec %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-msgspec toml,yaml


%prep
%autosetup -p1 -n msgspec-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x toml,yaml


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-msgspec -f %{pyproject_files}

%changelog
%autochangelog
