%global source0_hash 8491c1fb6c2fee454cad4cd94ed53f6bcfa790644ff38a2c42d3dc069d08d50e

%global pkgname ll-plugins

Summary:	Collection of LV2 plugins
Name:		lv2-ll-plugins
Version:	0.2.8
Release:	41%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		http://ll-plugins.nongnu.org/
Source:		http://download.savannah.nongnu.org/releases/ll-plugins/%{pkgname}-%{version}.tar.bz2
# Patch sent to the author via email as there is no upstream tracker
# Fix 64 bit path
Patch0:		ll-plugins-lib64.patch

BuildRequires: make
BuildRequires:	gcc-c++
BuildRequires:	gtkmm24-devel
BuildRequires:	lash-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	lv2-c++-tools-static
BuildRequires:	lv2-devel

Requires:	lv2

%description
lv2-ll-plugins is a small collection of LV2 plugins, including an arpeggiator,
a MIDI keyboard, a drum-machine, a peak meter; and a host that runs them.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkgname}-%{version}
%patch -P0 -p1 -b .lib64

# Don't build and package elven as it is now a separate project
sed -i '/^PROGRAMS = elven/d' Makefile

%build
# this doesn't use GNU configure
./configure --prefix=%{_prefix} --lv2plugindir=%{_libdir}/lv2 --CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
make libdir=%{_libdir} DESTDIR=%{buildroot} install

rm -f %{buildroot}%{_docdir}/%{pkgname}/*

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/lv2/*

%changelog
%autochangelog
