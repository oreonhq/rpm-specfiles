%global source0_hash 1d6c53acf160edc9b42e4ba535343b3567f2f341d289b9e63ca6a84372c2c518

%global srcname uswid

Name:           python-%{srcname}
Version:        0.5.2
Release:        %autorelease
Summary:        Python module for working with Firmware SBoMs

License:        LGPL-2.1-or-later
URL:            https://github.com/hughsie/python-uswid
Source:         %{pypi_source %{srcname}}

BuildArch:      noarch

%global _description %{expand:
Software Identification (SWID) tags provide an extensible XML-based structure to
identify and describe individual software components, patches, and installation
bundles. XML SWID tag representations can be too large for devices with network
and storage constraints.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-cbor2
BuildRequires:  python3-lxml
BuildRequires:  python3-pefile
BuildRequires:  python3-wheel

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
sed -i -e '/^#!\//, 1d' %{srcname}/*.py

%build
%py3_build

%install
%py3_install

%check
#%{python3} setup.py test
%pytest

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/uswid

%changelog
%autochangelog
