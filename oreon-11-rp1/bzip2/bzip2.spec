%global source2_hash c667e2db9a3cd17bde492584263cb7c30d8050538678ece3078ae58230e6e5e1
%global source0_hash ab5a03176ee106d3f0fa90e381da478ddae405918153cca248e682cd0c4a2269
%global source3_key_fpr EC3CFE88F6CA0788774F5C1D1AA44BE649DE760A
%global library_version 1.0.8
Summary:        File compression utility
Name: bzip2
Version: 1.0.8
Release:        23%{?dist}
License: BSD-4-Clause
URL: https://sourceware.org/bzip2
Source0:        https://sourceware.org/pub/bzip2/%{name}-%{version}.tar.gz
Source1:        bzip2.pc
Source2:        https://sourceware.org/pub/bzip2/%{name}-%{version}.tar.gz.sig
Source3:        gpgkey-5C1D1AA44BE649DE760A.gpg
Patch0:        bzip2-saneso.patch
Patch1:        bzip2-cflags.patch
Patch2:        bzip2-ldflags.patch
Patch3:        man_gzipdiff.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
# /oreon:deps
%description
Bzip2 is a freely available, patent-free, high quality data compressor.
Bzip2 compresses files to within 10 to 15 percent of the capabilities
of the best techniques available.  However, bzip2 has the added benefit
of being approximately two times faster at compression and six times
faster at decompression than those techniques.  Bzip2 is not the
fastest compression utility, but it does strike a balance between speed
and compression capability.

Install bzip2 if you need a compression utility.

%package devel
Summary: Libraries and header files for apps which will use bzip2
Requires: bzip2-libs%{?_isa} = %{version}-%{release}
%description devel
Header files and a library of bzip2 functions, for developing apps
which will use the library.

%package libs
Summary: Libraries for applications using bzip2
%description libs
Libraries for applications using the bzip2 compression format.

%package static
Summary: Libraries for applications using bzip2
%description static
Static libraries for applications using the bzip2 compression format.

%prep

test -z "%{source3_key_fpr}" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" 2>/dev/null | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source3_key_fpr}" || { echo "oreon: Source3 key fingerprint mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE3}' --signature='%{SOURCE2}' --data='%{SOURCE0}'
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p2

cp -a %{SOURCE1} .
sed -i "s|^libdir=|libdir=%{_libdir}|" bzip2.pc

%build

%make_build -f Makefile-libbz2_so CC="%{__cc}" AR="%{__ar}" RANLIB="ranlib" \
    CFLAGS="$RPM_OPT_FLAGS -D_FILE_OFFSET_BITS=64 -fpic -fPIC" \
    LDFLAGS="%{__global_ldflags}" \
    all
rm -f *.o
%make_build CC="%{__cc}" AR="%{__ar}" RANLIB="ranlib" \
    CFLAGS="$RPM_OPT_FLAGS -D_FILE_OFFSET_BITS=64" \
    LDFLAGS="%{__global_ldflags}" \
    all
%install
chmod 644 bzlib.h
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/pkgconfig,%{_includedir}}
cp -p bzlib.h $RPM_BUILD_ROOT%{_includedir}
install -m 755 libbz2.so.%{library_version} $RPM_BUILD_ROOT%{_libdir}
install -m 644 libbz2.a $RPM_BUILD_ROOT%{_libdir}
install -m 644 bzip2.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/bzip2.pc
install -m 755 bzip2-shared  $RPM_BUILD_ROOT%{_bindir}/bzip2
install -m 755 bzip2recover bzgrep bzdiff bzmore  $RPM_BUILD_ROOT%{_bindir}/
cp -p bzip2.1 bzdiff.1 bzgrep.1 bzmore.1  $RPM_BUILD_ROOT%{_mandir}/man1/
ln -s bzip2 $RPM_BUILD_ROOT%{_bindir}/bunzip2
ln -s bzip2 $RPM_BUILD_ROOT%{_bindir}/bzcat
ln -s bzdiff $RPM_BUILD_ROOT%{_bindir}/bzcmp
ln -s bzmore $RPM_BUILD_ROOT%{_bindir}/bzless
ln -s bzgrep $RPM_BUILD_ROOT%{_bindir}/bzegrep
ln -s bzgrep $RPM_BUILD_ROOT%{_bindir}/bzfgrep
ln -s libbz2.so.%{library_version} $RPM_BUILD_ROOT%{_libdir}/libbz2.so.1
ln -s libbz2.so.1 $RPM_BUILD_ROOT%{_libdir}/libbz2.so
ln -s bzip2.1 $RPM_BUILD_ROOT%{_mandir}/man1/bzip2recover.1
ln -s bzip2.1 $RPM_BUILD_ROOT%{_mandir}/man1/bunzip2.1
ln -s bzip2.1 $RPM_BUILD_ROOT%{_mandir}/man1/bzcat.1
ln -s bzdiff.1 $RPM_BUILD_ROOT%{_mandir}/man1/bzcmp.1
ln -s bzmore.1 $RPM_BUILD_ROOT%{_mandir}/man1/bzless.1
ln -s bzgrep.1 $RPM_BUILD_ROOT%{_mandir}/man1/bzegrep.1
ln -s bzgrep.1 $RPM_BUILD_ROOT%{_mandir}/man1/bzfgrep.1
%ldconfig_scriptlets libs
%oreon_autofiles bzip2-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles bzip2-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bzip2-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n bzip2-devel -f %{oreon_filedir}/bzip2-devel.list
%files -n bzip2-libs -f %{oreon_filedir}/bzip2-libs.list
%files -n bzip2-static -f %{oreon_filedir}/bzip2-static.list

%changelog

* Fri Apr 3 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.8-23
- Escape macros in commented legacy Source0 line (rpmlint)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.8-23
- Prepare for Oreon 11 (RP1)
