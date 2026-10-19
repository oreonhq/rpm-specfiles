%global source0_hash 080aa631459c941fa18f0facd0265e7d94e3dcf1a0104e62777797e0b2cfe81c
Name:           pop-gtk-theme
Version:        5.5.1
Release:        1%{?dist}
Summary:        Pop GTK Theme
License:        GPL-3.0-only AND LGPL-2.1-only AND CC-BY-SA-4.0
URL:            https://github.com/pop-os/gtk-theme
Source0:        https://github.com/pop-os/gtk-theme/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          0001-fix-gtk4-include-some-missing-assets-in-gresource.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  glib2-devel
BuildRequires:  meson
BuildRequires:  sassc
# /oreon:deps
%description
The Pop theme for GTK.

# gtk2
%package -n pop-gtk2-theme
Summary:        Pop GTK 2 Theme
Requires:       gtk2
Requires:       gtk-murrine-engine
Supplements:    (pop-session and gtk2)
%description -n pop-gtk2-theme
%{summary}.

%package -n pop-gtk3-theme
Summary:        Pop GTK 3 Theme
Supplements:    (pop-session and gtk3)
%description -n pop-gtk3-theme
%{summary}.

%package -n pop-gtk4-theme
Summary:        Pop GTK 4 Theme
Supplements:    (pop-session and gtk4)
%description -n pop-gtk4-theme
%{summary}.

%package -n pop-gnome-shell-theme
Summary:        Pop GNOME Shell Theme
Requires:       gnome-shell
%description -n pop-gnome-shell-theme
%{summary}.

%package -n pop-sound-theme
Summary:        Pop sound theme
License:        CC-BY-SA-4.0
%description -n pop-sound-theme
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gtk-theme-%{version}
%oreon_prep
%build

%meson -Dgnome-shell-gresource=true
%meson_build
%install
%meson_install
%oreon_autofiles pop-gtk2-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles pop-gtk3-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles pop-gtk4-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles pop-gnome-shell-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles pop-sound-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n pop-gtk2-theme -f %{oreon_filedir}/pop-gtk2-theme.list
%files -n pop-gtk3-theme -f %{oreon_filedir}/pop-gtk3-theme.list
%files -n pop-gtk4-theme -f %{oreon_filedir}/pop-gtk4-theme.list
%files -n pop-gnome-shell-theme -f %{oreon_filedir}/pop-gnome-shell-theme.list
%files -n pop-sound-theme -f %{oreon_filedir}/pop-sound-theme.list

%changelog

%autochangelog
