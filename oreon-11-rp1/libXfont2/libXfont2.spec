%global source0_hash 8b7b82fdeba48769b69433e8e3fbb984a5f6bf368b0d5f47abeec49de3e58efb

Summary: X.Org X11 libXfont2 runtime library
Name: libXfont2
Version: 2.0.7
Release: 5%{?dist}
License: BSD-2-Clause AND BSD-4-Clause-UC AND HPND-sell-variant AND MIT-open-group AND SMLNJ AND X11
URL: http://www.x.org

Source0:        http://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig(fontsproto)
BuildRequires: xorg-x11-util-macros
BuildRequires: xorg-x11-xtrans-devel >= 1.0.3-3
BuildRequires: libfontenc-devel
BuildRequires: freetype-devel

Requires:       libfontenc%{?_isa}

%description
X.Org X11 libXfont2 runtime library

%package devel
Summary: X.Org X11 libXfont2 development package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libfontenc-devel%{?_isa}

%description devel
X.Org X11 libXfont development package

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup

%build
autoreconf -v --install --force
export CFLAGS="$RPM_OPT_FLAGS -Os"
%configure --disable-static
make %{?_smp_mflags}  

%install
%make_install

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_post
%ldconfig_postun

%files
%license COPYING
%doc AUTHORS README.md ChangeLog
%{_libdir}/libXfont2.so.2*

%files devel
%{_includedir}/X11/fonts/libxfont2.h
%{_libdir}/libXfont2.so
%{_libdir}/pkgconfig/xfont2.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.7-4
- Prepare for Oreon 11 (RP1)
