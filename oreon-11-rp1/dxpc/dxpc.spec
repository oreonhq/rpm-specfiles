%global source0_hash 414c499c6aa97f061dc589733142d5be671645436938cfc02b243914a0a27de5

Summary: A Differential X Protocol Compressor
Name:    dxpc
Version: 3.9.2
Release: 31%{?dist}

# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL:     http://www.vigor.nu/%{name}/
Source:  http://www.vigor.nu/%{name}/%{name}-%{version}.tgz
Patch0: dxpc-3.9.0-mandir.patch
Patch1: dxpc-3.9.0-dxpcssh.patch
Patch2: dxpc-3.9.1b1-destdir.patch

BuildRequires:  gcc-c++
BuildRequires: lzo-devel >= 1.08
%if 0%{?fedora} > 4
BuildRequires: libXt-devel
%else
BuildRequires: xorg-x11-devel
%endif
BuildRequires: make

%description
dxpc is an X protocol compressor designed to improve the
speed of X11 applications run over low-bandwidth links
(such as dialup PPP connections or ADSL).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P0 -p1 -b .mandir
%patch -P1 -p0 -b .dxpcssh
%patch -P2 -p0 -b .destdir

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%files
%doc README CHANGES TODO
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
