%global source0_hash bfc9603e2023ea071f2661ecc29e52c94b1beed6b69deae45b466df7f5b2ce55

Name:		gtk+extra
Version:	2.1.2
Release:	43%{?dist}
Summary:	A library of gtk+ widgets
Summary(fr):	Une bibliothèque de widgets gtk+

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
URL:		http://gtkextra.sourceforge.net/
Source:		http://downloads.sourceforge.net/gtkextra/gtk+extra-%{version}.tar.gz
Patch0:		%{name}-%{version}-gtk2.21.patch
Patch1:		%{name}-%{version}-make.patch
Patch2:		%{name}-%{version}-marshal.patch
Patch3:		%{name}-%{version}-gtkitementry.patch
Patch4:		%{name}-%{version}-gtkcharsel.patch
Patch5:		%{name}-%{version}-gtkcolorcombo.patch
Patch6:		%{name}-%{version}-format.patch
Patch7:		%{name}-%{version}-roundint.patch

BuildRequires:	gtk2-devel libtool gtk-doc
BuildRequires: make

%description
A library of dynamically linked gtk+ widgets including:
GtkSheet, GtkPlot, and GtkIconList

%description -l fr
Une bibliothèque de widgets gtk+ liés dynamiquement incluant :
GtkSheet, GtkPlot et GtkIconList

%package devel
Summary:	A library of gtk+ widgets
Summary(fr):	Une bibliothèque de widgets gtk+
Requires:	%{name} = %{version}-%{release}
Requires:	gtk2-devel

%description devel
The %{name}-devel package includes the static libraries, header files,
and documentation for compiling programs that use gtk+extra widgets.

%description -l fr devel
Le paquetage %{name}-devel contient les bibliothèques statiques, les fichiers
d'en-têtes et la documentation nécessaires à la compilation des programmes
qui utilisent les widgets gtk+extra.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%{__chmod} a-x ChangeLog
%{__sed} -i 's/\r//' docs/{gtk*.ChangeLog,HELP,README,TODO,VERSION}
%{__sed} -i 's/\r//' docs/reference/*.html
%{__sed} -i 's/\r//' docs/tutorial/{*.html,gtksheet/*.{c,html}}

%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p1
%patch -P3 -p0
%patch -P4 -p0
%patch -P5 -p0
%patch -P6 -p0
%patch -P7 -p0
libtoolize --force
aclocal
autoheader

autoreconf -i
automake 

%build
%configure
make  %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/libgtkextra*.so.*

%files devel
%doc docs/{gtk*.ChangeLog,COPYING,HELP,README,TODO,VERSION}
%doc docs/reference/ docs/tutorial/
%dir %{_datadir}/gtk-doc/html/gtkextra/
%{_datadir}/gtk-doc/html/gtkextra/*
%{_libdir}/*.a
%exclude %{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%changelog
%autochangelog
