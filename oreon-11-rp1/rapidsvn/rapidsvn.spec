%global source0_hash bb601784ed4f0e29ec5572ef4120b54343ef2154d4b257b9104aaf2e537d33ad
%global commit 3a564e071c3c792f5d733a9433b9765031f8eed0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           rapidsvn
Version:        0.13.0
Release:        1%{?dist}
Summary:        Graphical interface for the Subversion revision control system
License:        GPL-3.0-or-later
URL:            http://www.rapidsvn.org/
Source0:        https://github.com/RapidSVN/RapidSVN/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:         wxwidgets3.2.patch
Requires:       svncpp = %{version}
# oreon:deps
BuildRequires:  apr-devel
BuildRequires:  apr-util-devel
BuildRequires:  cppunit-devel
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  libxcrypt-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  openldap-devel
BuildRequires:  subversion-devel
BuildRequires:  wxGTK-devel
# /oreon:deps
%description
RapidSVN is a GUI front-end for the Subversion revision control system. It
allows access to most of the features of Subversion through a user-friendly
interface.

%package -n svncpp
Summary:        C++ bindings for the Subversion client library
License:        LGPL-3.0-or-later
BuildRequires:  gcc-c++
BuildRequires:  subversion-devel
BuildRequires:  cppunit-devel
BuildRequires:  gettext
Requires:       subversion
%description -n svncpp
svncpp is a C++ wrapper for the C Subversion client library which abstracts
many parts of the C API and provides an object-oriented programming interface.

%package -n svncpp-devel
Summary:        Development resources for the 'svncpp' library
License:        LGPL-3.0-or-later
Requires:       svncpp = %{version}-%{release}
%description -n svncpp-devel
Development resources for the 'svncpp' C++ client library for Subversion.
Install this package if you need to compile an application that requires the
'svncpp' library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n RapidSVN-%{commit}

%{__cat} <<EOF >rapidsvn.desktop
[Desktop Entry]
Encoding=UTF-8
Name=RapidSVN
GenericName=Subversion client
Comment=Manage Subversion repositories
Exec=rapidsvn
Icon=rapidsvn
Terminal=false
Type=Application
Categories=Development;GNOME;GTK;RevisionControl;
Version=0.9.4
EOF

%build

export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
sed -i s/\#MSGFMT=msgfmt/MSGFMT=msgfmt/ librapidsvn/src/locale/Makefile.am
sed -i '/MSGFMT=python/d' librapidsvn/src/locale/Makefile.am
./autogen.sh
%configure \
        --disable-static \
        --with-svn-lib=%{_libdir} \
        --with-apu-config=%{_bindir}/apu-1-config \
        --with-apr-config=%{_bindir}/apr-1-config \
        --with-docbook-xsl-manpages=%{_datadir}/sgml/docbook/xsl-stylesheets/manpages/docbook.xsl \
        --includedir=%{_includedir}/svncpp
make %{?_smp_mflags} LIBTOOL=/usr/bin/libtool
pushd doc/manpage
make manpage
popd
%install
make install DESTDIR=%{buildroot} LIBTOOL=/usr/bin/libtool
%{__install} -D -m 644 librapidsvn/src/res/bitmaps/rapidsvn_128x128.png %{buildroot}%{_datadir}/pixmaps/rapidsvn.png
%{__install} -d -m 755 %{buildroot}%{_datadir}/applications/
desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications \
        rapidsvn.desktop
%{__install} -D -m 644 doc/manpage/rapidsvn.1 %{buildroot}%{_mandir}/man1/rapidsvn.1
rm -f %{buildroot}%{_libdir}/librapidsvn.{a,la}
rm -f %{buildroot}%{_libdir}/libsvncpp.{a,la}
rm -f %{buildroot}%{_libdir}/librapidsvn.so
%find_lang %{name}
%oreon_autofiles svncpp usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles svncpp-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ldconfig_scriptlets -n svncpp
%files -f %{oreon_filedir}/main.list
%files -n svncpp -f %{oreon_filedir}/svncpp.list
%files -n svncpp-devel -f %{oreon_filedir}/svncpp-devel.list

%changelog

%autochangelog
