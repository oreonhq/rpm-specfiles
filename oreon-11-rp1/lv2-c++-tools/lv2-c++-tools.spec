%global source0_hash 29806062daf6356e503dd932f654a6280b2b60900c0e27bbd48cd84ecd987f5d
Summary:        Support library for writing LV2 plugins in C++
Name:		lv2-c++-tools
Version:	1.0.7
Release:        1%{?dist}
License:	GPL-3.0-or-later
URL:		http://ll-plugins.nongnu.org/hacking.html
Source0:        http://download.savannah.nongnu.org/releases/ll-plugins/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gtkmm24-devel
BuildRequires:  lv2-devel
BuildRequires:  make
# /oreon:deps
%description
This software package contains libraries and programs that should make it
easier to write LV2 plugins in C++.

%package devel
Summary:	Development files for %{name}
Provides:	%{name}-static = %{version}-%{release}
Requires:	%{name}%{_isa} = %{version}-%{release}
Requires:	pkgconfig
%description devel
This package contains libraries and header files for developing LV2 plugins
that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# We will use our lv2core
rm -f headers/lv2.h
sed -i -e '/lv2\.h/d' Makefile

%build

./configure --prefix=%{_prefix} \
	--lv2peg_LDFLAGS="-lboost_system" \
	--CFLAGS="%{optflags}" \
	--LDFLAGS="$RPM_LD_FLAGS"
make %{?_smp_mflags}
doxygen
%install
make libdir=%{_libdir} DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_libdir}/libpaq.a
rm -f %{buildroot}%{_docdir}/%{name}/*
ln -sf libpaq.so.0.0.0 %{buildroot}%{_libdir}/libpaq.so.0
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
