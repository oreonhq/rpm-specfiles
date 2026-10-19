%global source0_hash 8b15f0a880ab87280c40cfd7235cfff28134bf14d5646c07518b1ff6642a2473
Name:           i2c-tools
Version:        4.4
Release:        1%{?dist}
Summary:        A heterogeneous set of I2C tools for Linux
License:        GPL-2.0-or-later
URL:            https://i2c.wiki.kernel.org/index.php/I2C_Tools
Source0:        https://www.kernel.org/pub/software/utils/i2c-tools/%{name}-%{version}.tar.xz
Requires:       systemd-udev kmod
Requires:       libi2c%{?_isa} = %{version}-%{release}
ExcludeArch:    s390 s390x
Obsoletes:      i2c-tools-eepromer < 4.2-2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
This package contains a heterogeneous set of I2C tools for Linux: a bus
probing tool, a chip dumper, register-level access helpers, EEPROM
decoding scripts, and more.

%package -n python3-i2c-tools
Summary:        Python 3 bindings for Linux SMBus access through i2c-dev
License:        GPL-2.0-only
%{?python_provide:%python_provide python3-i2c-tools}
Requires:       libi2c%{?_isa} = %{version}-%{release}
%if %{without python2}
Obsoletes: %{name}-python < 4.0-4
Obsoletes: python2-i2c-tools < 4.0-5
%endif
%description -n python3-i2c-tools
Python 3 bindings for Linux SMBus access through i2c-dev

%package perl
Summary:        i2c tools written in Perl
License:        GPL-2.0-or-later
Requires:       libi2c%{?_isa} = %{version}-%{release}
%description perl
A collection of tools written in perl for use with i2c devices.

%package -n libi2c
Summary:        I2C/SMBus bus access library
License:        LGPL-2.1-or-later
%description -n libi2c
libi2c offers a way for applications to interact with the devices
connected to the I2C or SMBus buses of the system.

%package -n libi2c-devel
Summary:        Development files for the I2C library
License:        LGPL-2.1-or-later
Requires:       libi2c%{?_isa} = %{version}-%{release}
Obsoletes:      i2c-tools-devel < 4.0-1
%description -n libi2c-devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" BUILD_STATIC_LIB=0 EXTRA=eeprog
pushd py-smbus
CFLAGS="$RPM_OPT_FLAGS -I../include" LDFLAGS="$RPM_LD_FLAGS" \
  %{__python3} setup.py build -b build-py3
popd
%install
make install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} BUILD_STATIC_LIB=0 \
  EXTRA=eeprog libdir=%{_libdir} bindir=%{_bindir} sbindir=%{_sbindir}
pushd py-smbus
%{__python3} setup.py build -b build-py3 install --skip-build --root=$RPM_BUILD_ROOT
popd
rm -f $RPM_BUILD_ROOT%{_bindir}/decode-edid.pl
rm -f $RPM_BUILD_ROOT%{_bindir}/{ddcmon,decode-edid}
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/modprobe.d 
echo "alias char-major-89-* i2c-dev" > \
  $RPM_BUILD_ROOT%{_prefix}/lib/modprobe.d/i2c-dev.conf
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/udev/makedev.d
for (( i = 0 ; i < 8 ; i++ )) do
  echo "i2c-$i" >> $RPM_BUILD_ROOT%{_sysconfdir}/udev/makedev.d/99-i2c-dev.nodes
done
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/modules-load.d
echo 'i2c-dev' > $RPM_BUILD_ROOT%{_prefix}/lib/modules-load.d/%{name}.conf
%oreon_autofiles python3-i2c-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles libi2c usr/*/lib*.so.*
%oreon_autofiles libi2c-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

if [ "$1" = 1 ] ; then
  /usr/sbin/modprobe i2c-dev
fi
exit 0
%ldconfig_post -n libi2c
%ldconfig_postun -n libi2c
%files -f %{oreon_filedir}/main.list
%files -n python3-i2c-tools -f %{oreon_filedir}/python3-i2c-tools.list
%files -n i2c-tools-perl -f %{oreon_filedir}/i2c-tools-perl.list
%files -n libi2c -f %{oreon_filedir}/libi2c.list
%files -n libi2c-devel -f %{oreon_filedir}/libi2c-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.4-4
- Prepare for Oreon 11 (RP1)
