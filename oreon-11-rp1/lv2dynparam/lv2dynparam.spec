%global source0_hash 209d9c03936510619c582bf8116657f14210c653788aa38efc615274aac9d82d

Summary:	LV2 dynamic parameters extension
Name:		lv2dynparam
Version:	2
Release:	34%{?dist}
License:	GPL-2.0-only
URL:		http://home.gna.org/lv2dynparam/
Source:		http://download.gna.org/lv2dynparam/lv2dynparam1-2.tar.bz2

BuildRequires: make
BuildRequires:	gcc
BuildRequires:	lv2-devel

%description
lv2dynparam is a LV2 plugin interface extension that enables plugin parameters
to appear and disappear (i.e. number of voices). It also allows nested grouping
of parameters. Groups can be used for things like ADSR abstraction, i.e. group
of 4 float parameters.

The extension should be suitable for all plugins that expose many and/or
complex data types, like samplers, non-trivial synths, etc.

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
This package contains libraries and header files for developing plugins that
use LV2 dynamic parameters extension.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}1-%{version}

# lv2core seemingly permanently renamed to lv2 at version 1.16
# A proper fix involves invoking autotools, however as this package is
# dead upstream a quick hack is sufficient.
sed -i s/lv2core/lv2/g configure

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

# Kill .la files
rm -f %{buildroot}%{_libdir}/*.la

%files
%doc AUTHORS README NEWS
%license COPYING
%{_libdir}/lib%{name}host1.so.*
%{_libdir}/lib%{name}plugin1.so.*

%files devel
%{_includedir}/%{name}1
%{_libdir}/lib%{name}host1.so
%{_libdir}/lib%{name}plugin1.so
%{_libdir}/pkgconfig/%{name}host1.pc
%{_libdir}/pkgconfig/%{name}plugin1.pc

%changelog
%autochangelog
