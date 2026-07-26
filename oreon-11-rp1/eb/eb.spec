%global source0_hash abe710a77c6fc3588232977bb2f30a2e69ddfbe9fa8d0b05b0d67d95e36f4b5f

Name:           eb
Version:        4.4.3
Release:        30%{?dist}
Summary:        Library for accessing Japanese CD-ROM electronic books
Summary(ja):    CD-ROM 書籍にアクセスするためのライブラリ

License:        BSD-3-Clause
URL:            http://www.sra.co.jp/people/m-kasahr/eb/
Source0:        ftp://ftp.sra.co.jp/pub/misc/eb/%{name}-%{version}.tar.bz2
Patch1:         eb-aclocal-conf-libdir.patch
Patch2:         eb-gcc14.patch

BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  zlib-devel
%ifarch aarch64
BuildRequires:	autoconf
%endif

%description
EB Library is a C library for accessing CD-ROM books.
EB Library supports to access CD-ROM books of
EB, EBG, EBXA, EBXA-C, S-EBXA and EPWING formats.

%description -l ja
EB ライブラリは CD-ROM 書籍にアクセスするための C のライブラリです。
EB, EBG, EBXA, EBXA-C, S-EBXA および EPWING 形式の
CD-ROM 書籍に対応しています。

%package devel
Summary:        Development files for eb
Requires:       eb = %{version}
Requires:       zlib-devel

%description devel
This package contains development files needs to use eb in programs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1 -b .1-etc~
%patch -P2 -p1

%build
%ifarch aarch64
autoconf
%endif
CFLAGS="$CFLAGS -std=gnu17"
%configure --disable-static --sysconfdir=%{_libdir}
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install

rm $RPM_BUILD_ROOT%{_libdir}/libeb.la

rm -rf tmp
mkdir -p tmp
mv $RPM_BUILD_ROOT%{_datadir}/eb/doc tmp/html

%find_lang %{name}
%find_lang %{name}utils
cat %{name}utils.lang >> %{name}.lang

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/*
%{_libdir}/libeb.so.*
%{_datadir}/eb

%files devel
%doc tmp/html
%{_includedir}/eb
%{_libdir}/eb.conf
%{_libdir}/libeb.so
%{_datadir}/aclocal/*

%changelog
%autochangelog
