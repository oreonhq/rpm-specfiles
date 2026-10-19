%global source0_hash 6b96a8844463300c10b9692a0a5edad8236eec9e84342f575f83d4fc89331228
%global geany_docdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}
%undefine  py_auto_byte_compile
Name:      geany
Version:   2.1.0
Release:        1%{?dist}
Summary:        A fast and lightweight IDE using GTK3
License:   GPL-2.0-or-later AND LicenseRef-Callaway-MIT
URL:       http://www.geany.org/
Source0:        http://download.geany.org/%{name}-%{version}.tar.bz2
Requires: vte291%{?_isa}
Requires: geany-libgeany = %{version}-%{release}
Provides: bundled(scintilla) = 5.5.4
Provides: bundled(lexilla) = 5.4.2
Recommends: xterm
Obsoletes: geany-themes
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  pango-devel
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  python3-docutils
# /oreon:deps
%description
Geany is a small and fast integrated development environment with basic
features and few dependencies to other packages or Desktop Environments.

Some features:
- Syntax highlighting
- Code completion
- Code folding
- Construct completion/snippets
- Auto-closing of XML and HTML tags
- Call tips
- Support for Many languages like C, Java, PHP, HTML, Python, Perl, Pascal
- symbol lists and symbol name auto-completion
- Code navigation
- Simple project management
- Plugin interface

%package libgeany
Summary:   Core functions of Geany
Requires:  geany = %{version}-%{release}
%description libgeany
This package contains the core functions of Geany which will be used by
Geany plugins.

%package devel
Summary:   Header files for building Geany plug-ins
Requires:  geany = %{version}-%{release}
Requires:  pkgconfig gtk3-devel
%description devel
This package contains the header files and pkg-config file needed for building
Geany plug-ins. You do not need to install this package to use Geany.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# remove waf since this isn't needed for the build, we're building the package
# with autotools
rm -f waf
rm -f wscript

%build

RST2HTML=/usr/bin/rst2html-3
%configure --docdir=%{geany_docdir} --enable-gtk3
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT DOCDIR=$RPM_BUILD_ROOT/%{geany_docdir}
rm -f $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.ico
desktop-file-install --delete-original \
        --dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
        --mode 0644                                             \
        $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
find $RPM_BUILD_ROOT -name "*.la" -delete
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
BugReportURL: https://sourceforge.net/p/geany/feature-requests/739/
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">geany.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <description>
    <p>
      Geany is a small and lightweight Integrated Development Environment.
      It was developed to provide a small and fast IDE.
      Another goal was to be as independent as possible from a KDE or GNOME -
      Geany only requires the GTK3 runtime libraries.
    </p>
  <!-- FIXME: Probably needs another paragraph or two -->
  </description>
  <url type="homepage">http://www.geany.org/</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/geany/a.png</screenshot>
    <screenshot>https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/geany/b.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n geany-libgeany -f %{oreon_filedir}/geany-libgeany.list
%files -n geany-devel -f %{oreon_filedir}/geany-devel.list

%changelog

%autochangelog
