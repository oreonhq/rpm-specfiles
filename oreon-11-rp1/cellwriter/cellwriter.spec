%global source0_hash 17bb07226d4680b565b18a60494cb19cdf9067b427c8df7454c16d809de9963b

Summary: Grid-entry natural handwriting input panel
Name: cellwriter
Version: 1.3.6
Release: 14%{?dist}
License: GPL-2.0-or-later
URL: https://github.com/risujin/cellwriter/
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires: desktop-file-utils
BuildRequires: libXtst-devel
BuildRequires: gtk2-devel
BuildRequires: libgnome-devel
BuildRequires: make

%description
CellWriter is a grid-entry natural handwriting input panel. As 
you write characters into the cells, your writing is instantly 
recognized at the character level. When you press 'Enter' on the 
panel, the input you entered is sent to the currently focused 
application as if typed on the keyboard.

Works well on a Wacom tablet, TabletPC, or any device with a stylus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags} CFLAGS="$CFLAGS -fcommon -std=gnu17" LIBS="$LIBS -lX11 -lm -lXtst -lxml2"

%install
make install DESTDIR="$RPM_BUILD_ROOT" INSTALL="install -p"

desktop-file-install --delete-original \
  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
  ${RPM_BUILD_ROOT}/%{_datadir}/applications/cellwriter.desktop

%files
%doc README COPYING TODO AUTHORS
%{_bindir}/cellwriter
%dir %{_datadir}/cellwriter
%{_datadir}/cellwriter/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/cellwriter.svg
%{_datadir}/pixmaps/cellwriter.xpm
%{_mandir}/*/*

%changelog
%autochangelog
