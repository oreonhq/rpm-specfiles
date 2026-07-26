%global source0_hash e9adde0a99ba787dfcb310b61f3acd37c5ba1a4c1cf36b376b60537ef64d1aa5

%global debug_package %{nil}
Name:		poppler-sharp
Version:	0.0.3
Release:	39%{?dist}
Summary:	C sharp Bindings for Poppler
Summary(es):	Enlaces C# para Poppler
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.github.com/jacintos/poppler-sharp
Source0:	http://github.com/downloads/jacintos/%{name}/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:	mono-devel
BuildRequires:	gtk-sharp2-gapi
BuildRequires:	gtk-sharp2-devel
BuildRequires:	poppler-glib-devel

Requires:	poppler
Requires:	poppler-glib

# Mono only available on these:
ExclusiveArch: %mono_arches

%description
Generates managed bindings for Poppler using the GAPI tools

%description -l es
Genera los vínculos administrados usando las herramientas GAPI

%package devel
Summary:	Development files for %{name}
Summary(es):	Archivos de desarrollo para %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
Development package for %{name}

%description devel -l es
Paquete de desarrollo para %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -i "s#gmcs#mcs#g" configure
sed -i "s#gmcs#mcs#g" configure.ac
sed -i "s#gmcs#mcs#g" Makefile.am
sed -i "s#gmcs#mcs#g" Makefile.in
sed -i "s#mono/2.0#mono/4.5#g" configure
sed -i "s#mono/2.0#mono/4.5#g" configure.ac

%build
%configure
sed -i "s#gmcs#mcs#g" configure
sed -i "s#gmcs#mcs#g" configure.ac
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%license COPYING
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/%{name}.dll*

%files devel
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
