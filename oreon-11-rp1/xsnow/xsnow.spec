%global source0_hash b2f786581856347d6ec976182042640f2eba38fbe48aed55f89c14f58272e965
Name:           xsnow
Version:        3.9.4
Release:        1%{?dist}
Summary:        Let it snow on your desktop
License:        GPL-3.0-or-later
URL:            https://sourceforge.net/projects/xsnow/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gsl-devel
BuildRequires:  gtk3-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXt-devel
BuildRequires:  libappstream-glib
BuildRequires:  libxml2-devel
BuildRequires:  make
# /oreon:deps
%description
Xsnow is a X Window application that will snow on the desktop background.
Santa and his reindeer will complete your festive-season feeling.
Xsnow runs in GNOME, KDE, FVWM and desktops that are derived from those.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Fix Makefile
sed -i 's!$(exec_prefix)/games!$(exec_prefix)/bin!' src/Makefile.in

%build

%configure --disable-selfrep
%make_build
%install
%make_install
install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
mv %{buildroot}%{_datadir}/pixmaps/%{name}.svg \
   %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
desktop-file-validate \
%{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
