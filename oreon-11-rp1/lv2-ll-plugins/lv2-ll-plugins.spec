%global source0_hash a20d0793f31de730f950ea7f3e08f44d3cfe0e52a009bbde2e52904cdb419883
%global pkgname ll-plugins
Summary:        Collection of LV2 plugins
Name:		lv2-ll-plugins
Version:	0.2.33
Release:        1%{?dist}
License:	GPL-3.0-or-later
URL:		http://ll-plugins.nongnu.org/
Source0:        http://download.savannah.nongnu.org/releases/%{pkgname}/%{pkgname}-%{version}.tar.bz2
Patch0:		ll-plugins-lib64.patch
Requires:	lv2
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gtkmm24-devel
BuildRequires:  lash-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  lv2-c++-tools-static
BuildRequires:  lv2-devel
BuildRequires:  make
# /oreon:deps
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

./configure --prefix=%{_prefix} --lv2plugindir=%{_libdir}/lv2 --CFLAGS="%{optflags}"
make %{?_smp_mflags}
%install
make libdir=%{_libdir} DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_docdir}/%{pkgname}/*
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
