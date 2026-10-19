%global source0_hash 9494aef0911a031c53670725b5c8c9bb9d3f7c5ea7318b1f72ddd9dcbbeceb6a
%global pkgname xdm
Summary:        X.Org X11 xdm - X Display Manager
Name: xorg-x11-%{pkgname}
Version: 1.1.17
Release:        3%{?dist}
Epoch: 1
License: MIT
URL: http://www.x.org
Source0:        https://ftp.x.org/pub/individual/app/xdm-%{version}.tar.xz
Source1: Xsetup_0
Source10: xdm.init
Source11: xdm.pamd
Patch1: xdm-1.0.5-sessreg-utmp-fix-bug177890.patch
Patch2: xdm-1.1.14-add-audit-events.patch
Patch3: xdm-1.1.14-xdm-systemd-unit.patch
Patch4: xdm-1.1.14-add-nolisten-tcp-option.patch
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Provides: xdm = %{version}-%{release}
Requires: pam
Requires: xorg-x11-xinit
Requires: sessreg
# oreon:deps
BuildRequires:  audit-libs-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXau-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXdmcp-devel
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXt-devel
BuildRequires:  libtool
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  xorg-x11-util-macros
BuildRequires:  xorg-x11-xtrans-devel
# /oreon:deps
%description
X.Org X11 xdm - X Display Manager

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkgname}-%{version}

%patch -P 1 -p0 -b .redhat-sessreg-utmp-fix-bug177890
%patch -P 2 -p1 -b .add-audit-events
%patch -P 3 -p1 -b .systemd-unit
%patch -P 4 -p1 -b .nolisten

%build

autoreconf -v --install
%configure \
	--disable-static \
	--with-libaudit \
	--with-xdmlibdir=%{_libexecdir} \
	--with-xdmconfigdir=%{_sysconfdir}/X11/xdm \
	--with-xdmscriptdir=%{_sysconfdir}/X11/xdm \
	--with-pixmapdir=%{_datadir}/xdm/pixmaps \
	--enable-xdmshell
%make_build
%install
echo looking for xdmshell
find . -name \*xdmshell\*
%make_install
echo looking for xdmshell
find %{buildroot} -name \*xdmshell\*
find %{buildroot} -name '*.la' -exec rm -f {} ';'
install -p -m 755 %{SOURCE1} %{buildroot}%{_sysconfdir}/X11/xdm/Xsetup_0
{
   mkdir -p %{buildroot}%{_sysconfdir}/pam.d
   install -p -m 644 %{SOURCE11} %{buildroot}%{_sysconfdir}/pam.d/xdm
}
rm -f %{buildroot}%{_sysconfdir}/X11/xdm/Xsession
(cd %{buildroot}%{_sysconfdir}/X11/xdm; ln -sf ../xinit/Xsession .)
mkdir -p %{buildroot}%{_sharedstatedir}/xdm
%oreon_autofiles main

%post

%systemd_post xdm.service
%preun

%systemd_preun xdm.service
%postun

%systemd_postun xdm.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
