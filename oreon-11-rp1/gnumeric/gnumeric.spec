%global source0_hash 89331121321b9bad72d37af5a6d13a0a636f0fbb0880f0ea1f2cf8b7ab9ae631
Name:             gnumeric
Epoch:            1
Version:          1.12.62
Release:        1%{?dist}
Summary:        Spreadsheet program for GNOME
License:          GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-or-later
URL:              http://www.gnumeric.org
Source0:        https://download.gnome.org/sources/%{name}/1.12/%{name}-%{version}.tar.xz
ExcludeArch:    %{ix86}
Requires:         hicolor-icon-theme
# oreon:deps
BuildRequires:  bison
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-dtds
BuildRequires:  gcc
BuildRequires:  goffice-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  libgda-ui-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  psiconv-devel
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%py_byte_compile %{__python3} $RPM_BUILD_ROOT%{_libdir}/%{name}/%{version}/plugins
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet \
        %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate \
        %{buildroot}/%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list
%files -n gnumeric-devel -f %{oreon_filedir}/gnumeric-devel.list
%files -n gnumeric-plugins-extras -f %{oreon_filedir}/gnumeric-plugins-extras.list

%changelog

%autochangelog
