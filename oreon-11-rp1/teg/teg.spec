%global source0_hash d643e0b1b4ebe4baaceb398435517c57a67d7aaaa25dc49880d5f50750b089fc

Name:           teg
Version:        0.13.0
Release:        4%{?dist}
Summary:        Turn based strategy game
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/wfx/teg/
Source0:        https://github.com/wfx/teg/archive/refs/tags/%{version}.tar.gz
Source1:        teg.desktop
#Patch0:         teg_libxml.patch
#Patch1:         teg_themes.patch
#Patch2:         teg-disable-help.patch
#Patch3:         teg_fixwording.patch
#Source2:        teg-fix-help.patch

#Patch20:        multiple_definitions.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  goocanvas2-devel
BuildRequires:  xmlto
BuildRequires:  tidy
BuildRequires:  pkgconfig
BuildRequires:  glib2-devel
BuildRequires:  libxml2-devel
BuildRequires:  libgnomeui-devel
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  perl(XML::Parser)
BuildRequires:  desktop-file-utils
Requires(pre):  GConf2
Requires(post): GConf2
Requires(preun): GConf2

%description
Tenes Empanadas Graciela is a clone of Plan Táctico y Estratégico de la 
Guerra, a turn based strategy game. Some rules are different.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q 
#%patch0 -p1
#%patch2 -p1
#%patch3 -p1
for file in AUTHORS COPYING README.md TODO PEOPLE ChangeLog; do
    iconv -f iso8859-1 -t utf-8 < $file > $file.$$
    mv -f $file.$$  $file
done

#%patch20 -p1

%build
./autogen.sh
%global optflags %{optflags} -fcommon
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/gconf/gconf.xml.defaults
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/pixmaps/
mv -f $RPM_BUILD_ROOT/%{_datadir}/pixmaps/teg_icono.png $RPM_BUILD_ROOT/%{_datadir}/pixmaps/teg.png
rm -rf $RPM_BUILD_ROOT/%{_datadir}/gnome/apps/Games/teg.desktop
desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
  --vendor="fedora"               \
%endif
  --dir=$RPM_BUILD_ROOT/%{_datadir}/applications %{SOURCE1}
#patch -p1 < %{SOURCE2}
#mv -f $RPM_BUILD_DIR/%{?buildsubdir}/docs/gnome-help/C/teg.sgml $RPM_BUILD_ROOT/%{_datadir}/gnome/help/teg/C/teg.xml

pushd .
cd $RPM_BUILD_ROOT/%{_datadir}/locale
for a in *.gmo; do
    mv -f $a/LC_MESSAGES/teg@INSTOBJEXT@ $a/LC_MESSAGES/teg.mo
    mv -f $a `basename $a .gmo`
done
popd

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README.md TODO PEOPLE ChangeLog
%{_bindir}/tegrobot
%{_bindir}/tegclient
%{_bindir}/tegserver
%{_datadir}/teg/
%{_datadir}/pixmaps/teg.png
%{_datadir}/gnome/help/teg/
%if 0%{?fedora} && 0%{?fedora} < 19
%{_datadir}/applications/fedora-teg.desktop
%else
%{_datadir}/applications/teg.desktop
%endif
#%{_sysconfdir}/gconf/schemas/teg.schemas
%{_datadir}/glib-2.0/schemas/net.sf.teg.gschema.xml
%{_datadir}/GConf/gsettings/teg.convert

%changelog
%autochangelog
