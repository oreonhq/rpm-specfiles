%global source0_hash bcc4976976bfbddbfec3f689f38927fbabc7f7fa611ea252a789583ea14cd1fb
Name:		fcitx-configtool
Version:	0.4.10
Release:        1%{?dist}
Summary:        Gtk+-based configuring tools for Fcitx
License:	GPL-2.0-or-later
URL:		https://github.com/fcitx/fcitx-configtool
Source0:        http://download.fcitx-im.org/fcitx-configtool/%{name}-%{version}.tar.xz
Requires:	fcitx
# oreon:deps
BuildRequires:  cmake
BuildRequires:  fcitx-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  iso-codes-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  unique-devel
BuildRequires:  unique3-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
