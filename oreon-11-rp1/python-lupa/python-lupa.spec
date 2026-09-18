%global source0_hash none

Name:           python-lupa
Version:        2.8
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python wrapper around Lua and LuaJIT

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/scoder/lupa
Source:         %{pypi_source lupa}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'lupa' generated automatically by pyp2spec.}

Patch:          lupa-default-to-no-bundle.diff

%description %_description

%package -n     python3-lupa
Summary:        %{summary}

%description -n python3-lupa %_description


%prep
%autosetup -p1 -n lupa-%{version}


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


%files -n python3-lupa -f %{pyproject_files}

%changelog
%autochangelog
