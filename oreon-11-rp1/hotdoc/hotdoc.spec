%global source0_hash cf22977cae68ca2f1e223dc901258dcbbd0e07eca924d8156c4fc94a54cad40b
Name:           hotdoc
Version:        0.18.3
Release:        1%{?dist}
Summary:        Documentation tool
License:        LGPL-2.1-or-later
URL:            https://pypi.org/project/hotdoc/
Source0:        https://files.pythonhosted.org/packages/a2/e8/799c34a47c3512899299113d55d928a5ee3d25649774c80946e97b53a7ba/hotdoc-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(meson) >= 1.0.0
BuildRequires:  python3dist(meson-python) >= 0.14.0
Requires:       python3-hotdoc = %{version}-%{release}
# /oreon:deps
%description
Hotdoc builds API documentation.

%package -n python3-hotdoc
Summary:        Documentation tool
Requires:       python3-appdirs
Requires:       python3-dbus-deviation
Requires:       python3-feedgen
Requires:       python3-lxml
Requires:       python3-networkx
Requires:       python3-pkgconfig
Requires:       python3-pyyaml
Requires:       python3-schema
Requires:       python3-toposort
Requires:       python3-wheezy-template
# oreon:reqs
Requires:       python3dist(appdirs) >= 1.4.4
Requires:       python3dist(dbus-deviation) >= 0.6.1
Requires:       python3dist(feedgen) >= 1.0.0
Requires:       python3dist(lxml) >= 5.4.0
Requires:       python3dist(networkx) >= 3.4
Requires:       python3dist(pkgconfig) >= 1.6.0
Requires:       python3dist(pyyaml) >= 6.0.2
Requires:       python3dist(schema) >= 0.7.7
Requires:       python3dist(toposort) >= 1.10
Requires:       python3dist(wheezy.template) >= 3.2.3
# /oreon:reqs
%description -n python3-hotdoc
Hotdoc builds API documentation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir hotdoc-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-hotdoc usr/lib/python3*/site-packages/hotdoc* usr/lib64/python3*/site-packages/hotdoc* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/hotdoc* usr/lib64/python3*/site-packages/hotdoc* usr/bin/*

%files
%files -n python3-hotdoc -f %{oreon_filedir}/python3-hotdoc.list
