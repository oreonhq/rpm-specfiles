%global source0_hash none

Name:           python-apache-libcloud
Version:        3.9.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A standard Python library that abstracts away differences among multiple cloud provider APIs. For more information and documentation, please see https://libcloud.apache.org

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://libcloud.apache.org
Source:         %{pypi_source apache_libcloud}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'apache-libcloud' generated automatically by pyp2spec.}

Patch0:         000-remove-linter-deps.patch

%description %_description

%package -n     python3-apache-libcloud
Summary:        %{summary}

%description -n python3-apache-libcloud %_description


%prep
%autosetup -p1 -n apache_libcloud-%{version}


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


%files -n python3-apache-libcloud -f %{pyproject_files}

%changelog
%autochangelog
