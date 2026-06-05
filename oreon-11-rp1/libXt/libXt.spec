%global source0_hash e0a774b33324f4d4c05b199ea45050f87206586d81655f8bef4dba434d931288

%global tarball libXt
#global gitdate 20190424
#global gitversion ba4ec9376

Summary: X.Org X11 libXt runtime library
Name: libXt
Version: 1.3.1
Release: 4%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
License: MIT AND HPND-sell-variant AND SMLNJ AND MIT-open-group AND X11
URL: https://www.x.org

%if 0%{?gitdate}
Source0:        libXt-1.3.1.tar.xz
Source1:        make-git-snapshot.sh
Source2:        commitid
%else
Source0:        libXt-1.3.1.tar.xz
%endif

Requires: libX11%{?_isa} >= 1.6

BuildRequires: make
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig(xproto) pkgconfig(x11) pkgconfig(sm)
BUildRequires: libX11-devel >= 1.6

%description
X.Org X11 libXt runtime library

%package devel
Summary: X.Org X11 libXt development package
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
X.Org X11 libXt development package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build
autoreconf -v --install --force
# FIXME: Work around pointer aliasing warnings from compiler for now
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure --disable-static \
  --with-xfile-search-path="%{_sysconfdir}/X11/%%L/%%T/%%N%%C%%S:%{_sysconfdir}/X11/%%l/%%T/\%%N%%C%%S:%{_sysconfdir}/X11/%%T/%%N%%C%%S:%{_sysconfdir}/X11/%%L/%%T/%%N%%S:%{_sysconfdir}/X\11/%%l/%%T/%%N%%S:%{_sysconfdir}/X11/%%T/%%N%%S:%{_datadir}/X11/%%L/%%T/%%N%%C%%S:%{_datadir}/X1\1/%%l/%%T/%%N%%C%%S:%{_datadir}/X11/%%T/%%N%%C%%S:%{_datadir}/X11/%%L/%%T/%%N%%S:%{_datadir}/X11/%%\l/%%T/%%N%%S:%{_datadir}/X11/%%T/%%N%%S"

V=1 make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p -m 0755 $RPM_BUILD_ROOT%{_datadir}/X11/app-defaults
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# adding to installed docs in order to avoid using %%doc magic
cp -p COPYING ${RPM_BUILD_ROOT}%{_datadir}/doc/%{name}/COPYING

%ldconfig_post
%ldconfig_postun

%files
%{_libdir}/libXt.so.6
%{_libdir}/libXt.so.6.0.0
%dir %{_datadir}/X11/app-defaults
# not using %%doc because of side-effect (#1001246)
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/COPYING

%files devel
%{_docdir}/%{name}/*.xml
%{_includedir}/X11/CallbackI.h
%{_includedir}/X11/Composite.h
%{_includedir}/X11/CompositeP.h
%{_includedir}/X11/ConstrainP.h
%{_includedir}/X11/Constraint.h
%{_includedir}/X11/ConvertI.h
%{_includedir}/X11/Core.h
%{_includedir}/X11/CoreP.h
%{_includedir}/X11/CreateI.h
%{_includedir}/X11/EventI.h
%{_includedir}/X11/HookObjI.h
%{_includedir}/X11/InitialI.h
%{_includedir}/X11/Intrinsic.h
%{_includedir}/X11/IntrinsicI.h
%{_includedir}/X11/IntrinsicP.h
%{_includedir}/X11/Object.h
%{_includedir}/X11/ObjectP.h
%{_includedir}/X11/PassivGraI.h
%{_includedir}/X11/RectObj.h
%{_includedir}/X11/RectObjP.h
%{_includedir}/X11/ResConfigP.h
%{_includedir}/X11/ResourceI.h
%{_includedir}/X11/SelectionI.h
%{_includedir}/X11/Shell.h
%{_includedir}/X11/ShellI.h
%{_includedir}/X11/ShellP.h
%{_includedir}/X11/StringDefs.h
%{_includedir}/X11/ThreadsI.h
%{_includedir}/X11/TranslateI.h
%{_includedir}/X11/VarargsI.h
%{_includedir}/X11/Vendor.h
%{_includedir}/X11/VendorP.h
%{_includedir}/X11/Xtos.h
%{_libdir}/libXt.so
%{_libdir}/pkgconfig/xt.pc
%{_mandir}/man3/*.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.1-4
- Import
