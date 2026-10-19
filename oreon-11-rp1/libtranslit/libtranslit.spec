%global source0_hash 0f8bfa19aeb5436fe175badaf58501017c1cd4b8c43fe66b8efbceb452f045de
Name:		libtranslit
Version:	0.0.3
Release:        1%{?dist}
Summary:        ASCII to Unicode transliteration library with multiple backends
License:	GPL-3.0-or-later
URL:		http://github.com/ueno/libtranslit
Source0:        http://du-a.org/files/libtranslit/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  pkgconfig(icu-io)
BuildRequires:  pkgconfig(m17n-shell)
BuildRequires:  vala
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libtranslit-devel -f %{oreon_filedir}/libtranslit-devel.list
%files -n libtranslit-m17n -f %{oreon_filedir}/libtranslit-m17n.list
%files -n libtranslit-icu -f %{oreon_filedir}/libtranslit-icu.list

%changelog

%autochangelog
