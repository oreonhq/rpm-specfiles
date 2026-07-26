%global source0_hash 3214d5f00e9703b5e8c9e7c3287d606dedec7285ceb4d5db332e93ada66fd575

%global xfceversion 4.10

Name:           xfwm4-themes
Version:        4.10.0
Release:        27%{?dist}
Summary:        Additional themes for xfwm4

# Automatically converted from old format: GPL+ and BSD - review is highly recommended.
License:        GPL-1.0-or-later AND LicenseRef-Callaway-BSD
URL:            http://www.xfce.org/
#VCS git:git://git.xfce.org/xfce/xfwm4-themes
Source0:        http://archive.xfce.org/src/art/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2

BuildRequires:  make
Requires:       xfwm4 filesystem
BuildArch:      noarch

%description
A set of additional themes for the xfwm4 window manager.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc README TODO COPYING AUTHORS
%{_datadir}/themes/*

%changelog
%autochangelog
