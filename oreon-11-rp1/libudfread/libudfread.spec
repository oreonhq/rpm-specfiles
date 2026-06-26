%global source0_hash b7febc6c05af412d0dac20039a76438739986be9b22f8451a4babe69e06a2543

Name:           libudfread
Version:        1.2.0
Release:        1%{?dist}
Summary:        UDF reader library
License:        LGPL-2.0-or-later
URL:            https://code.videolan.org/videolan/libudfread
Source0:        https://code.videolan.org/videolan/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  meson

%description
This library allows reading UDF filesystems, like raw devices and image files.
The library is created and maintained by VideoLAN Project and is used by
projects like VLC and Kodi.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson -Ddefault_library=shared
%meson_build

%install
%meson_install

%files
%doc ChangeLog
%license COPYING
%{_libdir}/libudfread.so.3*

%files devel
%{_includedir}/udfread/
%{_libdir}/libudfread.so
%{_libdir}/pkgconfig/libudfread.pc

%changelog
%autochangelog
