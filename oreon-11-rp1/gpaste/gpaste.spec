%global source0_hash 4b9ff7e0a8187433b432d797a566e9d03ca5e8a273a2261f5ecd181d6a15b322
%global alt_name GPaste
Name:           gpaste
Version:        45.12
Release:        1%{?dist}
Summary:        Clipboard management system
License:        BSD-2-Clause
URL:            https://github.com/Keruspe/%{alt_name}/
Source0:        https://www.imagination-land.org/files/%{name}/%{alt_name}-%{version}.tar.xz
Patch0:         gpaste-45.3-GNOME_Shell_49.patch
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%{?systemd_requires}
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gcr-4)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-keybindings)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  systemd-rpm-macros
BuildRequires:  vala
# /oreon:deps
%description
GPaste is a clipboard management system.

This package provides the D-Bus service and the command-line client.

%package libs
Summary:        Library to manage the clipboard history
%description libs
GPaste is a clipboard management system.

This package contains the shared library used by GPaste.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package ui
Summary:        Graphical interface for GPaste
Requires:       %{name} = %{version}-%{release}
Requires:       control-center-filesystem
%{?systemd_requires}
%description ui
GPaste is a clipboard management system.

This package provides a graphical interface for GPaste, as well as GNOME
integration (control center key bindings and search provider).

%package -n gnome-shell-extension-%{name}
Summary:        GNOME Shell extension for GPaste
Requires:       gnome-shell
Requires:       %{name}-ui = %{version}-%{release}
BuildArch:      noarch
%description -n gnome-shell-extension-%{name}
GPaste is a clipboard management system.

This package provides the GNOME Shell extension for GPaste.

%package bash-completion
Summary:        Bash completion for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       zsh
Supplements:    (%{name} and zsh)
%description zsh-completion
Zsh command line completion support for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{alt_name}-%{version}

%build

%meson
%meson_build
%install
%meson_install
install -Dpm 0644 */data/systemd/*.service -t $RPM_BUILD_ROOT%{_userunitdir}/
%find_lang %{alt_name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.GPaste.*.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/org.gnome.GPaste.Ui.appdata.xml
%post

%systemd_user_post org.gnome.GPaste.Preferences.service
%systemd_user_post org.gnome.GPaste.Ui.service
%post ui

%systemd_user_post org.gnome.GPaste.Preferences.service
%systemd_user_post org.gnome.GPaste.Ui.service
%preun

%systemd_user_preun org.gnome.GPaste.Preferences.service
%systemd_user_preun org.gnome.GPaste.Ui.service
%preun ui

%systemd_user_preun org.gnome.GPaste.Preferences.service
%systemd_user_preun org.gnome.GPaste.Ui.service
%files -f %{oreon_filedir}/main.list
%files -n gpaste-libs -f %{oreon_filedir}/gpaste-libs.list
%files -n gpaste-devel -f %{oreon_filedir}/gpaste-devel.list
%files -n gpaste-ui -f %{oreon_filedir}/gpaste-ui.list
%files -n gnome-shell-extension-gpaste -f %{oreon_filedir}/gnome-shell-extension-gpaste.list
%files -n gpaste-bash-completion -f %{oreon_filedir}/gpaste-bash-completion.list
%files -n gpaste-zsh-completion -f %{oreon_filedir}/gpaste-zsh-completion.list

%changelog

%autochangelog
