%global source0_hash b19926cc66ab341b610e2ac2ffbfda5b765bc21b3d83b3eecdae3e0f67f7f855

Name:           lpsk31
Version:        1.3
Release:        17%{?dist}
Summary:        A ncurses application for ham radio communications using PSK31 digital mode

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.5b4az.org/
Source0:        http://www.5b4az.org/pkg/psk31/%{name}/%{name}-%{version}.tar.bz2
Source1:        lpsk31-1.1-wrapper.in
Patch0:         lpsk31-1.1-makefile.patch
Patch1:         lpsk31-common.patch

BuildRequires:  gcc
BuildRequires:  alsa-lib-devel
BuildRequires:  ncurses-devel
BuildRequires: make

%description
lpsk31 is a ncurses console application for ham radio communications in the 
popular PSK31 digital mode. lpsk31 uses only integer arithmetic for both signal 
detection and audio tone synthesis, so that it needs no floating point 
calculations for its operation. lpsk31 can keep a log of QSO's in text and ADIF 
format as well as a raw log of all that is typed in the transmit window or 
displayed in the receive window. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
make CC="gcc $RPM_OPT_FLAGS" %{?_smp_mflags}

%install
%make_install

#install wrapper script
install -m 0755 -D -p %{SOURCE1} %{buildroot}%{_bindir}/lpsk31

%files
%doc AUTHORS README doc/*
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_libexecdir}/%{name}

%changelog
%autochangelog
