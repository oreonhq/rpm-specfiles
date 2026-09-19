%global source0_hash none

Name:           python-bravado-core
Version:        6.4.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Library for adding Swagger support to clients and servers

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/Yelp/bravado-core
Source:         %{pypi_source bravado_core}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'bravado-core' generated automatically by pyp2spec.}

Patch:          0001-Use-standard-library-mock-when-possible.patch

%description %_description

%package -n     python3-bravado-core
Summary:        %{summary}

%description -n python3-bravado-core %_description


%prep
%autosetup -p1 -n bravado_core-%{version}


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


%files -n python3-bravado-core -f %{pyproject_files}

%changelog
%autochangelog
