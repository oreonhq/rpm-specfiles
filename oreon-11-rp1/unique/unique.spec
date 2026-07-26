%global source0_hash e5c8041cef8e33c55732f06a292381cb345db946cf792a4ae18aa5c66cdd4fbb

Name:           unique
Version:        1.1.6
Release:        37%{?dist}
Summary:        Single instance support for applications

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.gnome.org/~ebassi/source/
Source0:        http://download.gnome.org/sources/libunique/1.1/libunique-%{version}.tar.bz2

# Fix build -- upstream dead (replaced with GtkApplication)
Patch0:    fix-unused-but-set-variable.patch
Patch1:    fix-disable-deprecated.patch
Patch2:    libunique-1.1.6-format-security.patch

BuildRequires: make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dbus-glib-devel
BuildRequires:  gnome-doc-utils >= 0.3.2
BuildRequires:  libtool
BuildRequires:  glib2-devel >= 2.12.0
BuildRequires:  gtk2-devel >= 2.11.0
BuildRequires:  gtk-doc >= 1.11

%description
Unique is a library for writing single instance applications, that is
applications that are run once and every further call to the same binary
either exits immediately or sends a command to the running instance.

%package devel
Summary: Libraries and headers for Unique
Requires: %{name} = %{version}-%{release}
Requires: dbus-glib-devel
Requires: gtk2-devel

%description devel
Headers and libraries for Unique.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libunique-%{?version}
%patch -P0 -p1 -b .unused-but-set-variable
%patch -P1 -p1 -b .disable-deprecated
%patch -P2 -p1 -b .format-security
# fix compatibility with gtk-doc 1.26
gtkdocize
autoreconf -fiv

%build
%configure --enable-gtk-doc --disable-static --enable-introspection=no --enable-maintainer-flags=no
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -delete

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/lib*.so.*

%files devel
%doc %{_datadir}/gtk-doc
%{_includedir}/unique-1.0/
%{_libdir}/pkgconfig/*
%{_libdir}/lib*.so

%changelog
%autochangelog
