%global source0_hash df42aa31d2aa3c14924518f52b736162867c5dc55dd04f18fd320f8b1dc28970
%global enablejit 1
%global build_cxxflags %{build_cxxflags} -std=c++20
%global build_cflags %{build_cflags} -std=gnu17
%global gtkopengl 1
%global __brp_remove_la_files %nil
%undefine _fortify_level
%global qt6 1
%if 0%{?fedora} <= 43 || (0%{?oreon} >= 11)
%global qt4webkit 1
%else
%global qt4webkit 0
%endif
Name:		gambas3
Summary:        IDE based on a basic interpreter with object extensions
Version:	3.22.1
Release:        1%{?dist}
License:	GPL-1.0-or-later
URL:		http://gambas.sourceforge.net/
Source0:        https://gitlab.com/gambas/gambas/-/archive/%{version}/gambas-%{version}.tar.bz2
Source1:	%{name}.desktop
%if 0%{?fedora} >= 35 || (0%{?oreon} >= 11)
%else
%endif
%if 0%{?qt4webkit}
%endif
%ifnarch ppc64le s390x
%endif
%if 0%{?qt6}
%ifnarch ppc64le s390x
%endif
%endif
%if 0%{?fedora} >= 41 || (0%{?oreon} >= 11)
%endif
ExcludeArch:    i686
Patch1:		%{name}-3.12.2-nolintl.patch
Patch2:		%{name}-3.12.2-noliconv.patch
Patch5:		%{name}-3.14.1-gst1.patch
Patch6:		gambas3-3.19.4-c++20-do-not-try-to-override-std-functions.patch
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  alure-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bzip2-devel
BuildRequires:  cairo-devel
BuildRequires:  curl-devel
BuildRequires:  dbus-devel
BuildRequires:  desktop-file-utils
BuildRequires:  dumb-devel
BuildRequires:  fluidsynth-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  glew-devel
BuildRequires:  glibc-devel
BuildRequires:  gmime30-devel
BuildRequires:  gmp-devel
BuildRequires:  gsl-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  gtkglext-devel
BuildRequires:  imlib2-devel
BuildRequires:  libICE-devel
BuildRequires:  libX11-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXft-devel
BuildRequires:  libXtst-devel
BuildRequires:  libffi-devel
BuildRequires:  libgnome-keyring-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libv4l-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  ncurses-devel
BuildRequires:  openal-soft-devel
BuildRequires:  openssl-devel
BuildRequires:  openssl-devel-engine
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  poppler-cpp-devel
BuildRequires:  poppler-devel
BuildRequires:  poppler-glib-devel
BuildRequires:  postgresql-private-devel
BuildRequires:  postgresql-server-devel
BuildRequires:  qt4-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtwebengine-devel
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qtwebengine-devel
BuildRequires:  sqlite-devel
BuildRequires:  sqlite2-devel
BuildRequires:  unixODBC-devel
BuildRequires:  xdg-utils
BuildRequires:  zlib-devel
# /oreon:deps
%description
Gambas3 is a free development environment based on a Basic interpreter
with object extensions, like Visual Basic (but it is NOT a clone !).
With Gambas3, you can quickly design your program GUI, access MySQL/MariaDB
or PostgreSQL databases, pilot KDE applications with DCOP, translate your
program into many languages, create network applications easily, and so
on...

%package runtime
Summary:	Runtime environment for Gambas3
Provides:	%{name}-gb-gui = %{version}-%{release}
Obsoletes:	%{name}-gb-gui <= 3.4
Provides:	%{name}-gb-test = %{version}-%{release}
Obsoletes:	%{name}-gb-test <= 3.15.2
Requires:	%{name}-gb-hash = %{version}-%{release}
%if 0%{?qt4webkit}
%else
Provides:	%{name}-gb-qt4-webkit = %{version}-%{release}
Obsoletes:	%{name}-gb-qt4-webkit <= 3.20.2
Provides:	%{name}-gb-qt4-webview = %{version}-%{release}
Obsoletes:      %{name}-gb-qt4-webview <= 3.20.2
%endif
%description runtime
Gambas3 is a free development environment based on a Basic interpreter
with object extensions, like Visual Basic. This package contains the
runtime components necessary to run programs designed in Gambas3.

%package dev-tools
Summary:	Development environment for Gambas3
Requires:	%{name}-runtime = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel <= 3.15.2
%description dev-tools
The gambas3-dev-tools package contains the tools needed to compile Gambas3
projects without having to install the complete development environment
(gambas3-ide).

%package scripter
Summary:	Scripter program that allows the creation of Gambas3 scripts
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-dev-tools = %{version}-%{release}
Requires:	%{name}-gb-pcre = %{version}-%{release}
%description scripter
This package includes the scripter program that allows the user to
write script files in Gambas.

%package gui
Summary:	Virtual package for Gambas3 packages that just need a gui
Requires:	(gambas3-gb-qt4 = %{version}-%{release} or gambas3-gb-qt5 = %{version}-%{release} or gambas3-gb-gtk = %{version}-%{release} or gambas3-gb-gtk3 = %{version}-%{release})
%description gui
This package is a virtual package that depends on one of the following
packages: gambas3-gb-qt4, gambas3-gb-qt5, gambas3-gb-gtk, gambas3-gb-gtk3.
It is used as a dependency for packages that requires any GUI package (like
gambas3-gb-form).

%package ide
Summary:	The complete Gambas3 Development Environment
License:	GPL-1.0-or-later
Provides:	%{name} = %{version}-%{release}
Requires:	tar, gzip, rpm-build, gettext, wget
Recommends:	pngquant, translate-shell, git, subversion
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-dev-tools = %{version}-%{release}
Requires:	%{name}-gb-clipper = %{version}-%{release}
Requires:	%{name}-gb-db2 = %{version}-%{release}
Requires:	%{name}-gb-db2-form = %{version}-%{release}
Requires:	%{name}-gb-desktop = %{version}-%{release}
Requires:	%{name}-gb-desktop-x11 = %{version}-%{release}
Requires:	%{name}-gb-eval-highlight = %{version}-%{release}
Requires:	%{name}-gb-form = %{version}-%{release}
Requires:	%{name}-gb-form-dialog = %{version}-%{release}
Requires:	%{name}-gb-form-editor = %{version}-%{release}
Requires:	%{name}-gb-form-htmlview = %{version}-%{release}
Requires:	%{name}-gb-form-mdi = %{version}-%{release}
Requires:	%{name}-gb-form-print = %{version}-%{release}
Requires:	%{name}-gb-form-stock = %{version}-%{release}
Requires:	%{name}-gb-form-terminal = %{version}-%{release}
Requires:	%{name}-gb-highlight = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}
%if 0%{enablejit}
Requires:	%{name}-gb-jit = %{version}-%{release}
%endif
Requires:	%{name}-gb-markdown = %{version}-%{release}
Requires:	%{name}-gb-net = %{version}-%{release}
Requires:	%{name}-gb-net-curl = %{version}-%{release}
Requires:	%{name}-gb-settings = %{version}-%{release}
Requires:	%{name}-gb-signal = %{version}-%{release}
Requires:	%{name}-gb-term = %{version}-%{release}
Requires:	%{name}-gb-util = %{version}-%{release}
Requires:	%{name}-gb-util-web = %{version}-%{release}
Requires:	%{name}-gb-gtk3-webview = %{version}-%{release}
Requires:	%{name}-gb-gtk3-wayland = %{version}-%{release}
Requires:	%{name}-gb-gtk3-x11 = %{version}-%{release}
%description ide
This package includes the complete Gambas3 Development Environment.
It pulls in the Gambas3 components necessary for the IDE to function.

%package gb-args
Summary:	Gambas3 component package for args
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-args
%{summary}

%package gb-cairo
Summary:	Gambas3 component package for cairo
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}
%description gb-cairo
%{summary}

%package gb-chart
Summary:	Gambas3 component package for chart
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-form = %{version}-%{release}
%description gb-chart
%{summary}

%package gb-clipper
Summary:	Gambas3 component package for clipper
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-clipper
%{summary}

%package gb-clipper2
Summary:	Gambas3 component package for clipper2
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-clipper2
%{summary}

%package gb-complex
Summary:	Gambas3 component package for complex
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-complex
%{summary}

%package gb-compress
Summary:	Gambas3 component package for compress
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-compress
%{summary}

%package gb-compress-bzlib2
Summary:	Gambas3 component package for compress-bzlib2
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-compress = %{version}-%{release}
%description gb-compress-bzlib2
%{summary}

%package gb-compress-zlib
Summary:	Gambas3 component package for compress-zlib
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-compress = %{version}-%{release}
%description gb-compress-zlib
%{summary}

%package gb-compress-zstd
Summary:	Gambas3 component package for compress-zstd
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-compress = %{version}-%{release}
%description gb-compress-zstd
%{summary}

%package gb-crypt
Summary:	Gambas3 component package for crypt
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-crypt
%{summary}

%package gb-data
Summary:	Gambas3 component package for data
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-data
%{summary}

%package gb-db
Summary:	Gambas3 component package for db
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-db
%{summary}

%package gb-db2
Summary:	Gambas3 component package for db2
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-db2
%{summary}

%package gb-db-form
Summary:	Gambas3 component package for db-form
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-db = %{version}-%{release}
Requires:	%{name}-gb-form = %{version}-%{release}
%description gb-db-form
%{summary}

%package gb-db2-form
Summary:	Gambas3 component package for db2-form
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-db2 = %{version}-%{release}
Requires:	%{name}-gb-form = %{version}-%{release}
%description gb-db2-form
%{summary}

%package gb-db-mysql
Summary:	Gambas3 component package for db-mysql
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-db =	%{version}-%{release}
%description gb-db-mysql
%{summary}

%package gb-db2-mysql
Summary:        Gambas3 component package for db2-mysql
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-db2 = %{version}-%{release}
%description gb-db2-mysql
%{summary}

%package gb-db-odbc
Summary:	Gambas3 component package for db-odbc
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-db =	%{version}-%{release}
%description gb-db-odbc
%{summary}

%package gb-db2-odbc
Summary:	Gambas3 component package for db2-odbc
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-db2 = %{version}-%{release}
%description gb-db2-odbc
%{summary}

%package gb-db-postgresql
Summary:	Gambas3 component package for db-postgresql
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-db =	%{version}-%{release}
%description gb-db-postgresql
%{summary}

%package gb-db2-postgresql
Summary:        Gambas3 component package for db2-postgresql
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-db2 = %{version}-%{release}
%description gb-db2-postgresql
%{summary}

%package gb-db-sqlite2
Summary:	Gambas3 component package for db-sqlite2
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-db =	%{version}-%{release}
%description gb-db-sqlite2
%{summary}

%package gb-db-sqlite3
Summary:	Gambas3 component package for db-sqlite3
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-db =	%{version}-%{release}
%description gb-db-sqlite3
%{summary}

%package gb-db2-sqlite3
Summary:        Gambas3 component package for db2-sqlite3
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-db2 = %{version}-%{release}
%description gb-db2-sqlite3
%{summary}

%package gb-desktop
Summary:	Gambas3 component package for desktop
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}
%description gb-desktop
%{summary}

%package gb-desktop-gnome-keyring
Summary:	Gambas3 component package for GNOME Desktop Keyring
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-desktop = %{version}-%{release}
Provides:	%{name}-gb-desktop-gnome = %{version}-%{release}
Obsoletes:	%{name}-gb-desktop-gnome <= 3.15.2
%description gb-desktop-gnome-keyring
%{summary}

%package gb-desktop-x11
Summary:	Gambas3 component package for X11 desktop
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}
Requires:	%{name}-gb-desktop = %{version}-%{release}
%description gb-desktop-x11
%{summary}

%package gb-dbus
Summary:	Gambas3 component package for dbus
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-dbus
%{summary}

%package gb-dbus-trayicon
Summary:	Gambas3 component package for dbus-trayicon
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-dbus = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}
%description gb-dbus-trayicon
%{summary}

%package gb-eval-highlight
Summary:	Gambas3 component package for eval highlight
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-eval-highlight
%{summary}

%package gb-form
Summary:	Gambas3 component package for form
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gui = %{version}-%{release}
%description gb-form
%{summary}

%package gb-form-dialog
Summary:	Gambas3 component package for form-dialog
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-form = %{version}-%{release}
%description gb-form-dialog
%{summary}

%package gb-form-editor
Summary:	Gambas3 component package for form-editor
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-eval-highlight = %{version}-%{release}
Requires:	%{name}-gb-util = %{version}-%{release}
Requires:	%{name}-gb-form = %{version}-%{release}
%description gb-form-editor
%{summary}

%package gb-form-htmlview
Summary:	Gambas3 component package for form-htmlview
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-form = %{version}-%{release}
%description gb-form-htmlview
%{summary}

%package gb-form-mdi
Summary:	Gambas3 component package for form-mdi
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-form = %{version}-%{release}
Requires:	%{name}-gb-settings = %{version}-%{release}
%description gb-form-mdi
%{summary}

%package gb-form-print
Summary:	Gambas3 component package for form-print
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-form = %{version}-%{release}
%description gb-form-print
%{summary}

%package gb-form-stock
Summary:	Gambas3 component package for form-stock
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-form-stock
%{summary}

%package gb-form-terminal
Summary:	Gambas3 component package for form-terminal
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-form = %{version}-%{release}
Requires:	%{name}-gui = %{version}-%{release}
Requires:	%{name}-gb-term = %{version}-%{release}
%description gb-form-terminal
%{summary}

%package gb-gmp
Summary:	Gambas3 component package for gmp
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-gmp
%{summary}

%package gb-gsl
Summary:	Gambas3 component package for gsl
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-gsl
%{summary}

%package gb-gtk
Summary:	Gambas3 component package for gtk
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}
%description gb-gtk
%{summary}

%package gb-gtk-opengl
Summary:	Gambas3 component package for gtk-opengl
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-gtk = %{version}-%{release}
Requires:	%{name}-gb-opengl = %{version}-%{release}
%description gb-gtk-opengl
%{summary}

%package gb-gtk3
Summary:	Gambas3 component package for gtk3
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}
Requires:	%{name}-gb-gtk3-wayland
Requires:	%{name}-gb-gtk3-x11
%description gb-gtk3
%{summary}.

%package gb-gtk3-opengl
Summary:	Gambas3 component package for gtk3-opengl
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-gtk3 = %{version}-%{release}
Requires:	%{name}-gb-opengl = %{version}-%{release}
%description gb-gtk3-opengl
%{summary}.

%package gb-gtk3-wayland
Summary:	Gambas3 component package for gtk3-wayland
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-gtk3 = %{version}-%{release}
Requires:	%{name}-gb-qt5 = %{version}-%{release}
%description gb-gtk3-wayland
%{summary}.

%package gb-gtk3-webview
Summary:	Gambas3 component package for gtk3-webview
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-gtk3 = %{version}-%{release}
%description gb-gtk3-webview
%{summary}.

%package gb-gtk3-x11
Summary:	Gambas3 component package for gtk3-x11
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-gtk3 = %{version}-%{release}
Requires:	%{name}-gb-qt5 = %{version}-%{release}
%description gb-gtk3-x11
%{summary}.

%package gb-hash
Summary:	Gambas3 component package that implements hashing functions
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-hash
Gambas3 component package that implements the Md5(), Sha1(),
Sha256(), and Sha512() functions.

%package gb-highlight
Summary:	Gambas3 component package for syntax highlighting
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}
Requires:	%{name}-gb-pcre = %{version}-%{release}
%description gb-highlight
%{summary}.

%package gb-httpd
Summary:	Gambas3 component package for httpd
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-httpd
%{summary}.

%package gb-image
Summary:	Gambas3 component package for image
License:	GPL-2.0-only OR QPL-1.0
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-image
%{summary}

%package gb-image-effect
Summary:	Gambas3 component package for image-effect
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}
%description gb-image-effect
%{summary}

%package gb-image-imlib
Summary:	Gambas3 component package for image-imlib
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}
%description gb-image-imlib
%{summary}

%package gb-image-io
Summary:	Gambas3 component package for image-io
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}
%description gb-image-io
%{summary}

%package gb-inotify
Summary:	Gambas3 component package for inotify
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-inotify
%{summary}

%if 0%{enablejit}
%package gb-jit
Summary:	Gambas3 component package for jit
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	gcc
%description gb-jit
%{summary}
%endif

%package gb-libxml
Summary:	Gambas3 component package for libxml
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-libxml
%{summary}

%package gb-logging
Summary:	Gambas3 component package for logging
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-logging
%{summary}

%package gb-map
Summary:	Gambas3 component package for map
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-net-curl = %{version}-%{release}
Requires:	%{name}-gb-net = %{version}-%{release}
%description gb-map
%{summary}.

%package gb-markdown
Summary:	Gambas3 component package for markdown
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-markdown
%{summary}.

%package gb-media
Summary:	Gambas3 component package for media
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}
%description gb-media
%{summary}

%package gb-media-form
Summary:	Gambas3 component package for media-form
Requires:	%{name}-gb-media = %{version}-%{release}
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gui = %{version}-%{release}
%description gb-media-form
%{summary}

%package gb-memcached
Summary:	Gambas3 component package for memcached
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-net = %{version}-%{release}
%description gb-memcached
%{summary}.

%package gb-mime
Summary:	Gambas3 component package for mime
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-mime
%{summary}

%package gb-mysql
Summary:	Gambas3 component package for mysql
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-db = %{version}-%{release}
Requires:	%{name}-gb-db-mysql = %{version}-%{release}
%description gb-mysql
%{summary}

%package gb-ncurses
Summary:	Gambas3 component package for ncurses
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-ncurses
%{summary}

%package gb-net
Summary:	Gambas3 component package for net
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-net
%{summary}

%package gb-net-curl
Summary:	Gambas3 component package for net.curl
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-net = %{version}-%{release}
%description gb-net-curl
%{summary}

%package gb-net-pop3
Summary:	Gambas3 component package for net-pop3
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-net = %{version}-%{release}
Requires:	%{name}-gb-mime = %{version}-%{release}
%description gb-net-pop3
%{summary}

%package gb-net-smtp
Summary:	Gambas3 component package for net-smtp
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-net = %{version}-%{release}
%description gb-net-smtp
%{summary}

%package gb-openal
Summary:	Gambas3 component package for openal
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-openal
%{summary}

%package gb-opengl
Summary:	Gambas3 component package for opengl
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}
%description gb-opengl
%{summary}

%package gb-opengl-glu
Summary:	Gambas3 component package for opengl-glu
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-opengl = %{version}-%{release}
%description gb-opengl-glu
%{summary}

%package gb-opengl-glsl
Summary:	Gambas3 component package for opengl-glsl
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-opengl = %{version}-%{release}
%description gb-opengl-glsl
%{summary}

%package gb-opengl-sge
Summary:	Gambas3 component package for opengl-sge
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-opengl = %{version}-%{release}
%description gb-opengl-sge
%{summary}

%package gb-openssl
Summary:	Gambas3 component package for openssl
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-openssl
%{summary}

%package gb-option
Summary:	Gambas3 component package for option
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-option
%{summary}

%package gb-pcre
Summary:	Gambas3 component package for pcre
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-pcre
%{summary}

%package gb-pdf
Summary:	Gambas3 component package for pdf
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}
%description gb-pdf
%{summary}

%package gb-poppler
Summary:	Gambas3 component package for poppler
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}
%description gb-poppler
%{summary}

%package gb-qt4
Summary:	Gambas3 component package for qt4
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}
%description gb-qt4
%{summary}

%package gb-qt4-ext
Summary:	Gambas3 component package for qt4.ext
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-qt4 = %{version}-%{release}
%description gb-qt4-ext
%{summary}

%package gb-qt4-opengl
Summary:	Gambas3 component package for qt4-opengl
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-qt4 = %{version}-%{release}
Requires:	%{name}-gb-opengl = %{version}-%{release}
%description gb-qt4-opengl
%{summary}

%if 0%{?qt4webkit}
%package gb-qt4-webkit
Summary:	Gambas3 component package for qt4-webkit
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-qt4 = %{version}-%{release}
%description gb-qt4-webkit
%{summary}

%package gb-qt4-webview
Summary:	 Gambas3 component package for qt4-webview
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-qt4 = %{version}-%{release}
%description gb-qt4-webview
%{summary}
%endif

%package gb-qt5
Summary:	 Gambas3 component package for qt5
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}
Requires:	%{name}-gb-qt5-wayland
Requires:	%{name}-gb-qt5-x11
%description gb-qt5
%{summary}

%package gb-qt5-ext
Summary:	Gambas3 component package for qt5-ext
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-qt5 = %{version}-%{release}
%description gb-qt5-ext
%{summary}

%package gb-qt5-opengl
Summary:	 Gambas3 component package for qt5-opengl
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-qt5 = %{version}-%{release}
Requires:	%{name}-gb-opengl = %{version}-%{release}
%description gb-qt5-opengl
%{summary}

%package gb-qt5-wayland
Summary:	 Gambas3 component package for qt5-wayland
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-qt5 = %{version}-%{release}
%description gb-qt5-wayland
%{summary}

%package gb-qt5-webkit
Summary:	 Gambas3 component package for qt5-webkit
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-qt5 = %{version}-%{release}
%description gb-qt5-webkit
%{summary}

%package gb-qt5-webview
Summary:	 Gambas3 component package for qt5-webview
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-qt5 = %{version}-%{release}
%description gb-qt5-webview
%{summary}

%package gb-qt5-x11
Summary:	 Gambas3 component package for qt5-x11
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-qt5 = %{version}-%{release}
%description gb-qt5-x11
%{summary}

%if 0%{?qt6}
%package gb-qt6
Summary:	Gambas3 component package for qt6
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}
Requires:	%{name}-gb-qt6-wayland
Requires:	%{name}-gb-qt6-x11
%description gb-qt6
%{summary}

%package gb-qt6-ext
Summary:	Gambas3 component package for qt6-ext
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-qt6 = %{version}-%{release}
%description gb-qt6-ext
%{summary}

%package gb-qt6-opengl
Summary:	Gambas3 component package for qt6-opengl
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-qt6 = %{version}-%{release}
Requires:	%{name}-gb-opengl = %{version}-%{release}
%description gb-qt6-opengl
%{summary}

%package gb-qt6-wayland
Summary:	Gambas3 component package for qt6-wayland
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-qt6 = %{version}-%{release}
%description gb-qt6-wayland
%{summary}

%package gb-qt6-webview
Summary:	Gambas3 component package for qt6-webview
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-qt6 = %{version}-%{release}
%description gb-qt6-webview
%{summary}

%package gb-qt6-x11
Summary:	Gambas3 component package for qt6-x11
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-qt6 = %{version}-%{release}
%description gb-qt6-x11
%{summary}
%endif

%package gb-report
Summary:	Gambas3 component package for report
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-form = %{version}-%{release}
%description gb-report
%{summary}

%package gb-report2
Summary:	Gambas3 component package for report2
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-form = %{version}-%{release}
%description gb-report2
%{summary}

%package gb-scanner
Summary:	Gambas3 component package for scanner
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-scanner
%{summary}

%package gb-sdl
Summary:	Gambas3 component package for sdl
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}
Requires:	%{name}-gb-image-io = %{version}-%{release}
Requires:	dejavu-sans-fonts
%description gb-sdl
%{summary}

%package gb-sdl-sound
Summary:	Gambas3 component package for sdl-sound
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-sdl-sound
%{summary}

%package gb-sdl2
Summary:	Gambas3 component for sdl2
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}
%description gb-sdl2
%{summary}

%package gb-sdl2-audio
Summary:	Gambas3 component for sdl2-audio
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-sdl2-audio
%{summary}

%package gb-settings
Summary:	Gambas3 component package for settings
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-settings
%{summary}

%package gb-signal
Summary:	Gambas3 component package for signal
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-signal
%{summary}

%package gb-term
Summary:	Gambas3 component package for term
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-term
%{summary}

%package gb-term-form
Summary:	Gambas3 component package for term-form
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-term = %{version}-%{release}
%description gb-term-form
%{summary}

%package gb-util
Summary:	Gambas3 component package for util
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-util
%{summary}

%package gb-util-web
Summary:	Gambas3 component package for util web
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-util-web
%{summary}

%package gb-v4l
Summary:	Gambas3 component package for v4l
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}
%description gb-v4l
%{summary}

%package gb-vb
Summary:	Gambas3 component package for vb
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-vb
%{summary}

%package gb-web
Summary:	Gambas3 component package for web
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-util-web = %{version}-%{release}
%description gb-web
%{summary}

%package gb-web-feed
Summary:	Gambas3 component package for web-feed
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-web = %{version}-%{release}
Requires:	%{name}-gb-xml = %{version}-%{release}
Requires:	%{name}-gb-util = %{version}-%{release}
%description gb-web-feed
%{summary}

%package gb-web-form
Summary:	Gambas3 component package for web-form
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-web = %{version}-%{release}
Requires:	%{name}-gb-util-web = %{version}-%{release}
Requires:	%{name}-gb-util = %{version}-%{release}
%description gb-web-form
%{summary}

%package gb-web-gui
Summary:	Gambas3 component package for web-gui
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-web = %{version}-%{release}
Requires:	%{name}-gb-util = %{version}-%{release}
Requires:	%{name}-gb-util-web = %{version}-%{release}
Requires:	%{name}-gb-signal = %{version}-%{release}
%description gb-web-gui
%{summary}

%package gb-xml
Summary:	Gambas3 component package for xml
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-xml
%{summary}

%package gb-xml-html
Summary:	Gambas3 component package for xml.html
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-xml = %{version}-%{release}
%description gb-xml-html
%{summary}

%package gb-xml-rpc
Summary:	Gambas3 component package for xml.rpc
Requires:	%{name}-runtime = %{version}-%{release}
%description gb-xml-rpc
%{summary}

%package gb-xml-xslt
Summary:	Gambas3 component package for xml.xslt
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-xml = %{version}-%{release}
%description gb-xml-xslt
%{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n gambas-%{version}
%patch -P 1 -p1 -b .nolintl
%patch -P 2 -p1 -b .noliconv
%patch -P 5 -p1 -b .gst1
%patch -P 6 -p1 -b .c++20
for i in `find . |grep acinclude.m4`; do
	sed -i 's|$AM_CFLAGS -O3|$AM_CFLAGS|g' $i
	sed -i 's|$AM_CXXFLAGS -Os -fno-omit-frame-pointer|$AM_CXXFLAGS|g' $i
	sed -i 's|$AM_CFLAGS -Os|$AM_CFLAGS|g' $i
	sed -i 's|$AM_CFLAGS -O0|$AM_CFLAGS|g' $i
	sed -i 's|$AM_CXXFLAGS -O0|$AM_CXXFLAGS|g' $i
done
# Need this for gcc44
sed -i 's|-fno-exceptions||g' gb.db.sqlite3/acinclude.m4
./reconf-all

# clean up some spurious exec perms
chmod -x main/gbx/gbx_local.h
chmod -x main/gbx/gbx_subr_file.c
chmod -x gb.qt4/src/CContainer.cpp
chmod -x main/lib/option/getoptions.*
chmod -x main/lib/option/main.c

%build

%if 0%{?fedora} <= 37 || (0%{?oreon} >= 11)
MY_CFLAGS=`echo %{build_cflags} | sed -e 's/-Wp,-D_FORTIFY_SOURCE=2//g' | sed -e 's/-Wp,-U_FORTIFY_SOURCE,-D_FORTIFY_SOURCE=3//g'`
%endif
%configure \
	--disable-silent-rules \
	--datadir="%{_datadir}" \
	--enable-intl \
	--enable-conv \
	--enable-qt4 \
	--enable-kde \
	--enable-net \
	--enable-curl \
	--enable-postgresql \
	--enable-mysql \
	--enable-sqlite3 \
	--enable-sdl \
	--enable-vb \
	--enable-pdf \
	--with-bzlib2-libraries=%{_libdir} \
	--with-crypt-libraries=%{_libdir} \
	--with-curl-libraries=%{_libdir} \
	--with-desktop-libraries=%{_libdir} \
	--with-ffi-includes=`pkg-config libffi --variable=includedir` \
	--with-ffi-libraries=`pkg-config libffi --variable=libdir` \
	--with-intl-libraries=%{_libdir} \
	--with-conv-libraries=%{_libdir} \
	--with-gettext-libraries=%{_libdir} \
	--with-gtk-libraries=%{_libdir} \
	--with-gtk_svg-libraries=%{_libdir} \
	--with-image-libraries=%{_libdir} \
	--with-kde-libraries=%{_libdir} \
	--with-mysql-includes=%{_includedir}/mysql \
	--with-mysql-libraries=%{_libdir}/mariadb \
	--with-net-libraries=%{_libdir} \
	--with-odbc-libraries=%{_libdir} \
	--with-opengl-libraries=%{_libdir} \
	--with-pcre-libraries=%{_libdir} \
	--with-poppler-libraries=%{_libdir} \
	--with-postgresql-libraries=%{_libdir} \
	--with-qt4-libraries=%{_libdir} \
	--with-qt5-libraries=%{_libdir} \
	--with-qtopengl-libraries=%{_libdir} \
	--with-sdl-libraries=%{_libdir} \
	--with-sdl_sound-libraries=%{_libdir} \
	--with-smtp-libraries=%{_libdir} \
	--with-sqlite2-libraries=%{_libdir} \
	--with-sqlite3-libraries=%{_libdir} \
	--with-v4l-libraries=%{_libdir} \
	--with-xml-libraries=%{_libdir} \
	--with-xslt-libraries=%{_libdir} \
	--with-zlib-libraries=%{_libdir} \
%if 0%{?fedora} <= 37 || (0%{?oreon} >= 11)
	AM_CFLAGS="$MY_CFLAGS" AM_CXXFLAGS="$MY_CFLAGS" CC="%{build_cc} $MY_CFLAGS"
%else
	AM_CFLAGS="%{build_cflags}" AM_CXXFLAGS="%{build_cflags}" CC="%{build_cc} %{build_cflags}"
%endif
for i in main; do
	sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' $i/libtool
	sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' $i/libtool
done
%make_build -C gb.qt5
%make_build
%install
export PATH=%{buildroot}%{_bindir}:$PATH
%make_install
%make_install
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/%{name}/examples/
install -m0644 -p ./app/src/%{name}/.icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications	\
  %{SOURCE1}
find %{buildroot}%{_datadir}/%{name}/ -type d -name .svn -exec rm -rf {} 2>/dev/null ';' || :
rm -rf %{buildroot}%{_libdir}/%{name}/gb.la %{buildroot}%{_libdir}/%{name}/gb.so*
rm -rf %{buildroot}%{_libdir}/%{name}/*.a
mkdir -p %{buildroot}%{_datadir}/mime/packages/
install -m 0644 -p app/mime/application-x-gambasscript.xml %{buildroot}%{_datadir}/mime/packages/
install -m 0644 -p main/mime/application-x-gambas3.xml %{buildroot}%{_datadir}/mime/packages/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gambas3-runtime -f %{oreon_filedir}/gambas3-runtime.list
%files -n gambas3-dev-tools -f %{oreon_filedir}/gambas3-dev-tools.list
%files -n gambas3-scripter -f %{oreon_filedir}/gambas3-scripter.list
%files -n gambas3-gui -f %{oreon_filedir}/gambas3-gui.list
%files -n gambas3-ide -f %{oreon_filedir}/gambas3-ide.list
%files -n gambas3-gb-args -f %{oreon_filedir}/gambas3-gb-args.list
%files -n gambas3-gb-cairo -f %{oreon_filedir}/gambas3-gb-cairo.list
%files -n gambas3-gb-chart -f %{oreon_filedir}/gambas3-gb-chart.list
%files -n gambas3-gb-clipper -f %{oreon_filedir}/gambas3-gb-clipper.list
%files -n gambas3-gb-clipper2 -f %{oreon_filedir}/gambas3-gb-clipper2.list
%files -n gambas3-gb-complex -f %{oreon_filedir}/gambas3-gb-complex.list
%files -n gambas3-gb-compress -f %{oreon_filedir}/gambas3-gb-compress.list
%files -n gambas3-gb-compress-bzlib2 -f %{oreon_filedir}/gambas3-gb-compress-bzlib2.list
%files -n gambas3-gb-compress-zlib -f %{oreon_filedir}/gambas3-gb-compress-zlib.list
%files -n gambas3-gb-compress-zstd -f %{oreon_filedir}/gambas3-gb-compress-zstd.list
%files -n gambas3-gb-crypt -f %{oreon_filedir}/gambas3-gb-crypt.list
%files -n gambas3-gb-data -f %{oreon_filedir}/gambas3-gb-data.list
%files -n gambas3-gb-db -f %{oreon_filedir}/gambas3-gb-db.list
%files -n gambas3-gb-db2 -f %{oreon_filedir}/gambas3-gb-db2.list
%files -n gambas3-gb-db-form -f %{oreon_filedir}/gambas3-gb-db-form.list
%files -n gambas3-gb-db2-form -f %{oreon_filedir}/gambas3-gb-db2-form.list
%files -n gambas3-gb-db-mysql -f %{oreon_filedir}/gambas3-gb-db-mysql.list
%files -n gambas3-gb-db2-mysql -f %{oreon_filedir}/gambas3-gb-db2-mysql.list
%files -n gambas3-gb-db-odbc -f %{oreon_filedir}/gambas3-gb-db-odbc.list
%files -n gambas3-gb-db2-odbc -f %{oreon_filedir}/gambas3-gb-db2-odbc.list
%files -n gambas3-gb-db-postgresql -f %{oreon_filedir}/gambas3-gb-db-postgresql.list
%files -n gambas3-gb-db2-postgresql -f %{oreon_filedir}/gambas3-gb-db2-postgresql.list
%files -n gambas3-gb-db-sqlite2 -f %{oreon_filedir}/gambas3-gb-db-sqlite2.list
%files -n gambas3-gb-db-sqlite3 -f %{oreon_filedir}/gambas3-gb-db-sqlite3.list
%files -n gambas3-gb-db2-sqlite3 -f %{oreon_filedir}/gambas3-gb-db2-sqlite3.list
%files -n gambas3-gb-desktop -f %{oreon_filedir}/gambas3-gb-desktop.list
%files -n gambas3-gb-desktop-gnome-keyring -f %{oreon_filedir}/gambas3-gb-desktop-gnome-keyring.list
%files -n gambas3-gb-desktop-x11 -f %{oreon_filedir}/gambas3-gb-desktop-x11.list
%files -n gambas3-gb-dbus -f %{oreon_filedir}/gambas3-gb-dbus.list
%files -n gambas3-gb-dbus-trayicon -f %{oreon_filedir}/gambas3-gb-dbus-trayicon.list
%files -n gambas3-gb-eval-highlight -f %{oreon_filedir}/gambas3-gb-eval-highlight.list
%files -n gambas3-gb-form -f %{oreon_filedir}/gambas3-gb-form.list
%files -n gambas3-gb-form-dialog -f %{oreon_filedir}/gambas3-gb-form-dialog.list
%files -n gambas3-gb-form-editor -f %{oreon_filedir}/gambas3-gb-form-editor.list
%files -n gambas3-gb-form-htmlview -f %{oreon_filedir}/gambas3-gb-form-htmlview.list
%files -n gambas3-gb-form-mdi -f %{oreon_filedir}/gambas3-gb-form-mdi.list
%files -n gambas3-gb-form-print -f %{oreon_filedir}/gambas3-gb-form-print.list
%files -n gambas3-gb-form-stock -f %{oreon_filedir}/gambas3-gb-form-stock.list
%files -n gambas3-gb-form-terminal -f %{oreon_filedir}/gambas3-gb-form-terminal.list
%files -n gambas3-gb-gmp -f %{oreon_filedir}/gambas3-gb-gmp.list
%files -n gambas3-gb-gsl -f %{oreon_filedir}/gambas3-gb-gsl.list
%files -n gambas3-gb-gtk -f %{oreon_filedir}/gambas3-gb-gtk.list
%files -n gambas3-gb-gtk-opengl -f %{oreon_filedir}/gambas3-gb-gtk-opengl.list
%files -n gambas3-gb-gtk3 -f %{oreon_filedir}/gambas3-gb-gtk3.list
%files -n gambas3-gb-gtk3-opengl -f %{oreon_filedir}/gambas3-gb-gtk3-opengl.list
%files -n gambas3-gb-gtk3-wayland -f %{oreon_filedir}/gambas3-gb-gtk3-wayland.list
%files -n gambas3-gb-gtk3-webview -f %{oreon_filedir}/gambas3-gb-gtk3-webview.list
%files -n gambas3-gb-gtk3-x11 -f %{oreon_filedir}/gambas3-gb-gtk3-x11.list
%files -n gambas3-gb-hash -f %{oreon_filedir}/gambas3-gb-hash.list
%files -n gambas3-gb-highlight -f %{oreon_filedir}/gambas3-gb-highlight.list
%files -n gambas3-gb-httpd -f %{oreon_filedir}/gambas3-gb-httpd.list
%files -n gambas3-gb-image -f %{oreon_filedir}/gambas3-gb-image.list
%files -n gambas3-gb-image-effect -f %{oreon_filedir}/gambas3-gb-image-effect.list
%files -n gambas3-gb-image-imlib -f %{oreon_filedir}/gambas3-gb-image-imlib.list
%files -n gambas3-gb-image-io -f %{oreon_filedir}/gambas3-gb-image-io.list
%files -n gambas3-gb-inotify -f %{oreon_filedir}/gambas3-gb-inotify.list
%files -n gambas3-gb-jit -f %{oreon_filedir}/gambas3-gb-jit.list
%files -n gambas3-gb-libxml -f %{oreon_filedir}/gambas3-gb-libxml.list
%files -n gambas3-gb-logging -f %{oreon_filedir}/gambas3-gb-logging.list
%files -n gambas3-gb-map -f %{oreon_filedir}/gambas3-gb-map.list
%files -n gambas3-gb-markdown -f %{oreon_filedir}/gambas3-gb-markdown.list
%files -n gambas3-gb-media -f %{oreon_filedir}/gambas3-gb-media.list
%files -n gambas3-gb-media-form -f %{oreon_filedir}/gambas3-gb-media-form.list
%files -n gambas3-gb-memcached -f %{oreon_filedir}/gambas3-gb-memcached.list
%files -n gambas3-gb-mime -f %{oreon_filedir}/gambas3-gb-mime.list
%files -n gambas3-gb-mysql -f %{oreon_filedir}/gambas3-gb-mysql.list
%files -n gambas3-gb-ncurses -f %{oreon_filedir}/gambas3-gb-ncurses.list
%files -n gambas3-gb-net -f %{oreon_filedir}/gambas3-gb-net.list
%files -n gambas3-gb-net-curl -f %{oreon_filedir}/gambas3-gb-net-curl.list
%files -n gambas3-gb-net-pop3 -f %{oreon_filedir}/gambas3-gb-net-pop3.list
%files -n gambas3-gb-net-smtp -f %{oreon_filedir}/gambas3-gb-net-smtp.list
%files -n gambas3-gb-openal -f %{oreon_filedir}/gambas3-gb-openal.list
%files -n gambas3-gb-opengl -f %{oreon_filedir}/gambas3-gb-opengl.list
%files -n gambas3-gb-opengl-glu -f %{oreon_filedir}/gambas3-gb-opengl-glu.list
%files -n gambas3-gb-opengl-glsl -f %{oreon_filedir}/gambas3-gb-opengl-glsl.list
%files -n gambas3-gb-opengl-sge -f %{oreon_filedir}/gambas3-gb-opengl-sge.list
%files -n gambas3-gb-openssl -f %{oreon_filedir}/gambas3-gb-openssl.list
%files -n gambas3-gb-option -f %{oreon_filedir}/gambas3-gb-option.list
%files -n gambas3-gb-pcre -f %{oreon_filedir}/gambas3-gb-pcre.list
%files -n gambas3-gb-pdf -f %{oreon_filedir}/gambas3-gb-pdf.list
%files -n gambas3-gb-poppler -f %{oreon_filedir}/gambas3-gb-poppler.list
%files -n gambas3-gb-qt4 -f %{oreon_filedir}/gambas3-gb-qt4.list
%files -n gambas3-gb-qt4-ext -f %{oreon_filedir}/gambas3-gb-qt4-ext.list
%files -n gambas3-gb-qt4-opengl -f %{oreon_filedir}/gambas3-gb-qt4-opengl.list
%files -n gambas3-gb-qt5 -f %{oreon_filedir}/gambas3-gb-qt5.list
%files -n gambas3-gb-qt5-ext -f %{oreon_filedir}/gambas3-gb-qt5-ext.list
%files -n gambas3-gb-qt5-opengl -f %{oreon_filedir}/gambas3-gb-qt5-opengl.list
%files -n gambas3-gb-qt5-wayland -f %{oreon_filedir}/gambas3-gb-qt5-wayland.list
%files -n gambas3-gb-qt5-webkit -f %{oreon_filedir}/gambas3-gb-qt5-webkit.list
%files -n gambas3-gb-qt5-webview -f %{oreon_filedir}/gambas3-gb-qt5-webview.list
%files -n gambas3-gb-qt5-x11 -f %{oreon_filedir}/gambas3-gb-qt5-x11.list
%files -n gambas3-gb-qt6 -f %{oreon_filedir}/gambas3-gb-qt6.list
%files -n gambas3-gb-qt6-ext -f %{oreon_filedir}/gambas3-gb-qt6-ext.list
%files -n gambas3-gb-qt6-opengl -f %{oreon_filedir}/gambas3-gb-qt6-opengl.list
%files -n gambas3-gb-qt6-wayland -f %{oreon_filedir}/gambas3-gb-qt6-wayland.list
%files -n gambas3-gb-qt6-webview -f %{oreon_filedir}/gambas3-gb-qt6-webview.list
%files -n gambas3-gb-qt6-x11 -f %{oreon_filedir}/gambas3-gb-qt6-x11.list
%files -n gambas3-gb-report -f %{oreon_filedir}/gambas3-gb-report.list
%files -n gambas3-gb-report2 -f %{oreon_filedir}/gambas3-gb-report2.list
%files -n gambas3-gb-scanner -f %{oreon_filedir}/gambas3-gb-scanner.list
%files -n gambas3-gb-sdl -f %{oreon_filedir}/gambas3-gb-sdl.list
%files -n gambas3-gb-sdl-sound -f %{oreon_filedir}/gambas3-gb-sdl-sound.list
%files -n gambas3-gb-sdl2 -f %{oreon_filedir}/gambas3-gb-sdl2.list
%files -n gambas3-gb-sdl2-audio -f %{oreon_filedir}/gambas3-gb-sdl2-audio.list
%files -n gambas3-gb-settings -f %{oreon_filedir}/gambas3-gb-settings.list
%files -n gambas3-gb-signal -f %{oreon_filedir}/gambas3-gb-signal.list
%files -n gambas3-gb-term -f %{oreon_filedir}/gambas3-gb-term.list
%files -n gambas3-gb-term-form -f %{oreon_filedir}/gambas3-gb-term-form.list
%files -n gambas3-gb-util -f %{oreon_filedir}/gambas3-gb-util.list
%files -n gambas3-gb-util-web -f %{oreon_filedir}/gambas3-gb-util-web.list
%files -n gambas3-gb-v4l -f %{oreon_filedir}/gambas3-gb-v4l.list
%files -n gambas3-gb-vb -f %{oreon_filedir}/gambas3-gb-vb.list
%files -n gambas3-gb-web -f %{oreon_filedir}/gambas3-gb-web.list
%files -n gambas3-gb-web-feed -f %{oreon_filedir}/gambas3-gb-web-feed.list
%files -n gambas3-gb-web-form -f %{oreon_filedir}/gambas3-gb-web-form.list
%files -n gambas3-gb-web-gui -f %{oreon_filedir}/gambas3-gb-web-gui.list
%files -n gambas3-gb-xml -f %{oreon_filedir}/gambas3-gb-xml.list
%files -n gambas3-gb-xml-html -f %{oreon_filedir}/gambas3-gb-xml-html.list
%files -n gambas3-gb-xml-rpc -f %{oreon_filedir}/gambas3-gb-xml-rpc.list
%files -n gambas3-gb-xml-xslt -f %{oreon_filedir}/gambas3-gb-xml-xslt.list

%changelog

%autochangelog
