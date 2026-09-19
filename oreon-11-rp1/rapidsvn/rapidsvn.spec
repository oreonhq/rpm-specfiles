%global source0_hash bb601784ed4f0e29ec5572ef4120b54343ef2154d4b257b9104aaf2e537d33ad

%global commit 3a564e071c3c792f5d733a9433b9765031f8eed0
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           rapidsvn
Version:        0.13.0
Release:        0.20220212git%{shortcommit}%{?dist}
Summary:        Graphical interface for the Subversion revision control system

License:        GPL-3.0-or-later
URL:            http://www.rapidsvn.org/

Source0:        https://github.com/RapidSVN/RapidSVN/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:         wxwidgets3.2.patch

# Has to be a manual requirement, because the library version appears to not
# be being bumped upstream on API changes - well, at least RapidSVN 0.9.2
# has unresolved symbols if run against svncpp from the 0.9.1 distribution
Requires:       svncpp = %{version}

BuildRequires: make
BuildRequires:  apr-devel, apr-util-devel
BuildRequires:  libtool >= 1.4.2
BuildRequires:  libxcrypt-devel
BuildRequires:  openldap-devel

# For doc generation; rapidsvn needs the "dot" tool from graphviz
BuildRequires:  docbook-style-xsl >= 1.58.1, doxygen, libxslt >= 1.0.27
BuildRequires:  graphviz

BuildRequires:  wxGTK-devel
BuildRequires:  desktop-file-utils

%description
RapidSVN is a GUI front-end for the Subversion revision control system. It
allows access to most of the features of Subversion through a user-friendly
interface.

%package -n svncpp
Summary:        C++ bindings for the Subversion client library
License:        LGPL-3.0-or-later
BuildRequires:  gcc-c++
BuildRequires:  subversion-devel
# for test framework
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

# The upstream Makefile is currently set up for OS/X and tries to use an old
# version of Python-native msgfmt.py, which doesn't work with Python3. Instead,
# we switch back to using the gettext version of 'msgfmt'
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

# Install desktop file and icon
%{__install} -D -m 644 librapidsvn/src/res/bitmaps/rapidsvn_128x128.png %{buildroot}%{_datadir}/pixmaps/rapidsvn.png
%{__install} -d -m 755 %{buildroot}%{_datadir}/applications/
desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications \
        rapidsvn.desktop

# Install manpage
%{__install} -D -m 644 doc/manpage/rapidsvn.1 %{buildroot}%{_mandir}/man1/rapidsvn.1

# Remove libtool stuff
rm -f %{buildroot}%{_libdir}/librapidsvn.{a,la}
rm -f %{buildroot}%{_libdir}/libsvncpp.{a,la}

# Can't see any meaningful use for this
rm -f %{buildroot}%{_libdir}/librapidsvn.so

%find_lang %{name}

%check
# Tests seem to be incomplete/not readily executable at present
#pushd libsvncpp/tests/
#sed -i s~/home/brent/dev/rapidsvn/~%{buildroot}~
#make
#./svncpptest | grep OK		
#if [ $? != 0 ]; then	
#    echo "svncpp tests failed"
#    exit 5
#fi

%ldconfig_scriptlets -n svncpp

%files -f %{name}.lang
%doc AUTHORS CHANGES FDL.txt GPL.txt LICENSE.txt README
%{_bindir}/rapidsvn
%{_libdir}/librapidsvn.so.*
%{_datadir}/applications/*rapidsvn.desktop
%{_datadir}/pixmaps/rapidsvn.png
%{_mandir}/man1/*

%files -n svncpp
%doc LGPL.txt
%{_libdir}/libsvncpp.so.4*

%files -n svncpp-devel
%doc doc/svncpp/html
%{_includedir}/svncpp/
%{_libdir}/libsvncpp.so

%changelog
%autochangelog
