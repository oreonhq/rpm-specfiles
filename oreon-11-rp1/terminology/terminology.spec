%global source0_hash f354057051b05cffb699e33836a1135db1d4ed8bf954f9b57dc0e93bc307514d
Name:           terminology
Version:        1.14.0
Release:        1%{?dist}
License:        LicenseRef-Callaway-BSD
Summary:        EFL based terminal emulator
Url:            http://www.enlightenment.org
Source0:        https://download.enlightenment.org/rel/apps/%{name}/%{name}-%{version}.tar.xz
Suggests:       terminus-fonts
Suggests:       xorg-x11-fonts-misc
%if 0%{?el8} > 0
ExcludeArch: s390x
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  efl-devel
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  meson
BuildRequires:  ninja-build
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
