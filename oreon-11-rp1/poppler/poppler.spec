%global source1_hash eb030aa6dc372a5e30685ae18519f29c85b39c85827cd6ed959f757e82ce2230
%global source0_hash 8059eadb6805340768f138c465b57f8164c92b4a0773c37ef031ea6c0d987b2e
%global source3_hash 29e56e326f716fe1adfb2454aed6dce891d71186795f835543c560676a599889
%global test_sha 03a4b9eb854a06a83c465e82de601796c458bbe9
%global test_date 2021-01-11
%bcond qt 1
%if %{with qt}
%if %{undefined rhel} || 0%{?rhel} < 10 || (0%{?oreon} >= 11)
%global qt5 1
%endif
%if %{undefined rhel} || 0%{?rhel} >= 10 || (0%{?oreon} >= 11)
%global qt6 1
%endif
%endif
Summary:        PDF rendering library
Name:    poppler
Version: 26.09.0
Release:        1%{?dist}
License: (GPL-2.0-only OR GPL-3.0-only) AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
URL:     https://poppler.freedesktop.org/
Source0:        https://poppler.freedesktop.org/poppler-%{version}.tar.xz
Source1:        https://poppler.freedesktop.org/poppler-%{version}.tar.xz.sig
Source2:        armored-keys.asc
Source3: %{name}-test-%{test_date}-%{test_sha}.tar.xz
Patch1:  poppler-0.90.0-position-independent-code.patch
Patch2:  poppler-21.01.0-glib-introspection.patch
%if 0%{?qt5}
%endif
%if 0%{?qt6}
%endif
Requires: poppler-data
Recommends: font(d050000l)
Recommends: font(standardsymbolsps)
Obsoletes: poppler-glib-demos < 0.60.1-1
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(Gpgmepp)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-ft)
BuildRequires:  pkgconfig(cairo-pdf)
BuildRequires:  pkgconfig(cairo-ps)
BuildRequires:  pkgconfig(cairo-svg)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(poppler-data)
# /oreon:deps
%description
%{name} is a PDF rendering library.

%package devel
Summary: Libraries and headers for poppler
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
You should install the poppler-devel package if you would like to
compile applications based on poppler.

%package glib
Summary: Glib wrapper for poppler
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gobject-introspection
%description glib
%{summary}.

%package glib-devel
Summary: Development files for glib wrapper
Requires: %{name}-glib%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Suggests: %{name}-doc = %{version}-%{release}
%description glib-devel
%{summary}.

%package glib-doc
Summary: Documentation for glib wrapper
BuildArch: noarch
%description glib-doc
%{summary}.

%if 0%{?qt5}
%package qt5
Summary: Qt5 wrapper for poppler
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-qt < 0.90.0-9
%description qt5
%{summary}.

%package qt5-devel
Summary: Development files for Qt5 wrapper
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel
Obsoletes: %{name}-qt-devel < 0.90.0-9
%description qt5-devel
%{summary}.
%endif

%if 0%{?qt6}
%package qt6
Summary: Qt6 wrapper for poppler
Requires: %{name}%{?_isa} = %{version}-%{release}
%description qt6
%{summary}.

%package qt6-devel
Summary: Development files for Qt6 wrapper
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel
%description qt6-devel
%{summary}.
%endif

%package cpp
Summary: Pure C++ wrapper for poppler
Requires: %{name}%{?_isa} = %{version}-%{release}
%description cpp
%{summary}.

%package cpp-devel
Summary: Development files for C++ wrapper
Requires: %{name}-cpp%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description cpp-devel
%{summary}.

%package utils
Summary: Command line utilities for converting PDF files
Requires: %{name}%{?_isa} = %{version}-%{release}
%description utils
Command line tools for manipulating PDF files and converting them to
other formats.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source3_hash}" = "none" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source3_hash}" || { echo "oreon: Source3 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -b 3

chmod -x poppler/CairoFontEngine.cc

%build

%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DENABLE_CMS=lcms2 \
  -DENABLE_DCTDECODER=libjpeg \
  -DENABLE_GTK_DOC=ON \
  -DENABLE_LIBOPENJPEG=openjpeg2 \
%if ! 0%{?qt5}
  -DENABLE_QT5=OFF \
%endif
%if ! 0%{?qt6}
  -DENABLE_QT6=OFF \
%endif
  -DENABLE_UNSTABLE_API_ABI_HEADERS=ON \
  -DENABLE_ZLIB=OFF \
  ..
%cmake_build
%install
%cmake_install
%find_lang pdfsig
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%make_build test
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion poppler)" = "%{version}"
test "$(pkg-config --modversion poppler-cpp)" = "%{version}"
test "$(pkg-config --modversion poppler-glib)" = "%{version}"
%if 0%{?qt5}
test "$(pkg-config --modversion poppler-qt5)" = "%{version}"
%endif
%if 0%{?qt6}
test "$(pkg-config --modversion poppler-qt6)" = "%{version}"
%endif
%ldconfig_scriptlets
%ldconfig_scriptlets glib
%if 0%{?qt5}
%ldconfig_scriptlets qt5
%endif
%if 0%{?qt6}
%ldconfig_scriptlets qt6
%endif
%ldconfig_scriptlets cpp
%files -f %{oreon_filedir}/main.list
%files -n poppler-devel -f %{oreon_filedir}/poppler-devel.list
%files -n poppler-glib -f %{oreon_filedir}/poppler-glib.list
%files -n poppler-glib-devel -f %{oreon_filedir}/poppler-glib-devel.list
%files -n poppler-glib-doc -f %{oreon_filedir}/poppler-glib-doc.list
%files -n poppler-qt5 -f %{oreon_filedir}/poppler-qt5.list
%files -n poppler-qt5-devel -f %{oreon_filedir}/poppler-qt5-devel.list
%files -n poppler-qt6 -f %{oreon_filedir}/poppler-qt6.list
%files -n poppler-qt6-devel -f %{oreon_filedir}/poppler-qt6-devel.list
%files -n poppler-cpp -f %{oreon_filedir}/poppler-cpp.list
%files -n poppler-cpp-devel -f %{oreon_filedir}/poppler-cpp-devel.list
%files -n poppler-utils -f %{oreon_filedir}/poppler-utils.list

%changelog

%autochangelog
