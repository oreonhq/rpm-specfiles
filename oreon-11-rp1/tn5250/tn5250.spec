%global source0_hash c9563787de32c92580e18ccc8d79b8a8d5dca5c64b71de94a43bb6448431346d

Summary:   5250 Telnet protocol and Terminal
Name:      tn5250
Version:   0.18.0
Release:   3%{?dist}
# doc/tn5250*.1 are GPLv2+
License:   LGPL-2.1-or-later AND GPL-2.0-or-later
URL:       https://github.com/tn5250/tn5250
Source:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:   xt5250.desktop
Requires:  dialog
Requires:  xterm
Requires:  hicolor-icon-theme
BuildRequires: make
BuildRequires: gcc
BuildRequires: ncurses-devel
BuildRequires: openssl-devel
BuildRequires: desktop-file-utils
BuildRequires: libtool

%description
tn5250 is an implementation of the 5250 Telnet protocol.
It provides the 5250 library and a 5250 terminal emulation.

%package devel
Summary: Development tools for the 5250 protocol
Requires: ncurses-devel
Requires: openssl-devel
Requires: %{name} = %{version}-%{release}

%description devel
Libraries and header files to use with lib5250.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

autoreconf -vfi

%build
%configure --disable-static --disable-silent-rules

%make_build

%install
%make_install

mkdir -p %{buildroot}/%{_datadir}/%{name}
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/{48x48,64x64}/apps
install -m644 -p termcaps/linux/5250.tcap %{buildroot}/%{_datadir}/%{name}
install -m644 -p termcaps/linux/5250.terminfo %{buildroot}/%{_datadir}/%{name}
install -m644 -p tn5250-48x48.png %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/tn5250.png
install -m644 -p tn5250-62x48.png %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/tn5250.png
install -m644 -p tn5250-48x48.xpm %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/tn5250.xpm
install -m644 -p tn5250-62x48.xpm %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/tn5250.xpm
rm -f %{buildroot}/%{_libdir}/lib5250.la
mkdir -p %{buildroot}/%{_datadir}/applications
desktop-file-install  \
   --dir %{buildroot}/%{_datadir}/applications %{SOURCE1}
cp -pf termcaps/linux/README README.Linux

/usr/bin/tic -o %{buildroot}/%{_datadir}/terminfo termcaps/linux/5250.terminfo

%files
%license COPYING
%doc AUTHORS ChangeLog README*
%{_bindir}/5250keys
%{_bindir}/lp5250d
%{_bindir}/scs2*
%{_bindir}/tn5250
%{_bindir}/xt5250
%{_libdir}/lib5250.so.*
%{_mandir}/man1/lp5250d.1*
%{_mandir}/man1/scs2*.1*
%{_mandir}/man1/tn5250.1*
%{_mandir}/man5/tn5250rc.5*
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}/
%{_datadir}/applications/xt5250.desktop
%{_datadir}/terminfo/5/5250
%{_datadir}/terminfo/x/xterm-5250

%files devel
%{_includedir}/%{name}/
%{_includedir}/%{name}.h
%{_libdir}/lib5250.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
