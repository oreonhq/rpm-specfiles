%global source0_hash 16a37fecd7bbd63ec9de3ec6c0af331cee77d6dfda838a1b1573d6f298474da5

Name:           terminology
Version:        1.13.0
Release:        10%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
Summary:        EFL based terminal emulator
Url:            http://www.enlightenment.org
Source0:        https://download.enlightenment.org/rel/apps/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  desktop-file-utils
BuildRequires:  efl-devel >= 1.26
BuildRequires:  gettext-devel autoconf automake libtool
BuildRequires:  meson
BuildRequires:  ninja-build
Suggests:       terminus-fonts
Suggests:       xorg-x11-fonts-misc

%if 0%{?el8} > 0
ExcludeArch: s390x
%endif

%description
Fast and lightweight terminal emulator using EFL libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%meson
%meson_build

%install
%meson_install

#Remove fonts that already exist in Fedora
rm -rf %{buildroot}%{_datadir}/terminology/fonts/10x20.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/4x6.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/5x7.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/5x8.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/6x10.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/6x12.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/6x13.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/6x9.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/7x13.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/7x14.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/8x13.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/9x15.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/9x18.pcf
rm -rf %{buildroot}%{_datadir}/terminology/fonts/terminus-*

desktop-file-validate %{buildroot}/%{_datadir}/applications/terminology.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc README.md COPYING
%{_mandir}/man1/*
%{_bindir}/tyalpha
%{_bindir}/tybg
%{_bindir}/tycat
%{_bindir}/tyls
%{_bindir}/typop
%{_bindir}/tyq
%{_bindir}/tysend
%{_bindir}/terminology
%{_datadir}/applications/terminology.desktop
%{_datadir}/icons/hicolor/128x128/apps/terminology.png
%{_datadir}/terminology

%changelog
%autochangelog
