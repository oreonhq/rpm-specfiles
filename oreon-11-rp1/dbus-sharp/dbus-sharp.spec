%global source0_hash 0866c001f2d6e01a6f1b4d080db08d25ba1422e34c7d03020e0e70f3de3a9859

%define debug_package %{nil}

Summary: C# bindings for D-Bus
Name: dbus-sharp
Version: 0.8.1
Release: 26%{?dist}
Epoch: 2
URL: http://mono.github.com/dbus-sharp/
Source0: https://github.com/downloads/mono/dbus-sharp/%{name}-%{version}.tar.gz
Patch0: dbus-sharp-0.8.1-fix-framework.patch
Patch1: dbus-sharp-0.8.1-enable-dbus-property-extraction.patch
Patch2: dbus-sharp-0.8.1-fix-array-writing.patch
Patch3: dbus-sharp-0.8.1-no-check-exists.patch
Patch4: dbus-sharp-0.8.1-mono-4.8-cleanups.patch
# based on https://github.com/mono/dbus-sharp/pull/23/commits/fb4ce33375bd4693e418089e2f379554ee52df67
Patch5: dbus-sharp-0.8.1-trapping.patch
License: MIT
BuildRequires: mono-devel
BuildRequires: autoconf, automake, libtool
BuildRequires: make
# Mono only available on these:
ExclusiveArch: %mono_arches

%description
D-Bus mono bindings for use with mono programs.

%package devel
Summary: Development files for D-Bus Sharp
Requires: %name = %{epoch}:%{version}-%{release}
Requires: pkgconfig

%description devel
Development files for D-Bus Sharp development.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .fixframework
%patch -P1 -p1 -b .propfix
# %%patch2 -p1 -b .fixarray
%patch -P3 -p1 -b .nocheckexists
%patch -P4 -p1 -b .cleanups
%patch -P5 -p1 -b .trapping

sed -i "s#gmcs#mcs#g" configure
sed -i "s#gmcs#mcs#g" configure.ac

%build
autoreconf -vif
export MONO_SHARED_DIR=%{_builddir}/%{?buildsubdir}
%configure --libdir=%{_prefix}/lib
export NoCompilerStandardLib=false
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
test "%{_libdir}" = "%{_prefix}/lib" || mv $RPM_BUILD_ROOT/%{_prefix}/lib/pkgconfig/* $RPM_BUILD_ROOT/%{_libdir}/pkgconfig

%files
%doc COPYING README
%{_prefix}/lib/mono/dbus-sharp-2.0
%{_prefix}/lib/mono/gac/dbus-sharp

%files devel
%{_libdir}/pkgconfig/dbus-sharp-2.0.pc

%changelog
%autochangelog
