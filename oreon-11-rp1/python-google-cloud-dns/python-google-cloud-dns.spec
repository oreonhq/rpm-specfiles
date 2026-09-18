%global source0_hash none

Name:           python-google-cloud-dns
Version:        0.37.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Google Cloud DNS API client library

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-dns
Source:         %{pypi_source google_cloud_dns}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'google-cloud-dns' generated automatically by pyp2spec.}

Patch0:         python-google-cloud-dns-mock.patch

%description %_description

%package -n     python3-google-cloud-dns
Summary:        %{summary}

%description -n python3-google-cloud-dns %_description


%prep
%autosetup -p1 -n google_cloud_dns-%{version}


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


%files -n python3-google-cloud-dns -f %{pyproject_files}

%changelog
%autochangelog
