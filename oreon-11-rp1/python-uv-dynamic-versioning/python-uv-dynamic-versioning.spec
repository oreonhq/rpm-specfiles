%global source0_hash none

Name:           python-uv-dynamic-versioning
Version:        0.14.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Dynamic versioning based on VCS tags for uv/hatch project

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/ninoseki/uv-dynamic-versioning/
Source:         %{pypi_source uv_dynamic_versioning}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'uv-dynamic-versioning' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-uv-dynamic-versioning
Summary:        %{summary}

%description -n python3-uv-dynamic-versioning %_description


%prep
%autosetup -p1 -n uv_dynamic_versioning-%{version}


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


%files -n python3-uv-dynamic-versioning -f %{pyproject_files}
%{_bindir}/uv-dynamic-versioning

%changelog
%autochangelog
