%global source0_hash 1dba8f470d2b12517e7b86d83cd2ebf13eb57ff1a01a4f2d2d156cf5194d97b6

# Review: https://bugzilla.redhat.com/show_bug.cgi?id=173105
%global _hardened_build 1

%global minorversion 1.2
%global xfceversion 4.20

Name:           xfce4-battery-plugin
Version:        1.2.0
Release:        %autorelease
Summary:        Battery monitor for the Xfce panel

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-battery-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  meson
Requires:       xfce4-panel >= %{xfceversion}

%description
A battery monitor plugin for the Xfce panel, compatible with APM and ACPI.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%meson
%meson_build

%install
%meson_install

# remove la file
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# make sure debuginfo is generated properly
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS COPYING.LIB README.md
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/*/*

%changelog
%autochangelog
