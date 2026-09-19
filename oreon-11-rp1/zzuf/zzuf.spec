%global source0_hash a34f624503e09acd269c70d826aac2a35c03e84dc351873f140f0ba6a792ffd6

Name:           zzuf
Version:        0.15
Release:        26%{?dist}
Summary:        Transparent application input fuzzer

License:        WTFPL
URL:            http://sam.zoy.org/zzuf/
Source0:        http://github.com/zzuf/%{name}/archive/zzuf-%{version}.tar.gz
#Source0:	http://ftp.debian.org/debian/pool/main/z/zzuf/zzuf_0.13.svn20100215.orig.tar.gz
Patch0:         %{name}-0.13-optflags.patch
# AC_TRY_CFLAGS doesn't honor CFLAGS
# Causes package to produce broken configure results
Patch1:         %{name}-0.13-Remove-AC_TRY_CFLAGS.patch
Patch2:		zzuf-0.15-glibc.patch
Patch3: zzuf-zzat-c99.patch

BuildRequires: make
BuildRequires:  gcc autoconf automake libtool
%description
zzuf is a transparent application input fuzzer.  It works by
intercepting file operations and changing random bits in the program's
input.  zzuf's behaviour is deterministic, making it easy to reproduce
bugs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0
%patch -P1 -p1
%patch -P2 -p0
%patch -P3 -p1
touch -r aclocal.m4 configure.*

%build
autoreconf -if
%configure --disable-dependency-tracking --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/zzuf/libzzuf.la

%files
%doc AUTHORS TODO doc/
%license COPYING
%{_bindir}/zzuf
%{_bindir}/zzat
%dir %{_libdir}/zzuf/
%{_libdir}/zzuf/libzzuf.so
%{_mandir}/man1/zzuf.1*
%{_mandir}/man1/zzat.1*
%{_mandir}/man3/libzzuf.3*

%changelog
%autochangelog
