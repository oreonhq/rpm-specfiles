%global source0_hash a8f02ce073e2b920cca8ac45d418e7cb64438ad0814780c5912c6d63f8a4e038
Name:           unique3
Version:        3.0.2
Release:        34%{?dist}
Summary:        Single instance support for applications
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.gnome.org/~ebassi/source/
Source0:        http://download.gnome.org/sources/libunique/3.0/libunique-%{version}.tar.xz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  glib2-devel
BuildRequires:  gnome-doc-utils
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n unique3-docs -f %{oreon_filedir}/unique3-docs.list
%files -n unique3-devel -f %{oreon_filedir}/unique3-devel.list

%changelog

%autochangelog
