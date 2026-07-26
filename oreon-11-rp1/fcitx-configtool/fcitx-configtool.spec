%global source0_hash bcc4976976bfbddbfec3f689f38927fbabc7f7fa611ea252a789583ea14cd1fb

Name:		fcitx-configtool
Version:	0.4.10
Release:	24%{?dist}
Summary:	Gtk+-based configuring tools for Fcitx
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/fcitx/fcitx-configtool
Source0:	http://download.fcitx-im.org/fcitx-configtool/%{name}-%{version}.tar.xz

BuildRequires:	gcc
BuildRequires:	cmake, fcitx-devel, gettext, intltool, libxml2-devel
BuildRequires:	gtk2-devel, iso-codes-devel, libtool, unique-devel
BuildRequires:	gtk3-devel, unique3-devel
Requires:	fcitx

%description
fcitx-config-gtk and fcitx-config-gtk3 are Gtk based configuring tools for
Fcitx.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build
%cmake -DENABLE_GTK3=ON -DENABLE_GTK2=ON
%cmake_build

%install
%cmake_install

%find_lang %{name}

%files -f %{name}.lang
%doc README
%license COPYING
%{_bindir}/*

%changelog
%autochangelog
