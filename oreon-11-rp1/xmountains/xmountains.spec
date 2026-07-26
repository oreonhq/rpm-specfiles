%global source0_hash 123dddf40ed3a678a507526469f43af5e4a33bc0c0000232f78cd399c63809d0

Name:           xmountains
Version:        2.11
Release:        6%{?dist}
Summary:        A fractal terrain generator

# SPDX confirmed
License:        HPND
URL:            https://spbooth.github.io/xmountains/
Source0:        https://github.com/spbooth/xmountains/archive/v%{version}/%{name}-%{version}.tar.gz
Source11:        xscreensaver-xmountains.xml
Source12:        xscreensaver-xmountains.conf
# Need report to the upstream
# Fix for C23
Patch0:         xmountains-2.11-c23.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  xorg-x11-xbitmaps
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  libX11-devel
BuildRequires:  imake

%description
Xmountains is a fractal terrain generator written by Stephen Booth.

%package         xscreensaver
Summary:         XScreenSaver integration support
Requires(post): xscreensaver-base
Requires:        xscreensaver-base
Requires:        %{name} = %{version}-%{release}
BuildArch:       noarch

%description     xscreensaver
This package adds XScreenSaver integration.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .c23

%global optflags %optflags -Werror=implicit-function-declaration

%build
xmkmf
make %{?_smp_mflags} CCOPTIONS="$RPM_OPT_FLAGS -DANSI"

%install
make install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL="install -p" \
	%{nil}
make install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL="install -p" \
	INSTMANFLAGS="-m 0644" \
	%{nil}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/xscreensaver/{config,hacks.conf.d}
install -cpm 0644 %{SOURCE11} $RPM_BUILD_ROOT%{_datadir}/xscreensaver/config/xmountains.xml
install -cpm 0644 %{SOURCE12} $RPM_BUILD_ROOT%{_datadir}/xscreensaver/hacks.conf.d/xmountains.conf

%post xscreensaver
if [ -x %{_sbindir}/update-xscreensaver-hacks ]; then
    %{_sbindir}/update-xscreensaver-hacks
fi

%postun xscreensaver
if [ -x %{_sbindir}/update-xscreensaver-hacks ]; then
    %{_sbindir}/update-xscreensaver-hacks || :
fi

%files
%doc	README
%license	copyright.h
%{_bindir}/xmountains
%{_mandir}/man1/xmountains.1x*

%files xscreensaver
%{_datadir}/xscreensaver/*/*

%changelog
%autochangelog
