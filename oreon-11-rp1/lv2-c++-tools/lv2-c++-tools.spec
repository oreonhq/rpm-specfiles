%global source0_hash 6ce16a51a37259a45d8a7a59f39a6c36fc09b4c700dd26244a9dada241864e3b

Summary:	Support library for writing LV2 plugins in C++
Name:		lv2-c++-tools
Version:	1.0.5
Release:	27%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		http://ll-plugins.nongnu.org/hacking.html
Source0:	http://download.savannah.nongnu.org/releases/ll-plugins/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	gcc-c++
BuildRequires:	gtkmm24-devel
BuildRequires:	lv2-devel

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
# this doesn't use GNU configure
./configure --prefix=%{_prefix} \
	--lv2peg_LDFLAGS="-lboost_system" \
	--CFLAGS="%{optflags}" \
	--LDFLAGS="$RPM_LD_FLAGS"
make %{?_smp_mflags}

# Build the devel doc
doxygen

%install
make libdir=%{_libdir} DESTDIR=%{buildroot} install

# We don't want this static library. The other ones are needed though
rm -f %{buildroot}%{_libdir}/libpaq.a

# We will put the AUTHORS COPYING ChangeLog README files
# into the proper location
rm -f %{buildroot}%{_docdir}/%{name}/*

# Add missing symlink
ln -sf libpaq.so.0.0.0 %{buildroot}%{_libdir}/libpaq.so.0

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/lib*.so.*

%files devel
%doc html/*
%{_bindir}/*
%{_includedir}/%{name}/
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
