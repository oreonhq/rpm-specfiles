%global source0_hash 68db0ca3cda2d46a663a92ec26e6eb5adc392ea5191bcda74268f0aefa78066b
Name:		libotf
Version:	0.9.16
Release:        8%{?dist}
Summary:        A Library for handling OpenType Font
License:	LGPL-2.1-or-later
URL:            http://www.nongnu.org/m17n/
Source0:        http://download.savannah.gnu.org/releases/m17n/%{name}-%{version}.tar.gz
Requires:	freetype
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  libXaw-devel
BuildRequires:  make
# /oreon:deps
%description 
The library "libotf" provides the following facilites.
Read Open Type Layout Tables from OTF file. Currently these tables are
supported; head, name, cmap, GDEF, GSUB, and GPOS.  Convert a Unicode
character sequence to a glyph code sequence by using the above tables.
The combination of libotf and the FreeType library (Ver.2) realizes
CTL (complex text layout) by OpenType fonts. This library is currently
used by the m17n library. It seems that the probject Free Type Layout
provides the similar (or better) facility as this library, but
currently they have not yet released their library. So, we have
developed this one.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}, pkgconfig
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%configure --disable-static
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
for file in $RPM_BUILD_ROOT%{_bindir}/*; do chrpath -d $file || true; done
(cd example && make clean && rm -rf .deps && rm Makefile)
rm $RPM_BUILD_ROOT%{_bindir}/libotf-config
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libotf-devel -f %{oreon_filedir}/libotf-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.16-8
- Prepare for Oreon 11 (RP1)
