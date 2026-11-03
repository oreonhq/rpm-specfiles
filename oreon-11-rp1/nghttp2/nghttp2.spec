%global source0_hash 5511d3128850e01b5b26ec92bf39df15381c767a63441438b25ad6235def902c
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: nghttp2
Version: 1.68.0
Release: 2%{?dist}
Summary: HTTP/2 library
License: MIT
URL: https://nghttp2.org/
Source0: https://github.com/nghttp2/nghttp2/releases/download/v%{version}/nghttp2-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: pkgconf
BuildRequires: patchelf


%description
nghttp2 is an HTTP/2 library.

%package -n libnghttp2
Summary: nghttp2 library
Obsoletes: nghttp2 < 1.68.0-2

%description -n libnghttp2
Shared nghttp2 library.

%package -n libnghttp2-devel
Summary: Development files for libnghttp2
Requires: libnghttp2%{?_isa} = %{version}-%{release}
Obsoletes: nghttp2-devel < 1.68.0-2

%description -n libnghttp2-devel
Headers and development library for libnghttp2.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_configure --disable-static --enable-lib-only
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.a
rm -rf %{buildroot}%{_mandir}/man1 %{buildroot}%{_docdir}
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%ldconfig_scriptlets -n libnghttp2

%files -n libnghttp2
%license COPYING
%{_libdir}/libnghttp2.so.14
%{_libdir}/libnghttp2.so.14.*

%files -n libnghttp2-devel
%{_includedir}/nghttp2/
%{_libdir}/libnghttp2.so
%{_libdir}/pkgconfig/libnghttp2.pc
