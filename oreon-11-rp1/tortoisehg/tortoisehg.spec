%global source0_hash 2812d76e2436a7e9af30cd3f536d844304a3d8d20eda2daf234661985f207383
%undefine _py3_shebang_s
Name:           tortoisehg
Version:        7.2.2
Release:        1%{?dist}
Summary:        Mercurial GUI command line tool thg
License:        GPL-2.0-or-later
URL:            https://foss.heptapod.net/mercurial/tortoisehg/thg
Source0:        https://www.mercurial-scm.org/release/tortoisehg/targz/tortoisehg-%{version}.tar.gz
Source1:        thg.appdata.xml
BuildArch:      noarch
Requires:       mercurial, python3-iniparse
Requires:       python3-qscintilla-qt6, python3-pygments
Requires:       python3-gobject-base
Provides: tortoisehg-nautilus = %{version}-%{release}
Obsoletes: tortoisehg-nautilus < %{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-tortoisehg = %{version}-%{release}
# /oreon:deps
%description
This package contains the thg command line tool, which provides a graphical
user interface to the Mercurial distributed revision control system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export THG_QT_API=PyQt6
%pyproject_wheel
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
%oreon_autofiles main

%check

appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/appdata/thg.appdata.xml
%files

%changelog

%autochangelog
