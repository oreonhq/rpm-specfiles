%global source0_hash 42a93130ed3ee02d064a7094e94e1ffae2032b3f35a87bf441e37fc3bb3a148f
%global _python_bytecompile_errors_terminate_build 0
%global with_python3 0
Name:           anjuta
Epoch:          1
Version:        3_34_0
Release:        1%{?dist}
Summary:        GNOME IDE for various programming languages (including C/C++, Python, Vala and JavaScript)
License:        GPL-2.0-or-later
URL:            http://www.anjuta.org/
Source0:        http://download.gnome.org/sources/anjuta/3.34/%{name}-%{version}.tar.xz
Patch0:         cpp-java.patch
Patch1:         webkit-4.1.patch
Patch2:         autoconf-2.72.patch
Patch3:         pointer-types.patch
%if 0%{?with_python3}
%else
%endif
Requires:       autogen
Requires:       gdb >= 7.0
Requires:       git
Requires:       hicolor-icon-theme
Requires:       libgda5-sqlite >= 5.1.0
Requires:       automake
Requires:       autoconf
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  autogen
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  devhelp-devel
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glade-devel
BuildRequires:  gnome-common
BuildRequires:  gobject-introspection-devel
BuildRequires:  graphviz-devel
BuildRequires:  gtk-doc
BuildRequires:  gtksourceview3-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  libgda5-devel
BuildRequires:  libgdl-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  neon-devel
BuildRequires:  perl(Locale::gettext)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl-generators
BuildRequires:  python3-devel
BuildRequires:  sqlite-devel
BuildRequires:  subversion-devel
BuildRequires:  vala-devel
BuildRequires:  vte291-devel
# /oreon:deps
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
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' libtool
make %{?_smp_mflags}
%install
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -delete
appstream-util replace-screenshots $RPM_BUILD_ROOT%{_datadir}/metainfo/anjuta.appdata.xml \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/anjuta/a.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/anjuta/b.png 
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/anjuta
for f in $RPM_BUILD_ROOT%{_libdir}/anjuta/*.so ; do
    chrpath --delete $f
done
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}
%find_lang %{name} --all-name --with-gnome
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/anjuta.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
