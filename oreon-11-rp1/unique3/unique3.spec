%global source0_hash a8f02ce073e2b920cca8ac45d418e7cb64438ad0814780c5912c6d63f8a4e038

Name:           unique3
Version:        3.0.2
Release:        34%{?dist}
Summary:        Single instance support for applications

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.gnome.org/~ebassi/source/
Source0:        http://download.gnome.org/sources/libunique/3.0/libunique-%{version}.tar.xz

BuildRequires: make
BuildRequires:  gnome-doc-utils >= 0.3.2
BuildRequires:  libtool
BuildRequires:  glib2-devel >= 2.25.0
BuildRequires:  gtk3-devel >= 2.99.3
BuildRequires:  gtk-doc >= 1.11

BuildRequires: automake autoconf libtool

%description
Unique is a library for writing single instance applications, that is
applications that are run once and every further call to the same binary
either exits immediately or sends a command to the running instance.

This version of unique works with GTK+ 3.

%package docs
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description docs
API docs for %{name}.

%package devel
Summary: Libraries and headers for unique3
Requires: %{name} = %{version}-%{release}
Requires: glib2-devel
Requires: gtk3-devel

%description devel
Headers and libraries for unique3.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libunique-%{?version}
# fix compatibility with gtk-doc 1.26
gtkdocize
autoreconf -i -f -v

%build
%configure --enable-gtk-doc --disable-static --enable-introspection=no
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/unique-3.0/
%{_libdir}/pkgconfig/*
%{_libdir}/lib*.so

%files docs
%doc %{_datadir}/gtk-doc

%changelog
%autochangelog
