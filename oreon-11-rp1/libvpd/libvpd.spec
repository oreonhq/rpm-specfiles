# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 557a5ead6d15d4f5a6d0e3d0ac0344cc028e17a162d9174680d41b37c99b1431
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:		libvpd
Version:	2.2.11
Release:	1%{?dist}
Summary:	VPD Database access library for lsvpd

License:	LGPL-2.0-or-later
URL:		https://github.com/power-ras/%{name}/releases
Source0:		https://github.com/power-ras/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:		99-libvpd.conf
Patch1:		libvpd-install-rules-in-system-wide-dir.patch

BuildRequires:	autoconf automake libtool
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	sqlite-devel
BuildRequires:	systemd-devel
BuildRequires:	zlib-devel

ExclusiveArch:	%{power64}

%description
The libvpd package contains the classes that are used to access a vpd database
created by vpdupdate in the lsvpd package.

%package devel
Summary:	Header files for libvpd
Requires:	%{name} = %{version}-%{release}
Requires:	sqlite-devel
%description devel
Contains header files for building with libvpd.

%prep
%oreon_verify_sources
%autosetup

%build
./bootstrap.sh
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
install -D -m644 %{SOURCE1} %{buildroot}%{_prefix}/lib/dracut/dracut.conf.d/99-libvpd.conf

%files
%license COPYING
%doc README
%{_libdir}/libvpd_cxx-2.2.so.*
%{_libdir}/libvpd-2.2.so.*
%{_udevrulesdir}/90-vpdupdate.rules
%{_prefix}/lib/dracut/dracut.conf.d/*

%files devel
%{_includedir}/libvpd-2
%{_libdir}/libvpd_cxx.so
%{_libdir}/libvpd.so
%{_libdir}/pkgconfig/libvpd-2.pc
%{_libdir}/pkgconfig/libvpd_cxx-2.pc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2.11-1
- Import
