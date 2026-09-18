%global source0_hash none

Name:           python-cattrs
Version:        26.2.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Composable complex class support for attrs and dataclasses.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://catt.rs
Source:         %{pypi_source cattrs}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cattrs' generated automatically by pyp2spec.}

Patch:          0001-Downstream-temporarily-loosen-version-bounds-on-some.patch

%description %_description

%package -n     python3-cattrs
Summary:        %{summary}

%description -n python3-cattrs %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-cattrs bson,cbor2,msgpack,msgspec,orjson,pyyaml,tomlkit,tomllib,ujson


%prep
%autosetup -p1 -n cattrs-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x bson,cbor2,msgpack,msgspec,orjson,pyyaml,tomlkit,tomllib,ujson


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-cattrs -f %{pyproject_files}

%changelog
%autochangelog
