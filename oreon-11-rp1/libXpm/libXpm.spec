%global source0_hash 64b31f81019e7d388c822b0b28af8d51c4622b83f1f0cb6fa3fc95e271226e43

Summary: X.Org X11 libXpm runtime library
Name: libXpm
Version: 3.5.17
Release: 7%{?dist}
License: MIT AND X11-distribute-modifications-variant
URL: http://www.x.org

Source0:        https://www.x.org/pub/individual/lib/libXpm-3.5.17.tar.xz

BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool make
BuildRequires: gettext
BuildRequires: pkgconfig(xext) pkgconfig(xt) pkgconfig(xau)
BuildRequires: ncompress gzip

%description
X.Org X11 libXpm runtime library

%package devel
Summary: X.Org X11 libXpm development package
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXpm development package

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q

%build
autoreconf -v --install --force
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_post
%ldconfig_postun

%files
%doc AUTHORS COPYING ChangeLog
%{_libdir}/libXpm.so.4
%{_libdir}/libXpm.so.4.11.0

%files devel
%{_bindir}/cxpm
%{_bindir}/sxpm
%{_includedir}/X11/xpm.h
%{_libdir}/libXpm.so
%{_libdir}/pkgconfig/xpm.pc
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.5.17-7
- Prepare for Oreon 11 (RP1)
