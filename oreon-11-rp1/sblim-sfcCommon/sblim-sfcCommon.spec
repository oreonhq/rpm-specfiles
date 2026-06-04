%global source0_hash b9b1037173d6ae0181c3bd5a316ddab5afd6a342ad0dbdc18e940fc0ad2c3297

Name:		sblim-sfcCommon
Version:	1.0.1
Release:	29%{?dist}
Summary:	Common functions for SBLIM Small Footprint CIM Broker and CIM Client Library.

License:	EPL-1.0
URL:		http://sourceforge.net/projects/sblim/
Source0:        https://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
Patch0:		sblim-sfcCommon-1.0.1-gcc15-fix.patch

BuildRequires: make
BuildRequires:	sblim-cmpi-devel
BuildRequires:	gcc gcc-c++

%description
This package provides a common library for functions
shared between Small Footprint CIM Broker (sblim-sfcb)
Small Footprint CIM Client (and sblim-sfcc).


%package	devel
Summary:	Sblim-sfcCommon Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Sblim-sfcCommon Development Files.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%autopatch -p1


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
# remove unused static libraries
rm -f %{buildroot}/%{_libdir}/libsfcUtil.a
rm -f %{buildroot}/%{_libdir}/libsfcUtil.la


%ldconfig_scriptlets


%files
%doc AUTHORS README COPYING NEWS ChangeLog
%{_libdir}/libsfcUtil.so.*


%files devel
%{_includedir}/sfcCommon
%{_libdir}/libsfcUtil.so



%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.1-29
- Prepare for Oreon 11 (RP1)
