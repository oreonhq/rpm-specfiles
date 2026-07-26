%global source0_hash 8bc43c60f1716b13cf35fc899e2a36ea9c6cdc3478a8f051220eef0f53567efd

%global xfceversion 4.20

Name:           xfconf
Version:        4.20.0
Release:        %autorelease
Summary:        Hierarchical configuration system for Xfce

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://www.xfce.org/
#VCS git:git://git.xfce.org/xfce/xfconf
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  glib2-devel
BuildRequires:  pkgconfig(libxfce4util-1.0) >= %{xfceversion}
BuildRequires:  pkgconfig(dbus-1) >= 1.1.0
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.84
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection-devel
BuildRequires:  vala
BuildRequires:  systemd-rpm-macros

Requires:       dbus

Obsoletes:      libxfce4mcs < 4.4.3-3
Obsoletes:      xfconf-perl < 4.13.8

%description
Xfconf is a hierarchical (tree-like) configuration system where the
immediate child nodes of the root are called "channels".  All settings
beneath the channel nodes are called "properties."

%package        devel
Summary:        Development tools for xfconf
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Requires:       dbus-devel
Requires:       dbus-glib-devel
Requires:       glib2-devel
Obsoletes:      libxfce4mcs-devel < 4.4.3-3
Obsoletes:      xfce-mcs-manager-devel < 4.4.3-3

%description devel
This package includes the libraries and header files you will need
to compile applications for xfconf.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --disable-static --with-perl-options=INSTALLDIRS="vendor"
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
export LD_LIBRARY_PATH="`pwd`/xfconf/.libs"

%make_build

%install
%make_install

# fix permissions for installed libraries
chmod 755 %{buildroot}/%{_libdir}/*.so

# remove .packlist files. 
find %{buildroot} -type f -name .packlist -exec rm -f {} \;

# get rid of .la files
find %{buildroot} -type f -name *.la -exec rm -f {} \;

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%{_libdir}/lib*.so.*
%{_bindir}/xfconf-query
%{_libdir}/xfce4/xfconf/
%{_libdir}/girepository-1.0/Xfconf-0.typelib
%{_datadir}/vala/vapi/libxfconf-0.deps
%{_datadir}/vala/vapi/libxfconf-0.vapi
%{_datadir}/dbus-1/services/org.xfce.Xfconf.service
%{_datadir}/gir-1.0/Xfconf-0.gir
%{_datadir}/bash-completion/completions/xfconf-query
%{_userunitdir}/xfconfd.service

%files devel
%doc %{_datadir}/gtk-doc
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/xfce4/xfconf-0
%{_libdir}/gio/modules/libxfconfgsettingsbackend.so

%changelog
%autochangelog
