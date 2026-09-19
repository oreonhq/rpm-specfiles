%global source0_hash 4407cd308ba1ab675ef4a99c56071ce2eabe374db05e8fbc391784466d03ae7d

Name:		itzam-core
Version:	2.1.1
Release:	35%{?dist}
Summary:	Library for creating and manipulating keyed-access database files

License:	GPL-3.0-or-later
URL:		http://www.coyotegulch.com/products/itzam/index.html
Source0:	http://www.coyotegulch.com/distfiles/%{name}-%{version}.tar.gz

Patch0:		itzam-core-2.1.1-itzam32.patch
Patch1:		itzam-core-2.1.1-configure-c99.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: chrpath
%description
Itzam/Core is a deliberately portable and concise C library for creating and
manipulating keyed-access database files containing variable-length, random
access records. Information is referenced by a user-defined key value;
indexes may be combined with or remain separate from data. 

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .itzam32
%patch -P1 -p1 -b .configure-c99

%build
%configure --disable-static --disable-rpath
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

cat LICENSE.NON-FREE | tr -d '\r' > LICENSE.NON-FREE.tmp
touch -r LICENSE.NON-FREE LICENSE.NON-FREE.tmp
mv LICENSE.NON-FREE.tmp LICENSE.NON-FREE

chrpath --delete $RPM_BUILD_ROOT%{_bindir}/itzam_exercise
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/itzam_bigfile
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/itzam_data_tests
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/itzam_dump_records

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING LICENSE.GPL LICENSE.NON-FREE LICENSE.POLICY NEWS README
%{_libdir}/*.so.*
%{_bindir}/*

%files devel
%{_includedir}/*
%{_libdir}/*.so

%changelog
%autochangelog
