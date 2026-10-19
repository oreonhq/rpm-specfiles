%global source0_hash 862a8caf8d3822b62bc584ed17ba53d1a61733b92d3d5ba29e1be47eadf8f061
%global _privatelibs lib(objrenderer|parsers|pgconnector|pgmodeler|pgmodeler_ui|utils)\\.so
%global __provides_exclude (%{_privatelibs})
%global __requires_exclude (%{_privatelibs})
Name:             pgmodeler
Version:          1.2.3
Release:        1%{?dist}
Summary:        PostgreSQL Database Modeler
License:          GPL-3.0-only
URL:              http://pgmodeler.io/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:          %{name}.desktop
Source2:          pgmodeler-mime-dbm.xml
Requires:         hicolor-icon-theme
Requires:         shared-mime-info
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libXext-devel
BuildRequires:  libappstream-glib
BuildRequires:  libpq-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  moreutils
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
# /oreon:deps
%description
PostgreSQL Database Modeler, or simply, pgModeler is an
open source tool for modeling databases that merges the classical
concepts of entity-relationship diagrams with specific features that
only PostgreSQL implements. The pgModeler translates the models created
by the user to SQL code and apply them onto database clusters (Version
9.x).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%qmake_qt6 \
 PREFIX=%{_prefix} \
 BINDIR=%{_bindir} \
 PRIVATEBINDIR=%{_libexecdir} \
 PLUGINSDIR=%{_libdir}/%{name}/plugins \
 SHAREDIR=%{_datarootdir}/%{name} \
 DOCDIR=%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}} \
 PRIVATELIBDIR=%{_libdir}/%{name} \
 %{name}.pro
%make_build
%install
%make_install INSTALL_ROOT=%{buildroot}
desktop-file-install --mode 644 --dir %{buildroot}%{_datadir}/applications/ %{SOURCE1}
convert -resize 256x256 pgmodeler_logo.png - | sponge pgmodeler_logo.png
install -p -dm 755 %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/ %{buildroot}%{_datadir}/mime/packages/
install -p -m 644 assets/conf/%{name}_logo.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
install -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/mime/packages/%{name}.xml
mkdir -p %{buildroot}%{_libdir}/%{name}/plugins
install -Dp -m 644 %{name}.appdata.xml %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
rm -f %{buildroot}/%{_docdir}/%{name}/LICENSE
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
