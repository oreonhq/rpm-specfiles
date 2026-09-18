%global source0_hash none

Name:           python-yubico
Version:        1.6.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python Yubico Client

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            http://github.com/Kami/python-yubico-client/
Source:         %{pypi_source yubico}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'yubico' generated automatically by pyp2spec.}

Patch0001:      0001-literal-comparison.patch

%description %_description

%package -n     python3-yubico
Summary:        %{summary}

%description -n python3-yubico %_description


%prep
%autosetup -p1 -n yubico-%{version}


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


%files -n python3-yubico -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.3-23
- Prepare for Oreon 11 (RP1)
