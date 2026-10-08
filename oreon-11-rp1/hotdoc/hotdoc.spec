%global source0_hash cf22977cae68ca2f1e223dc901258dcbbd0e07eca924d8156c4fc94a54cad40b

Name:           hotdoc
Version:        0.18.3
Release:        1%{?dist}
Summary:        Documentation tool
License:        LGPL-2.1-or-later
URL:            https://pypi.org/project/hotdoc/
Source0:        https://files.pythonhosted.org/packages/a2/e8/799c34a47c3512899299113d55d928a5ee3d25649774c80946e97b53a7ba/hotdoc-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3-meson-python
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  python3-appdirs
BuildRequires:  python3-dbus-deviation
BuildRequires:  python3-feedgen
BuildRequires:  python3-lxml
BuildRequires:  python3-networkx
BuildRequires:  python3-pkgconfig
BuildRequires:  python3-pyyaml
BuildRequires:  python3-schema
BuildRequires:  python3-toposort
BuildRequires:  python3-wheezy-template

%description
Hotdoc builds API documentation.

%package -n python3-hotdoc
Summary:        %{summary}
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

%description -n python3-hotdoc
Hotdoc builds API documentation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n hotdoc-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files hotdoc

%files -n python3-hotdoc -f %{pyproject_files}
%{_bindir}/hotdoc
%{_bindir}/hotdoc_dep_printer
