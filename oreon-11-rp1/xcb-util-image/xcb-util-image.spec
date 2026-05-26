Name:		xcb-util-image
Version:	0.4.1
Release:	9%{?dist}
Summary:	Port of Xlib's XImage and XShmImage functions on top of libxcb
License:	X11-distribute-modifications-variant
URL:		http://xcb.freedesktop.org
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 ccad8ee5dadb1271fd4727ad14d9bd77a64e505608766c4e98267d9aede40d3d
%global source0_file xcb-util-image-0.4.1.tar.xz
# oreon url source checksums end
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	pkgconfig(xcb-util) >= 0.3.8
BuildRequires:	m4

%description
XCB util-image module provides the following library:

  - image: Port of Xlib's XImage and XShmImage functions.


%package	devel
Summary:	Development and header files for xcb-util-image
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
Development files for xcb-util-image.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/xcb-util-image-0.4.1.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ccad8ee5dadb1271fd4727ad14d9bd77a64e505608766c4e98267d9aede40d3d" || { echo "oreon: Source0 SHA256 mismatch for xcb-util-image-0.4.1.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.1-9
- Prepare for Oreon 11 (RP1)
