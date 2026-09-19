%global source0_hash ffd50b7f963fa9b8ded3223c4786b07906c887ed900de64581a24ff201444cee

Name:		garmintools
Version:	0.10
Release:	34%{?dist}
Summary:	Tools for Garmin GPS-devices

License:	GPL-2.0-or-later
URL:		https://%{name}.googlecode.com
Source0:	%{url}/files/%{name}-%{version}.tar.gz

# Fix for gpx_laps_hr_cad
# See: https://code.google.com/p/garmintools/issues/detail?id=15
Patch0:		garmintools-0.10_gpx-laps-hr-cad.patch
# Fix for garmin_save_runs
# See: https://code.google.com/p/garmintools/issues/detail?id=35
Patch1:		garmintools-0.10_fix-gcc-48.patch

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	libusb-compat-0.1-devel
BuildRequires:	perl-generators
BuildRequires:	systemd-rpm-macros

Requires:	systemd-udev

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

# Kill rpath.
sed -i -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
	-e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
	libtool

%make_build

%install
%make_install

# We intentionally do NOT ship libtool-dumplings.
rm -f %{buildroot}%{_libdir}/*.{,l}a

# Install additional tools.
install -pm 0755 extras/fore2gmn.pl %{buildroot}%{_bindir}/fore2gmn

# Create needed dirs.
install -d -m 0755 \
	%{buildroot}%{_pkgdocdir} \
	%{buildroot}%{_modprobedir} \
	%{buildroot}%{_udevrulesdir}

# Create needed config.
cat >> 51-garmin.rules << EOF
ATTRS{idVendor}=="091e", ATTRS{idProduct}=="0003", MODE="0666"
EOF

cat >> %{name}.conf << EOF
# stop garmin_gps serial from loading for USB garmin devices
blacklist garmin_gps
EOF

install -pm 0644 51-garmin.rules %{buildroot}%{_udevrulesdir}
install -pm 0644 %{name}.conf %{buildroot}%{_modprobedir}

# Install documentation-files.
install -pm 0644 \
	AUTHORS ChangeLog NEWS README TODO \
	%{buildroot}%{_pkgdocdir}
rm -f %{buildroot}%{_pkgdocdir}/COPYING

%post
/sbin/ldconfig
# Remove garmin_gps module if loaded, see README.
/sbin/rmmod garmin_gps &>/dev/null || :

%postun -p /sbin/ldconfig

%files
%license COPYING
%config(noreplace) %{_modprobedir}/%{name}.conf
%config(noreplace) %{_udevrulesdir}/51-garmin.rules
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%{_bindir}/fore2gmn
%{_bindir}/garmin_*
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/*.1*

%files devel
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/AUTHORS
%doc %{_pkgdocdir}/ChangeLog
%doc %{_pkgdocdir}/NEWS
%doc %{_pkgdocdir}/TODO
%{_includedir}/garmin.h
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
