%global source0_hash none

Name:           python-minikerberos
Version:        0.4.9
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Kerberos manipulation library in pure Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/skelsec/minikerberos
Source:         %{pypi_source minikerberos}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'minikerberos' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-minikerberos
Summary:        %{summary}

%description -n python3-minikerberos %_description


%prep
%autosetup -p1 -n minikerberos-%{version}


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


%files -n python3-minikerberos -f %{pyproject_files}
%{_bindir}/minikerberos-asreproast
%{_bindir}/minikerberos-ccache2kirbi
%{_bindir}/minikerberos-ccacheedit
%{_bindir}/minikerberos-ccacheroast
%{_bindir}/minikerberos-cve202233647
%{_bindir}/minikerberos-cve202233679
%{_bindir}/minikerberos-getntpkinit
%{_bindir}/minikerberos-gets4u2proxy
%{_bindir}/minikerberos-gets4u2self
%{_bindir}/minikerberos-gettgs
%{_bindir}/minikerberos-gettgt
%{_bindir}/minikerberos-kerb23hashdecrypt
%{_bindir}/minikerberos-kerberoast
%{_bindir}/minikerberos-keylist
%{_bindir}/minikerberos-kirbi2ccache
%{_bindir}/minikerberos-pw

%changelog
%autochangelog
