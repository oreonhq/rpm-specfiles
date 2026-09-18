%global source0_hash none

Name:           python-httpbin
Version:        0.10.4
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        HTTP Request and Response Service

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ISC AND MIT
URL:            https://github.com/psf/httpbin
Source:         %{pypi_source httpbin}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'httpbin' generated automatically by pyp2spec.}

Patch:          0001-Make-flasgger-dep-optional-26.patch
Patch:          0001-Replace-deprecated-JSONIFY_PRETTYPRINT_REGULAR-usage.patch
Patch:          0001-Fix-bytes-endpoint-with-newer-werkzeug-versions.patch

%description %_description

%package -n     python3-httpbin
Summary:        %{summary}

%description -n python3-httpbin %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-httpbin mainapp,test


%prep
%autosetup -p1 -n httpbin-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x mainapp,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-httpbin -f %{pyproject_files}

%changelog
%autochangelog
