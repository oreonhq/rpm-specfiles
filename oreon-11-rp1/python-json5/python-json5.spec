%global source0_hash none

Name:           python-json5
Version:        0.15.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A Python implementation of the JSON5 data format.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/dpranke/pyjson5
Source:         %{pypi_source json5}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'json5' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-json5
Summary:        %{summary}

%description -n python3-json5 %_description


%prep
%autosetup -p1 -n json5-%{version}


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


%files -n python3-json5 -f %{pyproject_files}
%{_bindir}/pyjson5

%changelog
%autochangelog
