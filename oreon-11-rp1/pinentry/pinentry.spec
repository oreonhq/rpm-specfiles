%global source2_hash 6f57d0e17fefd2238bd037aebf03efa960641629dd61dd9d47f122a829f6e375
%global source1_hash fe7be7d1c2eb75b1d80cdc1e157974b5bd438b5c67f3000c88c0278f3964acba
%global source0_hash c2970f16d6afb66ecddfca767d743936c86239bff936eed7fd7597a678414b63
Name:    pinentry
Version: 1.3.3
Release:        1%{?dist}
Summary:        Collection of simple PIN or passphrase entry dialogs
License: GPL-2.0-or-later
URL:     https://www.gnupg.org/
Source0:        https://gnupg.org/ftp/gcrypt/pinentry/%{name}-%{version}.tar.bz2
Source1:        https://gnupg.org/ftp/gcrypt/pinentry/%{name}-%{version}.tar.bz2.sig
Source2: https://gnupg.org/signature_key.asc
Patch1: pinentry-1.1.1-coverity.patch
Source10: pinentry-wrapper
%if %{with gtk2}
%endif
%if %{with kf6}
%endif
Provides: %{name}-curses = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gnupg2
BuildRequires:  libassuan-devel
BuildRequires:  libcap-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(KF6GuiAddons)
BuildRequires:  pkgconfig(KF6WindowSystem)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(gcr-4)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libsecret-1)
# /oreon:deps
%description
Pinentry is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.
This package contains the curses (text) based version of the PIN entry dialog.

%package gnome3
Summary: Passphrase/PIN entry dialog for GNOME 3
Requires: %{name} = %{version}-%{release}
Provides: %{name}-gui = %{version}-%{release}
%description gnome3
Pinentry is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.
This package contains the GNOME 3 version of the PIN entry dialog.

%if %{with gtk2}
%package gtk
Summary: Passphrase/PIN entry dialog based on GTK+
Requires: %{name} = %{version}-%{release}
Provides: %{name}-gui = %{version}-%{release}
Provides: pinentry-gtk2 = %{version}-%{release}
%description gtk
Pinentry is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.
This package contains the GTK GUI based version of the PIN entry dialog.
%endif

%package qt
Summary: Passphrase/PIN entry dialog based on Qt6
Requires: %{name} = %{version}-%{release}
Provides: %{name}-gui = %{version}-%{release}
Obsoletes: pinentry-qt4 < 0.8.0-2
Obsoletes: pinentry-qt5 < 1.2.1-7
Provides:  pinentry-qt6 = %{version}-%{release}
%if ! %{with gtk2}
Obsoletes: %{name}-gtk < %{version}-%{release}
%endif
%description qt
Pinentry is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.
This package contains the Qt6 GUI based version of the PIN entry dialog.

%package emacs
Summary: Passphrase/PIN entry dialog based on emacs
Requires: %{name} = %{version}-%{release}
%description emacs
Pinentry is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.
This package contains the emacs based version of the PIN entry dialog.

%package tty
Summary: Passphrase/PIN entry dialog in tty
Requires: %{name} = %{version}-%{release}
%description tty
Pinentry is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.
This package contains the tty version of the PIN entry dialog.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

export ACLOCAL_PATH=/usr/share/gettext/m4/
autoreconf -fiv
%configure \
  --disable-rpath \
  --disable-dependency-tracking \
  --without-libcap \
  --disable-pinentry-fltk \
  --enable-pinentry-gnome3 \
%if %{with gtk2}
  --enable-pinentry-gtk2 \
%else
  --disable-pinentry-gtk2 \
%endif
  --enable-pinentry-qt \
  --disable-pinentry-qt5 \
  --enable-pinentry-emacs \
  --enable-pinentry-tty \
  --enable-libsecret
%make_build
%install
%make_install
%if %{with gtk2}
ln -s pinentry-gtk-2 $RPM_BUILD_ROOT%{_bindir}/pinentry-gtk
%endif
ln -s pinentry-qt $RPM_BUILD_ROOT%{_bindir}/pinentry-qt4
ln -s pinentry-qt $RPM_BUILD_ROOT%{_bindir}/pinentry-qt5
install -p -m755 -D %{SOURCE10} $RPM_BUILD_ROOT%{_bindir}/pinentry
rm -fv $RPM_BUILD_ROOT%{_infodir}/dir
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnupg.pinentry-qt.desktop
install -d %{buildroot}%{_datadir}/pixmaps
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n pinentry-gnome3 -f %{oreon_filedir}/pinentry-gnome3.list
%files -n pinentry-gtk -f %{oreon_filedir}/pinentry-gtk.list
%files -n pinentry-qt -f %{oreon_filedir}/pinentry-qt.list
%files -n pinentry-emacs -f %{oreon_filedir}/pinentry-emacs.list
%files -n pinentry-tty -f %{oreon_filedir}/pinentry-tty.list

%changelog

%autochangelog
