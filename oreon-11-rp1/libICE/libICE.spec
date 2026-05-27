%global source0_hash 974e4ed414225eb3c716985df9709f4da8d22a67a2890066bc6dfc89ad298625

Summary: X.Org X11 ICE runtime library
Name: libICE
Version: 1.1.2
Release: 4%{?dist}
License: MIT-open-group
URL: http://www.x.org

Source0: https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz

# Needed for pre-glibc-2.25, which at this point would mean RHEL7 but not 8
# Patch1: 0002-Add-getentropy-emulation-through-syscall.patch

BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool make
BuildRequires: pkgconfig
BuildRequires: xorg-x11-proto-devel
BuildRequires: xorg-x11-xtrans-devel >= 1.0.3-5

%description
The X.Org X11 ICE (Inter-Client Exchange) runtime library.

%package devel
Summary: X.Org X11 ICE development package
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The X.Org X11 ICE (Inter-Client Exchange) development package.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
#patch1 -p1 -b .cve-2017-2626

%build
autoreconf -v --install --force
%configure --disable-static \
	   --without-fop --without-xmlto
V=1 make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# adding to installed docs in order to avoid using %%doc magic
for f in AUTHORS ChangeLog COPYING ; do
    cp -p $f ${RPM_BUILD_ROOT}%{_docdir}/%{name}/${f}
done

%ldconfig_post
%ldconfig_postun

%files
%{_libdir}/libICE.so.6
%{_libdir}/libICE.so.6.3.0
# not using %%doc because of side-effect (#1001256)
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/ChangeLog
%{_docdir}/%{name}/COPYING

%files devel
%{_docdir}/%{name}/*.xml
%{_includedir}/X11/ICE
%{_libdir}/libICE.so
%{_libdir}/pkgconfig/ice.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.2-4
- Prepare for Oreon 11 (RP1)
