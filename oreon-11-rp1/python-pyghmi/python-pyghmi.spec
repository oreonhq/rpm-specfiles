%global source0_hash none

Name:           python-pyghmi
Version:        1.6.19
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python General Hardware Management Initiative _IPMI and others_

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            http://github.com/openstack/pyghmi/
Source:         %{pypi_source pyghmi}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyghmi' generated automatically by pyp2spec.}

Patch1000:  nopbr.patch
Patch1001:  setup.patch

%description %_description

%package -n     python3-pyghmi
Summary:        %{summary}

%description -n python3-pyghmi %_description


%prep
%autosetup -p1 -n pyghmi-%{version}


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


%files -n python3-pyghmi -f %{pyproject_files}
%{_bindir}/fakebmc
%{_bindir}/pyghmicons
%{_bindir}/pyghmiutil
%{_bindir}/virshbmc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{?version:%{version}}%{!?version:1.6.2}-5
- Prepare for Oreon 11 (RP1)
