%global source0_hash 2d93c9afd721aaf8aa9108be20a394578a7965d92c89df7c85cf85e9aa65e832

Name:		tzclock
Version:	3.1.7
Release:	18%{?dist}
Summary:	GTK+ graphical Clock displaying the time around the world

# SPDX confirmed
License:	GPL-2.0-only
URL:		https://theknight.co.uk/
Source0:	http://www.tzclock.org/releases/source/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	desktop-file-utils

%description
TzClock is an X Window GTK+ graphical Clock that can display 
the time around the world. It supports multiple faces showing 
different time zones. 
There is a stopwatch function that is accurate to a tenth of a second, 
plus there are many other nice features for you to discover.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

sed -i.suffix \
	-e 's|^Icon=.*|Icon=tzclock|' \
	%{name}.desktop

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__make} install \
	INSTALL="%{__install} -p" \
	DESTDIR=%{buildroot}

desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications \
	--delete-original \
	%{buildroot}%{_datadir}/applications/tzclock.desktop

%files
%defattr(-,root,root,-)
%doc	AUTHORS
%license	COPYING

%{_bindir}/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/*/tzclock*
%{_datadir}/applications/*desktop

%{_mandir}/man1/*

%changelog
%autochangelog
