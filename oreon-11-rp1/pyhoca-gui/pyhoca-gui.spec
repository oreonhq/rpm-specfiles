%global source0_hash 4c71e74b19c4e820e1e38b22f16da4cf46cc852e1c95fd4d3d4153dc4fd1b22a
Name:           pyhoca-gui
Version:        0.6.1.1
Release:        1%{?dist}
Summary:        Graphical X2Go client written in (wx)Python
License:        AGPL-3.0-or-later
URL:            https://www.x2go.org/
Source0:        https://code.x2go.org/releases/source/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python%{python3_pkgversion}-cups
Requires:       python%{python3_pkgversion}-setproctitle
Requires:       python%{python3_pkgversion}-x2go >= 0.5.0.0
Requires:       libnotify
Requires:       python%{python3_pkgversion}-gobject-base
Requires:       python%{python3_pkgversion}-wxpython4
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyhoca-gui = %{version}-%{release}
# /oreon:deps
%description
X2Go is a server based computing environment with:
   - session resuming
   - low bandwidth support
   - LDAP support
   - client side mass storage mounting support
   - client side printing support
   - audio support
   - authentication by smartcard and USB stick

PyHoca-GUI is a slim X2Go client that docks to the desktop's
notification area and allows multiple X2Go session handling.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%py3_shebang_fix %{name}
%{__python3} setup.py build_i18n
%pyproject_wheel
%install
%pyproject_install
rm -r %{buildroot}%{python3_sitelib}%{_datadir}/locale
mv %{buildroot}%{python3_sitelib}%{_datadir}/* %{buildroot}%{_datadir}/
mkdir -p %{buildroot}%{_bindir}/
cp -p %{name} %{buildroot}%{_bindir}/
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang PyHoca-GUI
%oreon_autofiles main

%files

%changelog

%autochangelog
