%global source0_hash 84cd2a481a27970ec39b5c95f72db026722904a2ccf3fdbd57b280cf2d02b5c4

Name:           gmime30
Version:        3.2.15
Release:        4%{?dist}
Summary:        Library for creating and parsing MIME messages

# The library is LGPL-2.1-or-later; various files (which we don't package)
# in examples/ and tests/ are GPL-2.0-or-later.
License:        LGPL-2.1-or-later
URL:            https://github.com/jstedfast/gmime
Source0:        https://github.com/jstedfast/gmime/releases/download/%{version}/gmime-%{version}.tar.xz

BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  make
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(gpg-error)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  vala

%description
The GMime suite provides a core library and set of utilities which may be
used for the creation and parsing of messages using the Multipurpose
Internet Mail Extension (MIME).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n gmime-%{version}

%build
%configure --disable-static
%make_build V=1

%install
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -delete

%files
%license COPYING
%doc AUTHORS README
%{_libdir}/libgmime-3.0.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GMime-3.0.typelib

%files devel
%{_libdir}/libgmime-3.0.so
%{_libdir}/pkgconfig/gmime-3.0.pc
%{_includedir}/gmime-3.0/
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GMime-3.0.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/gmime-3.*/
%{_datadir}/vala/

%changelog
%autochangelog
