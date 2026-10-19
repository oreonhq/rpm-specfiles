%global source0_hash 7129fe3b7ad500f88b8af8605ef07b96c87a75ec986a695fffc0a409f44a7c86
%if 0%{?fedora} || (0%{?oreon} >= 11)
%bcond_without anthy
%else
%bcond_with anthy
%endif
Name:           m17n-lib
Version:        1.8.6
Release:        1%{?dist}
Summary:        Multilingual text library
License:        LGPL-2.1-or-later
URL:            http://www.nongnu.org/m17n/
Source0:        https://download.savannah.gnu.org/releases/m17n/%{name}-%{version}.tar.gz
Patch0:         %{name}-1.8.0-multilib.patch
Provides: bundled(gnulib)
%if %{with anthy}
%endif
Requires:       m17n-db
# oreon:deps
BuildRequires:  anthy-unicode-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  fribidi-devel
BuildRequires:  gd-devel
BuildRequires:  gettext-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXft-devel
BuildRequires:  libotf-devel
BuildRequires:  libthai-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  m17n-db-devel
BuildRequires:  make
# /oreon:deps
%description
m17n-lib is a multilingual text library used primarily to allow
the input of many languages with the input table maps from m17n-db.

The package provides the core and input method backend libraries.

%if %{with anthy}
%package  anthy
Summary:  Anthy module for m17n
Requires: %{name}%{?_isa} = %{version}-%{release}
%description anthy
Anthy module for %{name} allows ja-anthy.mim to support input conversion.
%endif

%package  devel
Summary:  Development files for %{name}
Requires: %{name}-tools = %{version}-%{release}
%description devel
Development files for %{name}.

%package  tools
Summary:  The m17n GUI Library tools
Requires: m17n-db-extras
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tools
Tools to test M17n GUI widget library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir m17n-lib-1.8.6
%oreon_prep
%build

%configure --disable-rpath --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%{make_build}
%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm %{buildroot}%{_libdir}/m17n/1.0/libmimx-ispell.so
%if %{without anthy}
rm %{buildroot}%{_libdir}/m17n/1.0/libmimx-anthy.so
%endif
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%ldconfig_scriptlets tools
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n m17n-lib-anthy -f %{oreon_filedir}/m17n-lib-anthy.list
%files -n m17n-lib-devel -f %{oreon_filedir}/m17n-lib-devel.list
%files -n m17n-lib-tools -f %{oreon_filedir}/m17n-lib-tools.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.6-1
- Import
