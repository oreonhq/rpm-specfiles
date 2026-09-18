%global source0_hash none

Name:           python-avro
Version:        1.12.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Avro is a serialization and RPC framework.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://avro.apache.org/
Source:         %{pypi_source avro}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'avro' generated automatically by pyp2spec.}

Patch0:         0001-remove-ipc-tests-as-they-require-internet-connection.diff

%description %_description

%package -n     python3-avro
Summary:        %{summary}

%description -n python3-avro %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-avro snappy,zstandard


%prep
%autosetup -p1 -n avro-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x snappy,zstandard


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-avro -f %{pyproject_files}
%{_bindir}/avro

%changelog
%autochangelog
