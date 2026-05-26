# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 0ebd5cdef01547787cbc3697ae758c57db1eec10eab613704d4a17b27685ae00
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           mousetweaks
Version:        3.32.0
Release:        19%{?dist}
Summary:        Mouse accessibility support for the GNOME desktop
# Automatically converted from old format: GPLv3 and GFDL - review is highly recommended.
License:        GPL-3.0-only AND LicenseRef-Callaway-GFDL
URL:            https://wiki.gnome.org/Projects/Mousetweaks
Source0:        http://download.gnome.org/sources/mousetweaks/3.32/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gnome-doc-utils
BuildRequires:  pkgconfig
BuildRequires:  gtk3-devel >= 3.0.0
BuildRequires:  libXcursor-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXfixes-devel
BuildRequires:  gsettings-desktop-schemas-devel

%description
The Mousetweaks package provides mouse accessibility enhancements for
the GNOME desktop, such as performing various clicks without using any
hardware button. The options can be accessed through the Accessibility
tab of the Mouse Preferences of GNOME Control Center or through command-line.


%prep
%oreon_verify_sources
%setup -q

%build
%configure
%make_build


%install
%make_install

%find_lang mousetweaks --with-gnome

%files -f mousetweaks.lang
%doc COPYING README NEWS
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/mousetweaks.convert
%{_datadir}/glib-2.0/schemas/org.gnome.mousetweaks.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.mousetweaks.gschema.xml

%{_bindir}/mousetweaks
%{_datadir}/mousetweaks
%doc %{_mandir}/man1/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.32.0-19
- Prepare for Oreon 11 (RP1)
