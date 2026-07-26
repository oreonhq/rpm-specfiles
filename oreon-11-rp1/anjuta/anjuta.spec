%global source0_hash 42a93130ed3ee02d064a7094e94e1ffae2032b3f35a87bf441e37fc3bb3a148f

# The Python templates in /usr/share/anjuta/project can not be byte-compiled.
%global _python_bytecompile_errors_terminate_build 0

%if 0%{?fedora}
%global with_python3 1
%else
%global with_python3 0
%endif

Name:           anjuta
Epoch:          1
Version:        3.34.0
Release:        30%{?dist}
Summary:        GNOME IDE for various programming languages (including C/C++, Python, Vala and JavaScript)

License:        GPL-2.0-or-later
URL:            http://www.anjuta.org/
Source0:        http://download.gnome.org/sources/anjuta/3.34/%{name}-%{version}.tar.xz
Patch0:         cpp-java.patch
Patch1:         webkit-4.1.patch
Patch2:         autoconf-2.72.patch
Patch3:         pointer-types.patch

BuildRequires:  autogen
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  devhelp-devel >= 3.0.0
BuildRequires:  gettext
BuildRequires:  glade-devel
BuildRequires:  graphviz-devel
BuildRequires:  gtksourceview3-devel >= 2.91.8
BuildRequires:  intltool
BuildRequires:  libgda5-devel >= 5.1.0
BuildRequires:  libgdl-devel >= 2.91.4
BuildRequires:  libuuid-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  neon-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Locale::gettext)
BuildRequires:  perl(XML::Parser)
%if 0%{?with_python3}
BuildRequires:  python3-devel
%else
BuildRequires:  python-devel
%endif
BuildRequires:  sqlite-devel
BuildRequires:  subversion-devel
BuildRequires:  vala-devel
BuildRequires:  vte291-devel
BuildRequires:  libxml2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  gnome-common
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  gtk-doc

Requires:       autogen
Requires:       gdb >= 7.0
Requires:       git
Requires:       hicolor-icon-theme
Requires:       libgda5-sqlite >= 5.1.0
Requires:       automake
Requires:       autoconf
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Anjuta DevStudio is a versatile software development studio featuring
a number of advanced programming facilities including project
management, application wizard, interactive debugger, source editor,
version control, GUI designer, profiler and many more tools. It
focuses on providing simple and usable user interface, yet powerful
for efficient development.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains development files for %{name}.

%package libs
Summary:        Libraries for %{name}

%description libs
This package contains library files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P 0 -p0 -b .cpp-java
%patch -P 1 -p1 -b .webkit
%patch -P 2 -p1 -b .autoconf
%patch -P 3 -p0 -b .pointer

%build
autoreconf -fi
%if 0%{?with_python3}
export PYTHON=%{__python3}
%endif
%configure \
  --disable-compile-warnings \
  --disable-schemas-compile \
  --disable-silent-rules \
  --disable-static \
  --enable-introspection \
  --enable-plugin-devhelp \
  --enable-plugin-glade \
  --enable-plugin-subversion

# Omit unused direct shared library dependencies.
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags}

%install
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -delete

# Update the screenshot shown in the software center
#
# NOTE: It would be *awesome* if this file was pushed upstream.
#
# See http://people.freedesktop.org/~hughsient/appdata/#screenshots for more details.
#
appstream-util replace-screenshots $RPM_BUILD_ROOT%{_datadir}/metainfo/anjuta.appdata.xml \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/anjuta/a.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/anjuta/b.png 

# Remove lib64 rpaths
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/anjuta
for f in $RPM_BUILD_ROOT%{_libdir}/anjuta/*.so ; do
    chrpath --delete $f
done

# Use %%doc instead.
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%find_lang %{name} --all-name --with-gnome

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/anjuta.desktop

%files -f %{name}.lang
%doc AUTHORS
%doc MAINTAINERS
%doc NEWS
%doc ROADMAP
%{_bindir}/%{name}
%{_bindir}/%{name}-launcher
%{_bindir}/%{name}-tags
%{_datadir}/applications/anjuta.desktop
%{_datadir}/icons/hicolor/*/apps/anjuta.png
%{_datadir}/icons/hicolor/*/mimetypes/application-x-anjuta.png
%{_datadir}/icons/hicolor/scalable/apps/anjuta.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-anjuta.svg
%{_datadir}/icons/hicolor/symbolic/apps/anjuta-symbolic.svg
%{_datadir}/metainfo/anjuta.appdata.xml
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/anjuta/
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta*.gschema.xml
%{_datadir}/pixmaps/anjuta/
%{_mandir}/man1/anjuta.1*
%{_mandir}/man1/anjuta-launcher.1*

%files devel
%doc doc/ScintillaDoc.html
%{_libdir}/libanjuta-3.so
%{_libdir}/pkgconfig/libanjuta-3.0.pc
%{_datadir}/gir-1.0/Anjuta-3.0.gir
%{_datadir}/gir-1.0/IAnjuta-3.0.gir

%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%dir %{_datadir}/gtk-doc/html/libanjuta
%doc %{_datadir}/gtk-doc/html/libanjuta/*

%dir %{_includedir}/libanjuta-3.0
%{_includedir}/libanjuta-3.0/libanjuta

%files libs
%license COPYING
%{_libdir}/anjuta/
%{_libdir}/girepository-1.0/Anjuta-3.0.typelib
%{_libdir}/girepository-1.0/IAnjuta-3.0.typelib
%{_libdir}/libanjuta-3.so.*

%changelog
%autochangelog
