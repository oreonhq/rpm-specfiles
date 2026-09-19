%global source0_hash none

Name:           python-flask-compress
Version:        1.25
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Compress responses in your Flask app with gzip, deflate, brotli or zstandard.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/colour-science/flask-compress
Source:         %{pypi_source flask_compress}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'flask-compress' generated automatically by pyp2spec.}

Patch0:         flask-compress_setuptools-scm.patch

%description %_description

%package -n     python3-flask-compress
Summary:        %{summary}

%description -n python3-flask-compress %_description


%prep
%autosetup -p1 -n flask_compress-%{version}


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


%files -n python3-flask-compress -f %{pyproject_files}

%changelog
%autochangelog
