%global source0_hash 7149686a71ca42a1390869b6074815106b061aaeaaa8f2ef8c12c191d9a79f6a

Name:           gmime
Version:        2.6.23
Release:        26%{?dist}
Summary:        Library for creating and parsing MIME messages

# Files in examples/, src/ and tests/ are GPLv2+
# Automatically converted from old format: LGPLv2+ and GPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later
URL:            http://spruce.sourceforge.net/gmime/
Source0:        http://download.gnome.org/sources/gmime/2.6/gmime-%{version}.tar.xz

BuildRequires:  glib2-devel >= 2.18.0
BuildRequires:  gobject-introspection-devel
BuildRequires:  gpgme-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  vala-devel
BuildRequires:  vala
BuildRequires:  zlib-devel >= 1.2.1.1
BuildRequires:  gettext-devel, gtk-doc
BuildRequires:  automake autoconf

Patch1: gmime-2.5.8-gpg-error.patch
Patch2: gmime-2.6.23-build-avoid-useless-configure-time-checks.patch
Patch3: gmime-2.6.23-check-ac_cv_sys_file_offset_bits-against-empty.string.patch
Patch4: gmime-2.6.23-tune-up-fix-for-autoconf-2-72.patch

# mono available only on selected architectures
%ifarch  %mono_arches
%define buildmono 1
%else
%define buildmono 0
%endif

%if 0%{?rhel} >= 6
%define buildmono 0
%endif

%if 0%buildmono
BuildRequires:  mono-devel gtk-sharp2-gapi
BuildRequires:  gtk-sharp2-devel >= 2.4.0
%endif
BuildRequires: make

%description
The GMime suite provides a core library and set of utilities which may be
used for the creation and parsing of messages using the Multipurpose
Internet Mail Extension (MIME).

%package        devel
Summary:        Header files to develop libgmime applications
Requires:       %{name}%{_isa} = %{version}-%{release}
Requires:       glib2-devel

%description    devel
The GMime suite provides a core library and set of utilities which may be
used for the creation and parsing of messages using the Multipurpose
Internet Mail Extension (MIME). The devel-package contains header files
to develop applications that use libgmime.

%if 0%buildmono
%package        sharp
Summary:        Mono bindings for gmime
Requires:       %{name}%{_isa} = %{version}-%{release}
Requires:       gtk-sharp2

%description    sharp
The GMime suite provides a core library and set of utilities which may be
used for the creation and parsing of messages using the Multipurpose
Internet Mail Extension (MIME). The devel-package contains support 
for developing mono applications that use libgmime.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1 -b .gpg-error
%patch -P2 -p1 -b .build-avoid-useless-configure-time-checks
%patch -P3 -p1 -b .check-ac_cv_sys_file_offset_bits-against-empty.string.patch
%patch -P4 -p1 -b .tune-up-fix-for-autoconf-2-72.patch

%build
autoreconf -vif
MONO_ARGS="--enable-mono=no"
%if 0%buildmono
export MONO_SHARED_DIR=%{_builddir}/%{?buildsubdir}
MONO_ARGS="--enable-mono"
%endif
# Don't conflict with sharutils.
%configure $MONO_ARGS --program-prefix=%{name} --disable-static

# Omit unused direct shared library dependencies.
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags} V=1

%install
export MONO_SHARED_DIR=%{_builddir}/%{?buildsubdir}
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS README TODO
%{_libdir}/lib*.so.*
%{_libdir}/girepository-1.0/GMime-2.6.typelib

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/gmime-2.6.pc
%{_includedir}/gmime-2.6
%{_datadir}/gir-1.0/GMime-2.6.gir
%{_datadir}/gtk-doc/html/gmime-2.6
%{_datadir}/vala/

%if 0%buildmono
%files sharp
%{_libdir}/pkgconfig/gmime-sharp-2.6.pc
%{_monogacdir}/gmime-sharp
%{_monodir}/gmime-sharp-2.6
%{_datadir}/gapi-2.0/gmime-api.xml
%endif

%changelog
%autochangelog
