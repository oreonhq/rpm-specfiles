Name:		xcb-util-cursor
Version:	0.1.6
Release:	%autorelease
Summary:	Cursor library on top of libxcb
License:	X11-distribute-modifications-variant
URL:		http://xcb.freedesktop.org
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 fdeb8bd127873519be5cc70dcd0d3b5d33b667877200f9925a59fdcad8f7a933
%global source0_file xcb-util-cursor-0.1.6.tar.xz
# oreon url source checksums end
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	pkgconfig(xcb-util) >= 0.3.8
BuildRequires:	pkgconfig(xcb-render)
BuildRequires:	pkgconfig(xcb-renderutil)
BuildRequires:	pkgconfig(xcb-image)
BuildRequires:	m4

%description
XCB util-cursor module provides the following libraries:

  - cursor: port of libxcursor


%package	devel
Summary:	Development and header files for xcb-util-cursos
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
Development files for xcb-util-cursor.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/xcb-util-cursor-0.1.6.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "fdeb8bd127873519be5cc70dcd0d3b5d33b667877200f9925a59fdcad8f7a933" || { echo "oreon: Source0 SHA256 mismatch for xcb-util-cursor-0.1.6.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q


%build
%configure --with-pic --disable-static --disable-silent-rules
make %{?_smp_mflags}


%check
make check


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm %{buildroot}%{_libdir}/*.la


%ldconfig_post


%ldconfig_postun


%files
%doc README.md
%license COPYING
%{_libdir}/*.so.*


%files devel
%doc NEWS
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/xcb/*.h


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.6-1
- Prepare for Oreon 11 (RP1)
