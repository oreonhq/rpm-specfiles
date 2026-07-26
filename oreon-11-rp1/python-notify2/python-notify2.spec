%global source0_hash 33fa108d50c42f3cd3407cc437518ad3f6225d1bb237011f16393c9dd3ce197d

# Created by pyp2rpm-3.3.2

# Enable auto-generation of runtime dependencies
%{?python_enable_dependency_generator}

%global pypi_name notify2

Name:           python-%{pypi_name}
Version:        0.3.1
Release:        30%{?dist}
Summary:        Python interface to DBus notifications

License:        BSD-2-Clause
URL:            https://bitbucket.org/takluyver/pynotify2
Source0:        https://files.pythonhosted.org/packages/source/n/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

# Submitted: https://bitbucket.org/takluyver/pynotify2/pull-requests/1
Patch0001:      0001-doc-Fix-intersphinx-mapping-for-Sphinx-8.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  %{_bindir}/sphinx-build-3

%description
This is a pure-python replacement for notify-python, using python-dbus
to communicate with the notifications server directly.

It's compatible with Python 2 and 3, and its callbacks can work with
Gtk or Qt applications.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
# Requires aren't properly stated for dbus-python, so they aren't generated properly
Requires:       python%{python3_pkgversion}-dbus

%description -n python%{python3_pkgversion}-%{pypi_name}
This is a pure-python replacement for notify-python, using python-dbus
to communicate with the notifications server directly.

It's compatible with Python 2 and 3, and its callbacks can work with
Gtk or Qt applications.

%package -n python-%{pypi_name}-doc
Summary:        notify2 documentation
%description -n python-%{pypi_name}-doc
Documentation for notify2

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license docs/license.rst LICENSE
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license docs/license.rst LICENSE

%changelog
%autochangelog
