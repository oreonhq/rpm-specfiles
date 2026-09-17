%global source0_hash 864fcfcd5e23a2ba4ae419d20531f8b8d5d0e1ef91415872e2b57b09ba48f799

Name:		libvpd
Version:	2.2.10
Release:	5%{?dist}
Summary:	VPD Database access library for lsvpd

License:	LGPL-2.0-or-later
URL:		https://github.com/power-ras/%{name}/releases
Source:		https://github.com/power-ras/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
./bootstrap.sh
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete

# /usr/bin/touch is required by 90-vpdupdate.rules, make sure it's in initrd
mkdir -p %{buildroot}/usr/lib/dracut/dracut.conf.d
echo 'install_items+=" /usr/bin/touch "' > %{buildroot}/usr/lib/dracut/dracut.conf.d/99-libvpd.conf

# move 90-vpdupdate.rules to system-wide directory
mkdir -p %{buildroot}/%{_udevrulesdir}
mv %{buildroot}%{_sysconfdir}/udev/rules.d/90-vpdupdate.rules %{buildroot}/%{_udevrulesdir}

%files
%license COPYING
%doc README
%{_libdir}/libvpd_cxx-2.2.so.*
%{_libdir}/libvpd-2.2.so.*
%{_udevrulesdir}/90-vpdupdate.rules
/usr/lib/dracut/dracut.conf.d/99-libvpd.conf

%files devel
%{_includedir}/libvpd-2
%{_libdir}/libvpd_cxx.so
%{_libdir}/libvpd.so
%{_libdir}/pkgconfig/libvpd-2.pc
%{_libdir}/pkgconfig/libvpd_cxx-2.pc

%changelog
%autochangelog
