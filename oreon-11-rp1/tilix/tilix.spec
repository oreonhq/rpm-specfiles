%global source0_hash be389d199a6796bd871fc662f8a37606a1f84e5429f24e912d116f16c5f0a183
%global gtkd_version 3.11.0
%undefine _package_note_file
%undefine _annotated_build
%undefine _hardened_build
Name:           tilix
Version:        1.9.6
Release:        1%{?dist}
Summary:        Tiling terminal emulator
License:        MPL-2.0 AND GPL-2.0-or-later AND LGPL-3.0-or-later AND LGPL-3.0-only AND GPL-3.0-or-later AND (LGPL-3.0-or-later OR CC-BY-SA-3.0)
URL:            https://github.com/gnunn1/tilix
Source0:        https://github.com/gnunn1/tilix/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          https://github.com/gnunn1/tilix/commit/69fe457b58b58eb6f679bc50ef040d08b40fb65d.patch
Patch:          tilix-support-gtkd-3.11.0.patch
ExclusiveArch:  %{ldc_arches}
Requires:       dbus
Requires:       hicolor-icon-theme
Requires:       gtkd%{?_isa} >= %{gtkd_version}
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/appstreamcli
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  /usr/bin/po4a-translate
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  ldc
BuildRequires:  meson
BuildRequires:  pkgconfig(gtkd-3)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(vted-3)
BuildRequires:  pkgconfig(x11)
# /oreon:deps
%description
Tilix is a tiling terminal emulator with the following features:

 - Layout terminals in any fashion by splitting them horizontally or vertically
 - Terminals can be re-arranged using drag and drop both within and between
   windows
 - Terminals can be detached into a new window via drag and drop
 - Input can be synchronized between terminals so commands typed in one
   terminal are replicated to the others
 - The grouping of terminals can be saved and loaded from disk
 - Terminals support custom titles
 - Color schemes are stored in files and custom color schemes can be created by
   simply creating a new file
 - Transparent background
 - Supports notifications when processes are completed out of view

The application was written using GTK 3 and an effort was made to conform to
GNOME Human Interface Guidelines (HIG).

%package        nautilus
Summary:        Tilix extension for Nautilus
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       nautilus-python%{?_isa}
%description    nautilus
This package provides a Nautilus extension that adds the 'Open in Tilix'
option to the right-click context menu in Nautilus.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%if 0%{?flatpak}
sed -i -e "/^Exec=/ s|/usr/bin|%{_bindir}|" data/dbus/com.gexperts.Tilix.service
%endif

%build

export DFLAGS="%{_d_optflags} --allinst"
%meson
%meson_build
%if 0%{?flatpak}
gcc %optflags %__global_ldflags -o tilix-flatpak-toolbox experimental/flatpak/tilix-flatpak-toolbox.c
%endif
cp -a data/icons/LICENSE LICENSE-data-icons
cp -a source/x11/LICENSE LICENSE-source-x11
%install
%meson_install
%if 0%{?flatpak}
install -m 755 tilix-flatpak-toolbox $RPM_BUILD_ROOT%{_bindir}
%endif
%find_lang tilix --with-man
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/com.gexperts.Tilix.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/com.gexperts.Tilix.desktop
%files -f %{oreon_filedir}/main.list
%files -n tilix-nautilus -f %{oreon_filedir}/tilix-nautilus.list

%changelog

%autochangelog
