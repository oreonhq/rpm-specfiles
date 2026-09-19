%global source0_hash none

Name:           python-smartypants
Version:        2.0.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python with the SmartyPants

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/justinmayer/smartypants.py
Source:         %{pypi_source smartypants}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'smartypants' generated automatically by pyp2spec.}

Patch:          0001-Fix-regexps-and-tests-for-python3.12.patch

%description %_description

%package -n     python3-smartypants
Summary:        %{summary}

%description -n python3-smartypants %_description


%prep
%autosetup -p1 -n smartypants-%{version}


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


%files -n python3-smartypants -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.1-28
- Prepare for Oreon 11 (RP1)
