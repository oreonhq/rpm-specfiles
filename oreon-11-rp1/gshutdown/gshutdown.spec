%global source0_hash bb316be18e3573f983aff5a038603ed10a9df9dd9c7efde65b759aaf1221169f

Name:		gshutdown
Version:	0.2        
Release:	39%{?dist}
Summary:	GShutDown is an advanced shut down utility for GNOME

License:	GPLv2+
URL:		http://gshutdown.tuxfamily.org/
Source0:	http://gshutdown.tuxfamily.org/release/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:	libglade2-devel, desktop-file-utils
BuildRequires:	libnotify-devel, glib2-devel, gettext
BuildRequires: make

Patch0: gshutdown-0.2.libnotify-api.patch
Patch1: gshutdown-0.2.explicitlink.patch
Patch2: gshutdown-0.2-glib.patch
Patch3: gshutdown-0.2-format-security.patch
Patch4: gshutdown-c99.patch

%description
GShutdown is an advanced shutdown utility which
allows you to schedule the shutdown or the restart
of your computer, or logout your actual session.
Also can be use under Xfce and KDE.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
%patch -P0 -p1 -b .libnotify-api
%patch -P1 -p1 -b .explicitlink
%patch -P2 -p1 -b .glib
%patch -P3 -p1
%patch -P4 -p1

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

desktop-file-install					\
	--vendor ""					\
	--dir $RPM_BUILD_ROOT/%{_datadir}/applications	\
	--mode 0644					\
	$RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/pixmaps/%{name}.png

%changelog
%autochangelog
