%global source0_hash 626b501a51ac892fc3460cf550e60dca121f544eaa46eb69c90ce4682fc7ec02

%global module	gettext

Name:		python-%{module}
Version:	4.0
Release:	21%{?dist}
Summary:	Python Gettext po to mo file compiler
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD

URL:		https://pypi.org/project/python-gettext/
Source0:	%{pypi_source %{name}}
BuildArch:	noarch

%description
This implementation of Gettext for Python includes a Msgfmt class which can be
used to generate compiled mo files from Gettext po files and includes support
for the newer msgctxt keyword.

%package -n	python3-%{module}
Summary:	Python 3 Gettext po to mo file compiler
BuildRequires:	python3-devel
BuildRequires:	python3dist(setuptools)
%{?python_provide:%python_provide python3-%{module}}

%description -n	python3-%{module}
This implementation of Gettext for Python 3 includes a Msgfmt class which can be
used to generate compiled mo files from Gettext po files and includes support
for the newer msgctxt keyword.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Remove bundled egg-info
rm -rf python_gettext.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{module}
%doc CHANGES.rst README.rst
%license LICENSE.rst
%{python3_sitelib}/pythongettext/
%{python3_sitelib}/python_gettext-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
