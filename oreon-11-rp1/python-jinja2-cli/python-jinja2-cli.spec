%global source0_hash none

Name:           python-jinja2-cli
Version:        1.0.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        The CLI for Jinja2

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/mattrobenolt/jinja2-cli
Source:         %{pypi_source jinja2_cli}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'jinja2-cli' generated automatically by pyp2spec.}

Patch:          138.patch

%description %_description

%package -n     python3-jinja2-cli
Summary:        %{summary}

%description -n python3-jinja2-cli %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-jinja2-cli hjson,json5,toml,xml,yaml


%prep
%autosetup -p1 -n jinja2_cli-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x hjson,json5,toml,xml,yaml


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-jinja2-cli -f %{pyproject_files}
%{_bindir}/jinja2

%changelog
%autochangelog
