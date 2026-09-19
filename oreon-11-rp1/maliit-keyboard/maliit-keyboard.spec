%global source0_hash c3e1eb985b8ae7ce4e3e28412b7e797ff5db437ccd327e0d852a3c37f17fe456

Name:           maliit-keyboard
Version:        2.3.1
Release:        12%{?dist}
Summary:        Maliit Keyboard 2

# Automatically converted from old format: LGPLv3 and BSD - review is highly recommended.
License:        LGPL-3.0-only AND LicenseRef-Callaway-BSD
URL:            https://maliit.github.io/
Source0:        https://github.com/maliit/keyboard/archive/%{version}/%{name}-%{version}.tar.gz 

BuildRequires: cmake
BuildRequires: gcc-c++

BuildRequires: maliit-framework-devel >= 2.3.0
BuildRequires: glib2-devel
BuildRequires: hunspell-devel
BuildRequires: gettext

BuildRequires: anthy-unicode-devel
BuildRequires: libpinyin-devel
BuildRequires: libchewing-devel

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: qt5-qtfeedback-devel
BuildRequires: qt5-qtquickcontrols2-devel

# Upstream patches
# https://github.com/maliit/keyboard/pull/187
Patch1: make-sure-PressArea-gets-reset-when-the-keyboard-hides.patch

%description
Based on Ubuntu Keyboard. Ubuntu Keyboard was a QML and C++ based Keyboard
Plugin for Maliit, based on the Maliit Reference plugin, taking into account the
special UI/UX requests of Ubuntu Phone.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n keyboard-%{version} -p1

%build
%cmake -Denable-presage=OFF

%cmake_build

%install
%cmake_install

rm -rf %{buildroot}%{_datadir}/doc/maliit-keyboard
%find_lang %{name}

%files -f %{name}.lang
%license COPYING.BSD COPYING.LGPL COPYING
%doc README.md
%{_bindir}/maliit-keyboard
%dir %{_libdir}/maliit/
%{_libdir}/maliit/keyboard2/
%{_libdir}/maliit/plugins/
%dir %{_datadir}/maliit/
%{_datadir}/maliit/keyboard2/
%{_datadir}/glib-2.0/schemas/org.maliit.keyboard.maliit.gschema.xml
%{_datadir}/applications/com.github.maliit.keyboard.desktop
%{_metainfodir}/com.github.maliit.keyboard.metainfo.xml

%changelog
%autochangelog
