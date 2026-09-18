%global source0_hash none

Name:           python-qrcode
Version:        8.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        QR Code image generator

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/lincolnloop/python-qrcode
Source:         %{pypi_source qrcode}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'qrcode' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-qrcode
Summary:        %{summary}

%description -n python3-qrcode %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-qrcode all,pil,png


%prep
%autosetup -p1 -n qrcode-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all,pil,png


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-qrcode -f %{pyproject_files}
%{_bindir}/qr

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.0-1
- Prepare for Oreon 11 (RP1)
