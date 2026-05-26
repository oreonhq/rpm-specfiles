%global tarball libXvMC
#global gitdate 20130524
%global gitversion e9415ddef

Summary: X.Org X11 libXvMC runtime library
Name: libXvMC
Version: 1.0.13
Release: 9%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
License: MIT
URL: http://www.x.org

%if 0%{?gitdate}
Source0:        https://xorg.freedesktop.org/archive/individual/lib/libXvMC-1.0.13.tar.xz
Source1:    make-git-snapshot.sh
Source2:    commitid
%else
Source0: https://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 0a9ebe6dea7888a747e5aca1b891d53cd7d3a5f141a9645f77d9b6a12cee657c
%global source0_file libXvMC-1.0.13.tar.xz
# oreon url source checksums end
%endif

Requires: libX11 >= 1.5.99.902

BuildRequires: make
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig(videoproto) pkgconfig(xv)
BuildRequires: libX11-devel >= 1.5.99.902

%description
X.Org X11 libXvMC runtime library

%package devel
Summary: X.Org X11 libXvMC development package
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXvMC development package

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libXvMC-1.0.13.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "0a9ebe6dea7888a747e5aca1b891d53cd7d3a5f141a9645f77d9b6a12cee657c" || { echo "oreon: Source0 SHA256 mismatch for libXvMC-1.0.13.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build
autoreconf -v --install --force
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# do this ourself in %%doc so we get %%version
rm $RPM_BUILD_ROOT%{_docdir}/*/*.txt

# Touch XvMCConfig for rpm to package the ghost file. (#192254)
{
    mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11
    touch $RPM_BUILD_ROOT%{_sysconfdir}/X11/XvMCConfig
}

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_post
%ldconfig_postun

%files
%doc COPYING README.md
%{_libdir}/libXvMC.so.1
%{_libdir}/libXvMC.so.1.0.0
%{_libdir}/libXvMCW.so.1
%{_libdir}/libXvMCW.so.1.0.0
%ghost %config(missingok,noreplace) %verify (not md5 size mtime) %{_sysconfdir}/X11/XvMCConfig

%files devel
%doc XvMC_API.txt
%{_includedir}/X11/extensions/XvMClib.h
%{_includedir}/X11/extensions/vldXvMC.h
%{_libdir}/libXvMC.so
%{_libdir}/libXvMCW.so
%{_libdir}/pkgconfig/xvmc.pc
%{_libdir}/pkgconfig/xvmc-wrapper.pc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.13-9
- Import
