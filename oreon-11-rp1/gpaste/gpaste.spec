%global source0_hash 514f29c3b6ea130836561ed2e864f1f2cc08ff62219708d082418d642ce83307

%global alt_name GPaste

Name:           gpaste
Version:        45.3
Release:        4%{?dist}
Summary:        Clipboard management system

License:        BSD-2-Clause
URL:            https://github.com/Keruspe/%{alt_name}/
Source0:        https://www.imagination-land.org/files/%{name}/%{alt_name}-%{version}.tar.xz
# Fix GNOME 49 support (see https://github.com/Keruspe/GPaste/commit/c67a4df)
Patch0:         gpaste-45.3-GNOME_Shell_49.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gcr-4)
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
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%{?systemd_requires}
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

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

%files
%doc AUTHORS NEWS README.md THANKS
%{_bindir}/%{name}-client
%dir %{_libexecdir}/%{name}/
%{_libexecdir}/%{name}/gpaste-daemon
%{_datadir}/dbus-1/services/org.gnome.GPaste.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_userunitdir}/org.gnome.GPaste.service
%{_mandir}/man1/*.1.*

%files libs -f %{alt_name}.lang
%license COPYING
%{_libdir}/girepository-1.0/%{alt_name}*.typelib
%{_libdir}/lib%{name}*.so.*

%files devel
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/*
%{_includedir}/%{name}-2/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files ui
%{_libexecdir}/%{name}/%{name}-preferences
%{_libexecdir}/%{name}/%{name}-ui
%{_datadir}/applications/org.gnome.GPaste.*.desktop
%{_datadir}/dbus-1/services/org.gnome.GPaste.*.service
%{_datadir}/gnome-control-center/keybindings/*.xml
%{_datadir}/gnome-shell/search-providers/*.ini
%{_datadir}/metainfo/org.gnome.GPaste.Ui.appdata.xml
%{_userunitdir}/org.gnome.GPaste.Ui.service
%{_userunitdir}/org.gnome.GPaste.Preferences.service

%files -n gnome-shell-extension-%{name}
%{_datadir}/gnome-shell/extensions/GPaste@gnome-shell-extensions.gnome.org/

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}-client

%files zsh-completion
%{_datadir}/zsh/site-functions/_%{name}-client

%changelog
%autochangelog
