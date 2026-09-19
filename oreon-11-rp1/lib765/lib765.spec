%global source0_hash 285a5ff49c093df0d2db4471cc099db9fc0edc1981175c240d30e02dd40a99f0

Name:           lib765
Version:        0.4.2
Release:        34%{?dist}
Summary:        A library for emulating the uPD765a floppy controller
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.seasip.demon.co.uk/Unix/LibDsk
Source0:        http://www.seasip.demon.co.uk/Unix/LibDsk/%{name}-%{version}.tar.gz
BuildRequires: libtool
BuildRequires: gettext
BuildRequires: libdsk-devel
BuildRequires: make

%description
A library for emulating the uPD765a floppy controller as found on the Spectrum
+3, Amstrad CPC and PCW.

%package devel
Summary:    Development files for lib765
Requires:   libdsk-devel
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for lib765.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
#shiped libtool stuff seems broken on x86_64
autoreconf -if
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
find %{buildroot} -name \*\.la -print | xargs rm -f

%ldconfig_scriptlets

%files
%doc ChangeLog
%{_libdir}/lib765.so.*

%files devel
%doc doc/COPYING.LIB doc/765.txt
%{_libdir}/lib765.so
%{_includedir}/765.h

%changelog
%autochangelog
