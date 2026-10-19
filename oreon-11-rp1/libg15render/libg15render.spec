%global source0_hash 50124bf451e27b32f4fd2e72b0eaac09f3b8a7c54375476ee81dfee84e9285be
%global svnrev 316
Name:           libg15render
Version:        1.3.0
Release:        1%{?dist}
Summary:        Library for rendering bitmaps for the Logitech G15 keyboard LCD
License:        GPL-2.0-or-later
URL:            https://sourceforge.net/projects/g15tools/
Source0:        ftp://ftp.nluug.nl/pub/os/Linux/distr/debian/pool/main/libg/%{name}/%{name}_%{version}~svn%{svnrev}.orig.tar.gz
# oreon:deps
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
libg15render is a library for rendering bitmaps in the format expected
by the LCD screen on the Logitech G15 (and similar) keyboards.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       freetype-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}.svn%{svnrev}
autoreconf -ivf

%build

%configure --disable-static --enable-ttf
%make_build
%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -r $RPM_BUILD_ROOT%{_docdir}/%{name}-1.3
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libg15render-devel -f %{oreon_filedir}/libg15render-devel.list

%changelog

%autochangelog
