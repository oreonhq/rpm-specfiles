%global source0_hash none

Name:             gnumeric
Epoch:            1
Version:          1.12.59
Release:          2%{?dist}
Summary:          Spreadsheet program for GNOME
License:          GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-or-later
URL:              http://www.gnumeric.org
Source:           https://download.gnome.org/sources/%{name}/1.12/%{name}-%{version}.tar.xz
BuildRequires:    bison
BuildRequires:    desktop-file-utils
BuildRequires:    docbook-dtds
BuildRequires:    gcc
BuildRequires:    goffice-devel >= 0.10.46
BuildRequires:    intltool
BuildRequires:    itstool
BuildRequires:    libappstream-glib
BuildRequires:    libgda-ui-devel
BuildRequires:    libxcrypt-devel
BuildRequires:    make
BuildRequires:    perl-devel
BuildRequires:    perl-generators
BuildRequires:    perl(ExtUtils::Embed)
BuildRequires:    perl(Getopt::Long)
BuildRequires:    perl(IO::Compress::Gzip)
BuildRequires:    psiconv-devel
BuildRequires:    python3-gobject-devel
BuildRequires:    python3-devel
BuildRequires:    zlib-devel

# https://gitlab.gnome.org/GNOME/goffice/-/issues/70
ExcludeArch:    %{ix86}

Requires:         hicolor-icon-theme

%description
Gnumeric is a spreadsheet program for the GNOME GUI desktop
environment.

%package devel
Summary:          Files necessary to develop gnumeric-based applications
Requires:         %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
Gnumeric is a spreadsheet program for the GNOME GUI desktop
environment. The gnumeric-devel package includes files necessary to
develop gnumeric-based applications.

%package plugins-extras
Summary:          Additional plugins for Gnumeric incl. Perl and Python support
Requires:         %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:         python(abi) = %{python3_version}

%description plugins-extras
This package contains the following additional plugins for gnumeric:
* gda and gnomedb plugins:
  Database functions for retrieval of data from a database.
* perl plugin:
  This plugin allows writing of plugins in Perl.
* python-loader plugin:
  This plugin allows writing of plugins in Python.
* py-func plugin:
  Sample Python plugin providing some (useless) functions.
* gnome-glossary:
  Support for saving GNOME Glossary in .po files. 

%prep
%autosetup -p1
chmod -x plugins/excel/rc4.?

%build
%configure --disable-silent-rules --disable-maintainer-mode
# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install

%find_lang %{name} --all-name --with-gnome

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --delete-original                                  \
  --remove-category Science                                             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications                         \
  $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/org.%{name}.%{name}.appdata.xml

#remove .la files
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Bytecompile Python plugins
%py_byte_compile %{__python3} $RPM_BUILD_ROOT%{_libdir}/%{name}/%{version}/plugins

%ldconfig_scriptlets

%check
appstream-util validate-relax --nonet \
        %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate \
        %{buildroot}/%{_datadir}/applications/*.desktop
        

%files -f %{name}.lang
%doc HACKING AUTHORS ChangeLog NEWS BUGS README
%license COPYING
%{_bindir}/*
%{_libdir}/libspreadsheet-%{version}.so
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/%{version}
%exclude %{_libdir}/%{name}/%{version}/plugins/perl-*
%if 0%{?fedora} >= 37
%exclude %{_libdir}/%{name}/%{version}/plugins/gdaif
%endif
%exclude %{_libdir}/%{name}/%{version}/plugins/psiconv
%exclude %{_libdir}/%{name}/%{version}/plugins/gnome-glossary
%exclude %{_libdir}/%{name}/%{version}/plugins/py-*
%exclude %{_libdir}/%{name}/%{version}/plugins/python-*
%{_datadir}/glib-2.0/schemas/org.gnome.gnumeric.*
%{_datadir}/icons/hicolor/*/apps/org.%{name}.%{name}.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{version}
%{_datadir}/applications/org.%{name}.%{name}.desktop
%{_metainfodir}/org.%{name}.%{name}.appdata.xml
%{_mandir}/man1/*

%files devel
%{_libdir}/libspreadsheet.so
%{_libdir}/pkgconfig/libspreadsheet-1.12.pc
%{_includedir}/libspreadsheet-1.12

%files plugins-extras
%{_libdir}/%{name}/%{version}/plugins/perl-*
%if 0%{?fedora} >= 37
%{_libdir}/%{name}/%{version}/plugins/gdaif
%endif
%{_libdir}/%{name}/%{version}/plugins/psiconv
%{_libdir}/%{name}/%{version}/plugins/gnome-glossary
%{_libdir}/%{name}/%{version}/plugins/py-*
%{_libdir}/%{name}/%{version}/plugins/python-* 
%{_libdir}/goffice/*/plugins/gnumeric/gnumeric.so
%{_libdir}/goffice/*/plugins/gnumeric/plugin.xml

%changelog
%autochangelog
