%global source0_hash 821328b5054f7890a0d0cd2f52825270705df3641dbd476d58d17e56ed957b59

%define _lto_cflags %{nil}

Summary:        PostScript Type 1 font rasterizer
Name:           t1lib
Version:        5.1.2
Release:        43%{?dist}
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://sources.voidlinux.org/t1lib-5.1.2/
Source0:        https://sources.voidlinux.org/t1lib-%{version}/t1lib-%{version}.tar.gz
Patch0:         t1lib_5.1.2-3.diff.gz
Patch1:         t1lib-5.1.2-segf.patch
Patch2:         t1lib-5.1.2-afm-fix.patch
Patch3:         t1lib-5.1.2-type1-inv-rw-fix.patch
Patch4:         t1lib-5.1.2-aarch64.patch
Patch5:         t1lib-5.1.2-format-security.patch
Patch6:         t1lib-5.1.2-t1.patch
Patch7:         t1lib-configure-c99.patch
Patch8:         t1lib-c99.patch
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libXaw-devel
Requires(post): coreutils, findutils

%description
T1lib is a rasterizer library for Adobe Type 1 Fonts. It supports
rotation and transformation, kerning underlining and antialiasing. It
does not depend on X11, but does provides some special functions for
X11.

AFM-files can be generated from Type 1 font files and font subsetting
is possible.

%package        apps
Summary:        t1lib demo applications
Requires:       %{name} = %{version}-%{release}

%description    apps
Sample applications using t1lib

%package        devel
Summary:        Header files and development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains header files and development files for %{name}.

%package        static
Summary:        Static libraries for %{name}
Requires:       %{name}-devel = %{version}-%{release}

%description    static
This package contains static libraries for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
patch -p1 < debian/patches/no-config.diff
patch -p1 < debian/patches/no-docs.diff
patch -p1 < debian/patches/lib-cleanup.diff

iconv -f latin1 -t utf8 < Changes > Changes.utf8
touch -r Changes Changes.utf8
mv Changes.utf8 Changes

%build
%if 0%{?fedora} > 41 || 0%{?rhel} > 10 || 0%{?oreon} >= 11
export CFLAGS="%{optflags} -std=gnu17"
%endif
%configure
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make without_doc
touch -r lib/t1lib/t1lib.h.in lib/t1lib.h
touch -r lib/t1lib/t1libx.h lib/t1libx.h
ln README.t1lib-%{version} README
sed -e 's;/usr/share/X11/fonts;%{_datadir}/X11/fonts;' \
  -e 's;/usr/share/fonts/type1;%{_datadir}/fonts %{_datadir}/texmf/fonts;' \
  -e 's;/etc/t1lib/;%{_datadir}/t1lib/;' \
  debian/t1libconfig > t1libconfig
touch -r README.t1lib-%{version} t1libconfig

%install
%make_install
find %{buildroot}%{_libdir}/ -name \*.la -delete
chmod a+x %{buildroot}%{_libdir}/libt1*.so.*

mkdir -p %{buildroot}%{_mandir}/man{1,5,8}
install -p -m 644 debian/man/FontDatabase.5 %{buildroot}%{_mandir}/man5/
install -p -m 644 debian/man/t1libconfig.8 %{buildroot}%{_mandir}/man8/
install -p -m 644 debian/man/type1afm.1 %{buildroot}%{_mandir}/man1/
install -p -m 644 debian/man/xglyph.1 %{buildroot}%{_mandir}/man1/
touch -r README.t1lib-%{version} %{buildroot}%{_mandir}/man?/*.*

install -p -m 755 -D t1libconfig %{buildroot}%{_sbindir}/t1libconfig

mkdir -p %{buildroot}%{_datadir}/t1lib/
touch %{buildroot}%{_datadir}/t1lib/{FontDatabase,t1lib.config}

%post
%{?ldconfig}
%{_sbindir}/t1libconfig --force > /dev/null

%ldconfig_postun

%files
%doc Changes LGPL LICENSE README
%dir %{_datadir}/t1lib
%ghost %verify(not size mtime md5) %{_datadir}/t1lib/t1lib.config
%ghost %verify(not size mtime md5) %{_datadir}/t1lib/FontDatabase
%{_libdir}/libt1.so.*
%{_libdir}/libt1x.so.*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_sbindir}/t1libconfig

%files apps
%{_bindir}/type1afm
%{_bindir}/xglyph
%{_mandir}/man1/*

%files devel
%doc doc/t1lib_doc.pdf
%{_includedir}/t1lib*.h
%{_libdir}/libt1.so
%{_libdir}/libt1x.so

%files static
%{_libdir}/libt1.a
%{_libdir}/libt1x.a

%changelog
%autochangelog
