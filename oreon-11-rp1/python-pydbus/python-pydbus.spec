%global srcname pydbus

Name:           python-%{srcname}
Version:        0.6.0
Release:        35%{?dist}
Summary:        Pythonic DBus library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://pypi.python.org/pypi/pydbus
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{srcname}; echo ${n:0:1})/%{srcname}/%{srcname}-%{version}.tar.gz

# upstream fix, not yet in release
# https://github.com/LEW21/pydbus/commit/ff792feb45bbdc0dd6a9ff7453825e34b6554865
Patch1: 0001-make-direction-attribute-conforming-to-introspect.dt.patch

BuildArch:      noarch

%global _description \
The pydbus module provides pythonic DBUS bindings.\
It is based on PyGI, the Python GObject Introspection bindings,\
which is the recommended way to use GLib from Python.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-gobject-base
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.0-35
- Drop stale Patch2 Patch3 (do not apply to 0.6.0)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.0-34
- Prepare for Oreon 11 (RP1)
