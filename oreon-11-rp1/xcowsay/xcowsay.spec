%global source0_hash 46ace864ff28d2d21f4b7058f0295e18d0041a120c1078a951fa43c4e0f5c8c5

Name:           xcowsay
Version:        1.6
Release:        9%{?dist}
Summary:        Displays a cute cow and message on your desktop

License:        GPL-3.0-or-later
URL:            http://www.doof.me.uk/xcowsay
Source0:        http://www.nickg.me.uk/files/%{name}-%{version}.tar.gz
Source1:        xcowfortune.desktop
#Patch23:        xcowsay-aarch64.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  gettext
BuildRequires:  dbus-glib-devel
BuildRequires:  desktop-file-utils
Requires:       fortune-mod

%description
xcowsay displays a cute cow and message on your desktop.
The message can be text or images (with xcowdream)
xcowsay can run in daemon mode for sending
your cow message with DBus.
Inspired by the original cowsay.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
#%patch23 -p1 -b .aarch64
iconv -f iso-8859-1 -t utf-8 NEWS -o NEWS

%build
%configure --enable-dbus
make %{?_smp_mflags} 

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%find_lang %{name}

desktop-file-install --vendor=""     \
       --dir=%{buildroot}%{_datadir}/applications/   \
       %{SOURCE1}
# xcowfortune is the only .desktop file because the other program 
#(xcowsay, xcowthink and xcowdream) need an argument

%files -f %{name}.lang
%license COPYING
%doc NEWS README AUTHORS ChangeLog 
%{_bindir}/xcowdream
%{_bindir}/xcowfortune
%{_bindir}/xcowsay
%{_bindir}/xcowthink
%{_datadir}/man/man6/xcowsay.6.gz
%{_datadir}/xcowsay/
%{_datadir}/applications/xcowfortune.desktop

%changelog
%autochangelog
