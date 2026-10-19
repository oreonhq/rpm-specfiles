%global source0_hash c3e1eb985b8ae7ce4e3e28412b7e797ff5db437ccd327e0d852a3c37f17fe456
Name:           maliit-keyboard
Version:        2.3.1
Release:        1%{?dist}
Summary:        Maliit Keyboard 2
License:        LGPL-3.0-only AND LicenseRef-Callaway-BSD
URL:            https://maliit.github.io/
Source0:        https://github.com/maliit/keyboard/archive/%{version}/%{name}-%{version}.tar.gz
Patch1: make-sure-PressArea-gets-reset-when-the-keyboard-hides.patch
# oreon:deps
BuildRequires:  anthy-unicode-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  hunspell-devel
BuildRequires:  libchewing-devel
BuildRequires:  libpinyin-devel
BuildRequires:  maliit-framework-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtfeedback-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtquickcontrols2-devel
# /oreon:deps
%description
Based on Ubuntu Keyboard. Ubuntu Keyboard was a QML and C++ based Keyboard
Plugin for Maliit, based on the Maliit Reference plugin, taking into account the
special UI/UX requests of Ubuntu Phone.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir keyboard-%{version}
%oreon_prep
%build

%cmake -Denable-presage=OFF
%cmake_build
%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/doc/maliit-keyboard
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
