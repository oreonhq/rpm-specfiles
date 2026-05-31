%global source0_hash 62c34e21d06264687faea7edbf63632c9f04d55e72114aa4a57bb95e4f888a0b

Name:		xcb-util-wm
Version:	0.4.2
Release:	9%{?dist}
Summary:	Client and window-manager helper library on top of libxcb
License:	X11-distribute-modifications-variant
URL:		http://xcb.freedesktop.org
Source0:        http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.xz
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	pkgconfig(xcb-util) >= 0.3.8
BuildRequires:	m4

%description
XCB util-wm module provides the following libraries:

  - ewmh: Both client and window-manager helpers for EWMH.
  - icccm: Both client and window-manager helpers for ICCCM.


%package	devel
Summary:	Development and header files for xcb-util-vm
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
Development files for xcb-util-wm.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q


%build
%configure --with-pic --disable-static --disable-silent-rules
%make_build


%check
make check


%install
%make_install
rm %{buildroot}%{_libdir}/*.la


%ldconfig_post


%ldconfig_postun


%files
%doc README.md
%if 0%{?_licensedir:1}
%license COPYING
%else
%doc COPYING
%endif
%{_libdir}/*.so.*


%files devel
%doc NEWS
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/xcb/*.h


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.2-9
- Prepare for Oreon 11 (RP1)
