%global source0_hash none

Name:		libftdi
Version:	1.5
Release:	24%{?dist}
Summary:	Library to program and control the FTDI USB controller

License:	LGPL-2.1-only AND GPL-2.0-only AND GPL-2.0-or-later AND (GPL-2.0-only WITH eCos-exception-2.0) AND MIT AND BSD-2-Clause-Views
URL:		https://www.intra2net.com/en/developer/libftdi/
Source0:	https://www.intra2net.com/en/developer/%{name}/download/%{name}1-%{version}.tar.bz2

# http://developer.intra2net.com/git/?p=libftdi;a=commitdiff;h=cdb28383402d248dbc6062f4391b038375c52385;hp=5c2c58e03ea999534e8cb64906c8ae8b15536c30
Patch0:		libftdi-1.5-fix_pkgconfig_path.patch
# http://developer.intra2net.com/mailarchive/html/libftdi/2023/msg00003.html
Patch1:		libftdi-1.5-no-distutils.patch
# http://developer.intra2net.com/mailarchive/html/libftdi/2023/msg00005.html
Patch2:		libftdi-1.5-cmake-deps.patch
# Fix for SWIG 4.3.0
# https://bugzilla.redhat.com/show_bug.cgi?id=2319133
# http://developer.intra2net.com/mailarchive/html/libftdi/2024/msg00024.html
Patch3:		libftdi-1.5-swig-4.3.patch
# updates for modern cmake
# http://developer.intra2net.com/git/?p=libftdi;a=commitdiff;h=3861e7dc9e83f2f6ff4e1579cf3bbf63a6827105
# http://developer.intra2net.com/git/?p=libftdi;a=commitdiff;h=61a6bac98bbac623fb33b6153a063b6436f84721
# http://developer.intra2net.com/git/?p=libftdi;a=commitdiff;h=3dc444f99bbc780f06ee6115c086e30f2dda471a
# http://developer.intra2net.com/git/?p=libftdi;a=commitdiff;h=de9f01ece34d2fe6e842e0250a38f4b16eda2429
Patch4:		libftdi-1.5-cmake.patch

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	doxygen
BuildRequires:	boost-devel
BuildRequires:	libconfuse-devel
BuildRequires:	libusbx-devel
BuildRequires:	make
BuildRequires:	python3-devel
BuildRequires:	swig
BuildRequires:	systemd
Requires:	systemd


%description
A library (using libusb) to talk to FTDI's FT2232C,
FT232BM and FT245BM type chips including the popular bitbang mode.

%package devel
Summary:	Header files and static libraries for libftdi
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	python3-%{name}%{?_isa} = %{version}-%{release}
Requires:	cmake-filesystem

%description devel
Header files and static libraries for libftdi


%package -n python3-libftdi
%{?python_provide:%python_provide python3-libftdi}
Summary:	Libftdi library Python 3 binding
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n python3-libftdi
Libftdi Python 3 Language bindings.


%package c++
Summary:	Libftdi library C++ binding
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description c++
Libftdi library C++ language binding.


%package c++-devel
Summary:	Libftdi library C++ binding development headers and libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-c++ = %{version}-%{release}

%description c++-devel
Libftdi library C++ binding development headers and libraries
for building C++ applications with libftdi.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}1-%{version}

# switch to uaccess control
sed -i -e 's/GROUP="plugdev"/TAG+="uaccess"/g' packages/99-libftdi.rules


%build
%cmake -DSTATICLIBS=off -DFTDIPP=on -DPYTHON_BINDINGS=on -DDOCUMENTATION=on -DEXAMPLES=off -DBUILD_TESTS=on
%cmake_build

%install
%cmake_install

install -D -pm 0644 packages/99-libftdi.rules %{buildroot}%{_udevrulesdir}/69-libftdi.rules

rm -f %{buildroot}%{_datadir}/doc/libftdi1/example.conf
rm -f %{buildroot}%{_datadir}/doc/libftdipp1/example.conf


%check
%cmake_build -t check


%files
%license COPYING.LIB
%{_libdir}/libftdi1.so.2*
%{_udevrulesdir}/69-libftdi.rules

%files devel
%doc AUTHORS ChangeLog
%doc %{_datadir}/libftdi/examples
%dir %{_includedir}/libftdi1
%{_bindir}/ftdi_eeprom
%{_bindir}/libftdi1-config
%{_includedir}/libftdi1/*.h
%{_libdir}/libftdi1.so
%{_libdir}/pkgconfig/libftdi1.pc
%{_libdir}/cmake/libftdi1/

%files -n python3-libftdi
%{python3_sitearch}/*

%files c++
%{_libdir}/libftdipp1.so.2*
%{_libdir}/libftdipp1.so.3

%files c++-devel
%{_libdir}/libftdipp1.so
%{_includedir}/libftdi1/*.hpp
%{_libdir}/pkgconfig/libftdipp1.pc


%changelog
%autochangelog

