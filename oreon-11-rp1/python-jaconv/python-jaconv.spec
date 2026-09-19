%global source0_hash none

Name:           python-jaconv
Version:        0.5.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Pure-Python Japanese character interconverter for Hiragana, Katakana, Hankaku, Zenkaku and more

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/ikegami-yukino/jaconv
Source:         %{pypi_source jaconv}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'jaconv' generated automatically by pyp2spec.}

Patch0:         https://patch-diff.githubusercontent.com/raw/ikegami-yukino/jaconv/pull/36.patch

%description %_description

%package -n     python3-jaconv
Summary:        %{summary}

%description -n python3-jaconv %_description


%prep
%autosetup -p1 -n jaconv-%{version}


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


%files -n python3-jaconv -f %{pyproject_files}

%changelog
%autochangelog
