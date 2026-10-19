%global source0_hash 7c7091e9c86196148bd41177b4590dccb1510bfe6cea5bf7407ff194482eb049
Name:		libftdi
Version:	1.5
Release:        1%{?dist}
Summary:        Library to program and control the FTDI USB controller
License:	LGPL-2.1-only AND GPL-2.0-only AND GPL-2.0-or-later AND (GPL-2.0-only WITH eCos-exception-2.0) AND MIT AND BSD-2-Clause-Views
URL:		https://www.intra2net.com/en/developer/libftdi/
Source0:        https://www.intra2net.com/en/developer/%{name}/download/%{name}1-%{version}.tar.bz2
Patch0:		libftdi-1.5-fix_pkgconfig_path.patch
Patch1:		libftdi-1.5-no-distutils.patch
Patch2:		libftdi-1.5-cmake-deps.patch
Patch3:		libftdi-1.5-swig-4.3.patch
Patch4:		libftdi-1.5-cmake.patch
Requires:	systemd
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libconfuse-devel
BuildRequires:  libusbx-devel
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  swig
BuildRequires:  systemd
# /oreon:deps
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
%oreon_autofiles python3-libftdi usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%cmake_build -t check
%files -f %{oreon_filedir}/main.list
%files -n libftdi-devel -f %{oreon_filedir}/libftdi-devel.list
%files -n python3-libftdi -f %{oreon_filedir}/python3-libftdi.list

%changelog

%autochangelog

