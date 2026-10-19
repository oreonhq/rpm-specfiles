%global source0_hash ffd50b7f963fa9b8ded3223c4786b07906c887ed900de64581a24ff201444cee
Name:		garmintools
Version:	0.10
Release:        1%{?dist}
Summary:        Tools for Garmin GPS-devices
License:	GPL-2.0-or-later
URL:		https://%{name}.googlecode.com
Source0:        https://%{name}.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		garmintools-0.10_gpx-laps-hr-cad.patch
Patch1:		garmintools-0.10_fix-gcc-48.patch
Requires:	systemd-udev
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libusb-compat-0.1-devel
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
This software provides Linux users with the ability to communicate
with the Garmin Forerunner 305 via the USB interface.  It
implements all of the documented Garmin protocols as of Rev C
(May 19, 2006) over the USB physical link.

This means that if you have a Garmin with a USB connection to a PC,
you ought to be able to use this software to communicate with it.

%package	devel
Summary:	Development-files for %{name}
Requires:	%{name}%{?_isa} == %{version}-%{release}
Requires:	libusb-compat-0.1-devel%{?_isa}
%description	devel
This package contains files for developing application using
lib%{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .gpx_laps_hr_cad
%patch -P1 -p1 -b .fix-gcc-48

%build

%configure --disable-static
sed -i -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
	-e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
	libtool
%make_build
%install
%make_install
rm -f %{buildroot}%{_libdir}/*.{,l}a
install -pm 0755 extras/fore2gmn.pl %{buildroot}%{_bindir}/fore2gmn
install -d -m 0755 \
	%{buildroot}%{_pkgdocdir} \
	%{buildroot}%{_modprobedir} \
	%{buildroot}%{_udevrulesdir}
cat >> 51-garmin.rules << EOF
ATTRS{idVendor}=="091e", ATTRS{idProduct}=="0003", MODE="0666"
EOF
cat >> %{name}.conf << EOF
blacklist garmin_gps
EOF
install -pm 0644 51-garmin.rules %{buildroot}%{_udevrulesdir}
install -pm 0644 %{name}.conf %{buildroot}%{_modprobedir}
install -pm 0644 \
	AUTHORS ChangeLog NEWS README TODO \
	%{buildroot}%{_pkgdocdir}
rm -f %{buildroot}%{_pkgdocdir}/COPYING
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

/sbin/ldconfig
/sbin/rmmod garmin_gps &>/dev/null || :
%postun -p /sbin/ldconfig

%files -f %{oreon_filedir}/main.list
%files -n garmintools-devel -f %{oreon_filedir}/garmintools-devel.list

%changelog

%autochangelog
