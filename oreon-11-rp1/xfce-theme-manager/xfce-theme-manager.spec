%global source0_hash 3637984378e7b2a40232809dd0cd116ba8b7090dc47f411cbed3c6ef2b271d44

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%global pkgname Xfce-Theme-Manager
Name:		xfce-theme-manager
Version:	0.3.9
Release:	%autorelease
Summary:	A theme manager for Xfce
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only	
URL:		https://github.com/KeithDHedger/Xfce-Theme-Manager
# wget https://github.com/KeithDHedger/Xfce-Theme-Manager/archive/xfce-theme-manager-0.3.8.tar.gz
Source0:	https://github.com/KeithDHedger/Xfce-Theme-Manager/archive/%{pkgname}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	cairo-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	pkgconfig(gdk-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	xfce4-dev-tools
BuildRequires:	xfconf-devel

%description
A theme manager allowing easy configuration of themes,
window borders, controls, icons and cursors for Xfce

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkgname}-%{version} -p1

%build
#run autoreconf, not needed when upstream moves to  new automake
autoreconf -v -f -i -I.
%configure
make %{?_smp_mflags} xfcethememanager_CFLAGS="%{optflags} -export-dynamic" xfcethememanager_CXXFLAGS="%{optflags} -export-dynamic -Wunused -Wunused-function -Wno-unused-result -fPIC"

%install
make install DESTDIR=%{buildroot} docfilesdir="%{_pkgdocdir}"
desktop-file-install	\
--delete-original	\
--dir=%{buildroot}%{_datadir}/applications	\
--remove-key=Categories	\
--add-category=GTK	\
--add-category=Settings	\
--add-category=DesktopSettings	\
--add-category=X-XFCE-SettingsDialog	\
--add-category=X-XFCE-PersonalSettings	\
--add-category=X-XFCE	\
--set-name="Xfce Theme Manager"	\
%{buildroot}/%{_datadir}/applications/%{pkgname}.desktop

%files
%doc ChangeLog* Xfce-Theme-Manager/resources/docs/gpl-3.0.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{pkgname}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/Xfce-Theme-Manager/scripts
%{_mandir}/man1/%{name}.1.*
%{_mandir}/*/man1/%{name}.1.*

%changelog
%autochangelog
