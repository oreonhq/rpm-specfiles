%global source0_hash 285a5ff49c093df0d2db4471cc099db9fc0edc1981175c240d30e02dd40a99f0
Name:           lib765
Version:        0.4.2
Release:        34%{?dist}
Summary:        A library for emulating the uPD765a floppy controller
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.seasip.demon.co.uk/Unix/LibDsk
Source0:        http://www.seasip.demon.co.uk/Unix/LibDsk/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gettext
BuildRequires:  libdsk-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
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

autoreconf -if
%configure --disable-static
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
find %{buildroot} -name \*\.la -print | xargs rm -f
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n lib765-devel -f %{oreon_filedir}/lib765-devel.list

%changelog

%autochangelog
