Name:		xcb-util-keysyms
Version:	0.4.1
Release:	9%{?dist}
Summary:	Standard X key constants and keycodes conversion on top of libxcb
License:	X11-distribute-modifications-variant
URL:		http://xcb.freedesktop.org
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 7c260a5294412aed429df1da2f8afd3bd07b7cba3fec772fba15a613a6d5c638
%global source0_file xcb-util-keysyms-0.4.1.tar.xz
# oreon url source checksums end
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	pkgconfig(xcb-util) >= 0.3.8
BuildRequires:	m4

%description
XCB util-keysyms module provides the following library:

  - keysyms: Standard X key constants and conversion to/from keycodes.


%package	devel
Summary:	Development and header files for xcb-util-keysyms
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
Development files for xcb-util-keysyms.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/xcb-util-keysyms-0.4.1.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7c260a5294412aed429df1da2f8afd3bd07b7cba3fec772fba15a613a6d5c638" || { echo "oreon: Source0 SHA256 mismatch for xcb-util-keysyms-0.4.1.tar.xz" >&2; exit 1; })
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
%{_libdir}/*.so.*


%files devel
%doc NEWS
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/xcb/*.h


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.1-9
- Prepare for Oreon 11 (RP1)
