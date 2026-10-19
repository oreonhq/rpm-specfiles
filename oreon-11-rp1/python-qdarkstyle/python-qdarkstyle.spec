%global source0_hash 5c7412cbe2f348ac55284f9869736fb9918e78f00fcd929bfd40e6fd66237224
%bcond recompile_assets 1
Name:           python-qdarkstyle
Version:        3.2.3
Release:        1%{?dist}
Summary:        The most complete dark/light style sheet for C++/Python and Qt applications
License:        MIT AND CC-BY-4.0
URL:            https://github.com/ColinDuquesnoy/QDarkStyleSheet
Source0:        https://github.com/ColinDuquesnoy/QDarkStyleSheet/archive/v.%{version}/QDarkStyleSheet-v.%{version}.tar.gz
Source10:       qdarkstyle.1
Source11:       qdarkstyle.example.1
Source12:       qdarkstyle.utils.1
Patch:          %{url}/pull/355.patch
Patch:          %{url}/pull/356.patch
BuildArch:      noarch
%global common_description %{expand:
The most complete dark/light style sheet for Qt applications (Qt4, Qt5, PySide,
PySide2, PyQt4, PyQt5, QtPy, PyQtGraph, Qt.Py) for Python and C++.}
# oreon:deps
BuildRequires:  hardlink
BuildRequires:  python3dist(helpdev)
BuildRequires:  python3dist(pytest)
# /oreon:deps
%description %{common_description}

%package -n python3-qdarkstyle
Summary:        The most complete dark/light style sheet for C++/Python and Qt applications
Recommends:     python3-qdarkstyle+develop = %{version}-%{release}
Recommends:     %{py3_dist helpdev}
%description -n python3-qdarkstyle %{common_description}

%{_bindir}/qdarkstyle.example
%{_mandir}/man1/qdarkstyle.example.1*

%{_bindir}/qdarkstyle.utils
%{_mandir}/man1/qdarkstyle.utils.1*

%prep

%autosetup -p1
%if %{with recompile_assets}
rm -vf qdarkstyle/*/*style.{qrc,qss} qdarkstyle/*/_variables.scss
%endif

# We helped upstream clean up shebangs in
# https://github.com/ColinDuquesnoy/QDarkStyleSheet/pull/333, but upstream
# seems to prefer to have some executables (with shebang lines) inside the
# qdarkstyle package directory. Since executable permissions will be removed
# when installing into site-packages, we should remove the shebangs too; they
# won’t make sense anymore.
#
# The find-then-modify pattern preserves mtimes on sources that did not need to
# be modified.
find 'qdarkstyle' -type f -name '*.py' \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r -t sed -r -i '1{/^#!/d}'

%build -p

%if %{with recompile_assets}
QT_QPA_PLATFORM=offscreen PYTHONPATH="${PWD}" %{python3} -m qdarkstyle.utils \
    --create 'pyqt5'
%endif
%install
%pyproject_install
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}'
hardlink -c -v '%{buildroot}%{python3_sitelib}/qdarkstyle/'
%oreon_autofiles python3-qdarkstyle usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest
%files -f %{oreon_filedir}/main.list
%files -n python3-qdarkstyle -f %{oreon_filedir}/python3-qdarkstyle.list

%changelog

%autochangelog
