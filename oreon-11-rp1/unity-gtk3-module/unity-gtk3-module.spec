%global source0_hash 5a78ae6b021aaf35f573a56c7803773b0accdf34112ebfebd00651be87c0e28e

Name:           unity-gtk3-module
Version:        0.0.0+18.04.20171202
Release:        6%{?dist}
Summary:        GTK3 module for exporting old-style menus as GMenuModels

License:        LGPL-3.0-or-later
URL:            https://launchpad.net/unity-gtk-module
Source0:        https://launchpad.net/ubuntu/+archive/primary/+files/unity-gtk-module_0.0.0+18.04.20171202.orig.tar.gz

BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libX11-devel
BuildRequires:  pkgconfig
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  gtk-doc
BuildRequires:  systemd-rpm-macros

Requires:       gtk3%{?_isa}
Requires:       glib2%{?_isa}
Requires:       atk%{?_isa}

%description
Unity GTK3 module exports GTK menu shells over DBus. It provides appmenu
integration used by desktop components such as Plasma workspace integrations.

%package        devel
Summary:        Development files for libunity-gtk3-parser
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gtk3-devel
Requires:       glib2-devel
Requires:       pkgconfig

%description    devel
Headers and pkg-config metadata for the Unity GTK3 menu parser library
(libunity-gtk3-parser).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }mkdir -p %{name}-%{version}
tar -xzf %{SOURCE0} -C %{name}-%{version}
# tests/ is wired in configure.ac + Makefile.am; deleting it without editing breaks automake.
cfg=$(find '%{name}-%{version}' -maxdepth 4 -name configure.ac -print -quit)
test -n "$cfg" || { echo 'unity-gtk3-module: configure.ac not found under %{name}-%{version}' >&2; exit 1; }
top=$(dirname "$cfg")
# Last AC_CONFIG_FILES entry is "tests/autopilot/Makefile])" on one line, not Makefile alone
sed -i '/^[[:space:]]*tests\/Makefile$/d' "$top/configure.ac"
sed -i 's/^[[:space:]]*tests\/autopilot\/Makefile])$/])/' "$top/configure.ac"
sed -i 's/^SUBDIRS = lib src data docs tests$/SUBDIRS = lib src data docs/' "$top/Makefile.am"
rm -rf "$top/tests"
find '%{name}-%{version}' -type f -name '*.py' -delete 2>/dev/null || :
# GCC 15 is stricter about pointer types here
find "$top" -type f -name unity-gtk-menu-item.c -exec sed -i \
  's/icon = g_object_ref (pixbuf);/icon = G_ICON (g_object_ref (pixbuf));/g' {} +
# glib ref keeps GDBusMenuModel*; need GObject + G_MENU_MODEL for -Wincompatible-pointer-types (GCC 15)
find "$top" -type f -path '*/src/main.c' -exec sed -i \
  's/window_data->old_model = g_object_ref (old_menu_model);/window_data->old_model = G_MENU_MODEL (g_object_ref (G_OBJECT (old_menu_model)));/g' {} +

%build
cfg=
for c in $(find "%{_builddir}" -maxdepth 14 -name configure.ac 2>/dev/null); do
  case "$c" in *%{name}-%{version}*) cfg=$c; break;; esac
done
test -n "$cfg" || { echo 'unity-gtk3-module: configure.ac not found for %%build' >&2; exit 1; }
cd "$(dirname "$cfg")"
# Ubuntu orig tarball ships configure.ac only
if test ! -x ./configure; then
  gtkdocize --copy --docdir docs || :
  autoreconf -fiv
fi
%configure --with-gtk=3 --with-gtk-module-dir=%{_libdir}/gtk-3.0/modules
%make_build

%install
cfg=
for c in $(find "%{_builddir}" -maxdepth 14 -name configure.ac 2>/dev/null); do
  case "$c" in *%{name}-%{version}*) cfg=$c; break;; esac
done
test -n "$cfg" || exit 1
top=$(dirname "$cfg")
cd "$top"
%make_install
find '%{buildroot}' -type f -name '*.py' -delete 2>/dev/null || :
# Doc and license live next to configure.ac, not at %%{_builddir} root (%%doc/%%license look there)
install -d %{buildroot}%{_docdir}/%{name} %{buildroot}%{_licensedir}/%{name}
for f in AUTHORS NEWS README; do
  if test -f "$top/$f"; then
    install -p -m644 "$top/$f" %{buildroot}%{_docdir}/%{name}/
  else
    echo "unity-gtk3-module: missing doc file $f under $top" >&2
    exit 1
  fi
done
lic=
for cand in COPYING.LESSER COPYING LICENSE; do
  if test -f "$top/$cand"; then
    lic=$cand
    break
  fi
done
if test -n "$lic"; then
  install -p -m644 "$top/$lic" %{buildroot}%{_licensedir}/%{name}/COPYING.LESSER
else
  echo 'unity-gtk3-module: no COPYING.LESSER COPYING or LICENSE next to configure' >&2
  exit 1
fi

%post
if [ -x %{_bindir}/glib-compile-schemas ]; then
  %{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas >/dev/null 2>&1 || :
fi

%postun
if [ -x %{_bindir}/glib-compile-schemas ]; then
  %{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas >/dev/null 2>&1 || :
fi

%files
%license %{_licensedir}/%{name}/COPYING.LESSER
%doc %{_docdir}/%{name}/AUTHORS
%doc %{_docdir}/%{name}/NEWS
%doc %{_docdir}/%{name}/README
%{_libdir}/gtk-3.0/modules/libunity-gtk-module.so
%{_libdir}/libunity-gtk3-parser.so.*
%exclude %{_libdir}/libunity-gtk3-parser.a
%{_datadir}/glib-2.0/schemas/com.canonical.unity-gtk-module.gschema.xml
%{_datadir}/upstart/sessions/unity-gtk-module.conf
%{_userunitdir}/unity-gtk-module.service

%files devel
%{_includedir}/unity-gtk-parser/
%{_libdir}/libunity-gtk3-parser.so
%{_libdir}/pkgconfig/unity-gtk3-parser.pc

%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.0.0+18.04.20171202-2
- Patch main.c via find so GCC 15 GMenuModel cast always applies

* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.0.0+18.04.20171202-1
- Add unity-gtk3-module package for GTK3 appmenu module support
