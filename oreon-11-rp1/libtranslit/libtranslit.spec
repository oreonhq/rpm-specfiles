%global source0_hash 0f8bfa19aeb5436fe175badaf58501017c1cd4b8c43fe66b8efbceb452f045de

Name:		libtranslit
Version:	0.0.3
Release:	51%{?dist}
Summary:	ASCII to Unicode transliteration library with multiple backends

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		http://github.com/ueno/libtranslit
Source0:	http://du-a.org/files/libtranslit/%{name}-%{version}.tar.gz

BuildRequires:	gobject-introspection-devel
BuildRequires:	intltool
BuildRequires:	vala

%description
ASCII to Unicode transliteration library with multiple backends.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	m17n
Summary:	Transliteration module using m17n-lib for %{name}
BuildRequires:	pkgconfig(m17n-shell)
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	m17n
The %{name}-m17n package contains a transliteration module using
m17n-lib for %{name}.

%package	icu
Summary:	Transliteration module using m17n-lib for %{name}
BuildRequires:	pkgconfig(icu-io)
BuildRequires: make
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	icu
The %{name}-icu package contains a transliteration module using
ICU for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f '{}' ';'

%ldconfig_scriptlets

%files
%{_libdir}/*.so.*
%dir %{_libdir}/libtranslit
%dir %{_libdir}/libtranslit/modules
%{_libdir}/girepository-1.0/*.typelib

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*.vapi
%{_datadir}/vala/vapi/*.deps

%files m17n
%{_libdir}/libtranslit/modules/*m17n.so*

%files icu
%{_libdir}/libtranslit/modules/*icu.so*

%changelog
%autochangelog
