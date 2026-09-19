%global source0_hash d8c8782e4f3aedb2e5f5fc2b5ea1586555e08067e24da17a64582e971dc3aca8

%define		pkgtimestamp	20081027

Name:           tempest
# There is no version, so we use pre-release style versioning with a date
Version:        0
Release:        0.42.%{pkgtimestamp}%{?dist}
Summary:        Tempest OpenGL screensaver

# tempest.c	GPL-2.0-or-later
# vroot.h		HPND
# SPDX confimed
License:        GPL-2.0-or-later AND HPND
URL:            http://www.personal.utulsa.edu/~dan-guernsey
Source0:        http://www.personal.utulsa.edu/~dan-guernsey/dist/%{name}.tar.gz
Source1:        %{name}.conf
Source2:        %{name}.xml
Source3:        %{name}-gss.desktop
Patch0:         %{name}-20070929-desktop.patch
BuildRequires:  gcc
BuildRequires:  libGL-devel

%description
Tempest is a screensaver based on a physical model whereby particles are
attracted to their neighbors.

%package            xscreensaver
Summary:            XScreenSaver support for %{name}
Requires:           %{name} = %{version}-%{release}
Requires(post):     xscreensaver-base
Requires(postun):   xscreensaver-base
Requires:           xscreensaver-gl-base

%description        xscreensaver
Tempest is a screensaver based on a physical model whereby particles are
attracted to their neighbors. This package contains the files needed to use the
hack with xscreensaver.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}
%patch -P0 -p0 -b .orig

#Cleanups for the debuginfo package
chmod -x %{name}.c
sed -i 's/\r//' %{name}.c

%build
gcc %{optflags} -o tempest tempest.c -lGL -lm -lX11

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m0755 %{name} %{buildroot}%{_bindir}

# For xscreensaver
mkdir -p %{buildroot}%{_datadir}/xscreensaver/{config,hacks.conf.d}
install -p -m0644 %{SOURCE1} %{buildroot}%{_datadir}/xscreensaver/hacks.conf.d/
install -p -m0644 %{SOURCE2} %{buildroot}%{_datadir}/xscreensaver/config/

%post xscreensaver
if [ -x %{_sbindir}/update-xscreensaver-hacks ] ; then
   %{_sbindir}/update-xscreensaver-hacks || :
fi

%postun xscreensaver
if [ -x %{_sbindir}/update-xscreensaver-hacks ] ; then
   %{_sbindir}/update-xscreensaver-hacks || :
fi

%files
%{_bindir}/%{name}

%files xscreensaver
%{_datadir}/xscreensaver/config/%{name}.xml
%{_datadir}/xscreensaver/hacks.conf.d/%{name}.conf

%changelog
%autochangelog
