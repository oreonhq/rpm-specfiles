%global source0_hash ff9364244c58507cd4073ac22e580a4cded048d416c682496c1b1788ee8a30df

Name:           tilda
Version:        2.0.0
Release:        6%{?dist}
Summary:        A Gtk based drop down terminal for Linux and Unix

# Automatically converted from old format: GPLv2 and MIT - review is highly recommended.
License:        GPL-2.0-only AND LicenseRef-Callaway-MIT
URL:            http://github.com/lanoxx/tilda 
Source0:        https://github.com/lanoxx/%{name}/archive/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libconfuse-devel
BuildRequires:  libX11-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXt-devel
BuildRequires:  vte291-devel

# License GPLv2
Provides:  bundled(eggaccelerators)
Provides:  bundled(xerror)
# License MIT
Provides:  bundled(tomboykeybinder)

%description
Tilda is a Linux terminal taking after the likeness of many classic terminals
from first person shooter games, Quake, Doom and Half-Life (to name a few),
where the terminal has no border and is hidden from the desktop until a key is
pressed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{name}-%{version}

%build
autoreconf -fi
%configure
%make_build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}

%make_install
desktop-file-install --vendor=""                               \
        --dir=%{buildroot}%{_datadir}/applications             \
        --mode 0644                                            \
        --remove-category="Application"                        \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

install -D -p -m 644 %{name}.png \
        %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README.md ChangeLog TODO.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/tilda-dbus.desktop
%{_datadir}/man/man1/tilda.1.gz
%{_metainfodir}/tilda.appdata.xml

%changelog
%autochangelog
