%global source0_hash 42c962632b239a46e13eadcf63754298f7bda097405d17154b559c4376243230

%global modname gattlib

Name:               python-gattlib
Version:            0.20210616
Release:            19%{?dist}
Summary:            Library to access Bluetooth LE devices

License:            Apache-2.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
# main package under ASL 2.0
# src/bluez under GPLv2+ and LGPLv2+
URL:                https://github.com/oscaracena/pygattlib
Source0:            https://files.pythonhosted.org/packages/source/g/%{modname}/%{modname}-%{version}.tar.gz
Source1:	    COPYING
Patch0:             py313.patch

BuildRequires:      gcc-c++

%description
%{summary}.

%package -n python%{python3_pkgversion}-%{modname}
Summary:            %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-setuptools
BuildRequires:      boost-python%{python3_pkgversion}-devel
BuildRequires:      glib2-devel
BuildRequires:      bluez-libs-devel

%description -n python%{python3_pkgversion}-%{modname}
%{summary}.

Python %{python3_version} version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version} -p1
cp %{S:1} .

find . -type f | xargs chmod -x

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python%{python3_pkgversion}-%{modname}
%license COPYING
%{python3_sitearch}/gattlib*

%changelog
%autochangelog
