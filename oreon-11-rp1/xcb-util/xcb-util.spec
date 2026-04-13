Name:		xcb-util
Version:	0.4.1
Release:	9%{?dist}
Summary:	Convenience libraries sitting on top of libxcb
License:	X11-distribute-modifications-variant
URL:		http://xcb.freedesktop.org
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.xz
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	pkgconfig(xcb) >= 1.4


%description
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.


%package	devel
Summary:	Development and header files for xcb-util
Requires:	%{name}%{?isa} = %{version}-%{release}

%description	devel
Development files for xcb-util.


%prep
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
%{_libdir}/libxcb-util.so.1*


%files devel
%doc NEWS
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/xcb/*.h


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.1-9
- Prepare for Oreon 11 (RP1)
