%global source0_hash 92b73bb2c2c1f24cce8579ff2ab03f84e3f55976c06f1682393a272390b3790e
%global __provides_exclude_from ^%{_libdir}/%{name}/plugins/.*\.so$
Name:           qstardict
Version:        4.0.0
Release:        1%{?dist}
Summary:        StarDict clone written using Qt
License:        GPL-3.0-or-later
URL:            https://qstardict.ylsoftware.com/
Source0:        https://github.com/a-rodin/qstardict/archive/%{version}/qstardict-%{version}.tar.gz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  glib2-devel
BuildRequires:  libzim-devel
BuildRequires:  make
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtbase-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
QStarDict is a StarDict clone written using Qt. The user interface
is similar to StarDict.

Main features:
* Full support of StarDict dictionaries
* Working from the system tray
* Scanning mouse selection and showing pop-up windows with translation of
selected words
* Translations reformatting
* Pronouncing of the translated words
* Plugins support

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%qmake_qt6 PLUGINS_DIR=%{_libdir}/%{name}/plugins QMAKE_LRELEASE=lrelease-qt6
make %{?_smp_mflags}
%install
make install INSTALL_ROOT=%{buildroot}
install -pDm644 qstardict/qstardict.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
rm -fr %{buildroot}%{_docdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
