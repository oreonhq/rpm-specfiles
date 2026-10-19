%global source0_hash 1a9d57d15fb64288551cfe33de09823334a476c1b59819c817e8b94861a9de3a
Name:           git-cola
Version:        4.19.0
Release:        1%{?dist}
Summary:        A sleek and powerful git GUI
License:        GPL-2.0-or-later
URL:            https://git-cola.github.io
Source0:        https://github.com/git-cola/git-cola/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python%{python3_pkgversion}-pyqt6
Requires:       git
Requires:       hicolor-icon-theme
Requires:       python%{python3_pkgversion}dist(qtpy)
Recommends:     python%{python3_pkgversion}dist(notify2)
Recommends:     python%{python3_pkgversion}dist(send2trash) >= 1.7.1
%ifarch %{qt6_qtwebengine_arches}
Recommends:     python%{python3_pkgversion}-pyqt6-webengine
%endif
Suggests:       aspell
Suggests:       hunspell
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.0
Requires:       python3-git-cola = %{version}-%{release}
# /oreon:deps
%package -n       python3-git-cola+testing
Summary:        Metapackage for python3-git-cola testing extras
Requires:       python3-git-cola = %{version}-%{release}
Requires:       python3dist(pytest) >= 6
Requires:       python3dist(pytest-checkdocs) >= 2.4
Requires:       python3dist(pytest-enabler) >= 2.2
Requires:       python3dist(pytest-ruff) >= 0.2.1
Provides:       python3dist(git-cola[testing]) = %{version}-%{release}

%description -n python3-git-cola+testing
Metapackage for python3-git-cola testing extras.

%package -n       python3-git-cola+docs
Summary:        Metapackage for python3-git-cola docs extras
Requires:       python3-git-cola = %{version}-%{release}
Requires:       python3dist(rst.linker) >= 1.9
Provides:       python3dist(git-cola[docs]) = %{version}-%{release}

%description -n python3-git-cola+docs
Metapackage for python3-git-cola docs extras.

%package -n       python3-git-cola+extras
Summary:        Metapackage for python3-git-cola extras extras
Requires:       python3-git-cola = %{version}-%{release}
Provides:       python3dist(git-cola[extras]) = %{version}-%{release}

%description -n python3-git-cola+extras
Metapackage for python3-git-cola extras extras.

%package -n       python3-git-cola+dev
Summary:        Metapackage for python3-git-cola dev extras
Requires:       python3-git-cola = %{version}-%{release}
Requires:       python3dist(mypy) == 1.19.1
Provides:       python3dist(git-cola[dev]) = %{version}-%{release}

%description -n python3-git-cola+dev
Metapackage for python3-git-cola dev extras.

%package -n       python3-git-cola+build
Summary:        Metapackage for python3-git-cola build extras
Requires:       python3-git-cola = %{version}-%{release}
Requires:       python3dist(setuptools) >= 64.0
Requires:       python3dist(setuptools-scm[toml]) >= 3.4.1
Provides:       python3dist(git-cola[build]) = %{version}-%{release}

%description -n python3-git-cola+build
Metapackage for python3-git-cola build extras.

%package -n       python3-git-cola+pyqt5
Summary:        Metapackage for python3-git-cola pyqt5 extras
Requires:       python3-git-cola = %{version}-%{release}
Provides:       python3dist(git-cola[pyqt5]) = %{version}-%{release}

%description -n python3-git-cola+pyqt5
Metapackage for python3-git-cola pyqt5 extras.

%package -n       python3-git-cola+pyqt6
Summary:        Metapackage for python3-git-cola pyqt6 extras
Requires:       python3-git-cola = %{version}-%{release}
Provides:       python3dist(git-cola[pyqt6]) = %{version}-%{release}

%description -n python3-git-cola+pyqt6
Metapackage for python3-git-cola pyqt6 extras.

%package -n       python3-git-cola+pyside2
Summary:        Metapackage for python3-git-cola pyside2 extras
Requires:       python3-git-cola = %{version}-%{release}
Provides:       python3dist(git-cola[pyside2]) = %{version}-%{release}

%description -n python3-git-cola+pyside2
Metapackage for python3-git-cola pyside2 extras.

%package -n       python3-git-cola+pyside6
Summary:        Metapackage for python3-git-cola pyside6 extras
Requires:       python3-git-cola = %{version}-%{release}
Provides:       python3dist(git-cola[pyside6]) = %{version}-%{release}

%description -n python3-git-cola+pyside6
Metapackage for python3-git-cola pyside6 extras.

%description
git-cola is a powerful git GUI with a slick and intuitive user interface.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# fix #!/usr/bin/env python to #!/usr/bin/python3 everywhere
find . -type f -exec sh -c "head {} -n 1 | grep ^#\!\ \*/usr/bin/env\ python >/dev/null && sed -i -e sX^#\!\ \*/usr/bin/env\ python\ \*"\\\$"X#\!/usr/bin/python%{python3_pkgversion}Xg {}" \;

# Remove vendorized polib.py
rm cola/polib.py

%build

%global makeopts PYTHON="%{__python3}" SPHINXBUILD="$(ls /usr/bin/sphinx-build*|tail -n1)" NO_PRIVATE_LIBS=1 NO_VENDOR_LIBS=1
%pyproject_wheel
make %{makeopts} doc
%install
%pyproject_install
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/git-cola/lib/
make DESTDIR=%{buildroot} prefix=%{_prefix} %{makeopts} \
  install-desktop-files \
  install-doc \
  install-html \
  install-icons \
  install-metainfo
%oreon_autofiles main

%check

%pytest test
desktop-file-validate %{buildroot}%{_datadir}/applications/git-cola-folder-handler.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/git-cola.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/git-dag.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml
%files

%changelog

%autochangelog
