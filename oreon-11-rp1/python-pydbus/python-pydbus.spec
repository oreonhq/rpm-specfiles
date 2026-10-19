%global source0_hash 4207162eff54223822c185da06c1ba8a34137a9602f3da5a528eedf3f78d0f2c
%global srcname pydbus
Name:           python-%{srcname}
Version:        0.6.0
Release:        1%{?dist}
Summary:        Pythonic DBus library
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://pypi.python.org/pypi/pydbus
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
Patch1:        0001-make-direction-attribute-conforming-to-introspect.dt.patch
Patch2:        0002-Support-asynchronous-calls-58.patch
Patch3:        0003-Support-transformation-between-D-Bus-errors-and-exce.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-%{srcname}
Summary:        Pythonic DBus library
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-gobject-base
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-%{srcname}

Python 3 version.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{srcname}-%{version} -p1

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-pydbus -f %{oreon_filedir}/python3-pydbus.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.0-34
- Import
