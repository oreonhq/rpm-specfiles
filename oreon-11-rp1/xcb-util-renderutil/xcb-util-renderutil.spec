Name:		xcb-util-renderutil
Version:	0.3.10
Release:	9%{?dist}
Summary:	Convenience functions for the Render extension
License:	X11-distribute-modifications-variant AND HPND-sell-variant
URL:		http://xcb.freedesktop.org
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 3e15d4f0e22d8ddbfbb9f5d77db43eacd7a304029bf25a6166cc63caa96d04ba
%global source0_file xcb-util-renderutil-0.3.10.tar.xz
# oreon url source checksums end
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	pkgconfig(xcb-util) >= 0.3.8
BuildRequires:	m4

%description
XCB util-renderutil module provides the following library:

  - renderutil: Convenience functions for the Render extension.


%package	devel
Summary:	Development and header files for xcb-util-renderutil
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
Development files for xcb-util-renderutil.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/xcb-util-renderutil-0.3.10.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3e15d4f0e22d8ddbfbb9f5d77db43eacd7a304029bf25a6166cc63caa96d04ba" || { echo "oreon: Source0 SHA256 mismatch for xcb-util-renderutil-0.3.10.tar.xz" >&2; exit 1; })
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.10-9
- Prepare for Oreon 11 (RP1)
