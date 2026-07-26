%global source0_hash ac20cb676a690f763bd5cdf550d8abff5a56d5004956230ff4976826259fd279

# Prevent %%pyproject_install from specifying -s in the executable - that would prevent thg from picking up user installed extensions
%undefine _py3_shebang_s

Name:           tortoisehg
Version:        7.0.1
Release:        6%{?dist}
Summary:        Mercurial GUI command line tool thg
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://foss.heptapod.net/mercurial/tortoisehg/thg
Source0:        https://www.mercurial-scm.org/release/tortoisehg/targz/tortoisehg-%{version}.tar.gz
Source1:        thg.appdata.xml
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel, python3-setuptools, python3-pip, python3-wheel, python3-sphinx, python3-pyqt6-base
BuildRequires:  mercurial, gettext, desktop-file-utils, libappstream-glib
Requires:       mercurial, python3-iniparse
Requires:       python3-qscintilla-qt6, python3-pygments
Requires:       python3-gobject-base

Provides: tortoisehg-nautilus = %{version}-%{release}
Obsoletes: tortoisehg-nautilus < %{version}-%{release}

%description
This package contains the thg command line tool, which provides a graphical
user interface to the Mercurial distributed revision control system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

%build
export THG_QT_API=PyQt6
%pyproject_wheel

# override config.py from setup.py build_config()
sed \
  "s|^\(license_path *= *\).*|\1'%{_licensedir}/tortoisehg/COPYING.txt'|g" \
  build/lib/tortoisehg/util/config.py

(cd doc && make html)
rm doc/build/html/.buildinfo

%install
export THG_QT_API=PyQt6
%pyproject_install
rm $RPM_BUILD_ROOT/%{python3_sitelib}/hgext3rd/__init__.*
rm $RPM_BUILD_ROOT/%{python3_sitelib}/hgext3rd/__pycache__/__init__.*

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/mercurial/hgrc.d
install -pm0644 contrib/mergetools.rc $RPM_BUILD_ROOT%{_sysconfdir}/mercurial/hgrc.d/thgmergetools.rc

desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications contrib/thg.desktop
install -D %{SOURCE1} -pm0644 $RPM_BUILD_ROOT/%{_datadir}/appdata/thg.appdata.xml

%find_lang %{name}

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/appdata/thg.appdata.xml

%files -f %{name}.lang
%license COPYING.txt
%exclude %{_datadir}/doc/tortoisehg/COPYING.txt
%doc doc/build/html/
%config(noreplace) %{_sysconfdir}/mercurial/hgrc.d/thgmergetools.rc
%{_bindir}/thg
%{_datadir}/appdata/thg.appdata.xml
%{python3_sitelib}/hgext3rd/thg.py*
%{python3_sitelib}/hgext3rd/__pycache__/thg.*.pyc
%{python3_sitelib}/tortoisehg/
%{python3_sitelib}/tortoisehg-*.dist-info
%{_datadir}/pixmaps/tortoisehg/
%{_datadir}/pixmaps/thg_logo.svg
%{_datadir}/applications/thg.desktop

%exclude %{_datadir}/nautilus-python/extensions/nautilus-thg.py
%exclude %{_datadir}/nautilus-python/extensions/__pycache__/nautilus-thg.cpython-*.pyc

%changelog
%autochangelog
