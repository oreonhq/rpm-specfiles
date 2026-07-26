%global source0_hash none

Name:       virtualbox-guest-additions
Version:    7.2.6
Release:    1%{?dist}
Summary:    VirtualBox Guest Additions
License:    GPL-3.0-only AND (GPL-3.0-only OR CDDL-1.0)
URL:        https://www.virtualbox.org/wiki/VirtualBox

Source0:    https://download.virtualbox.org/virtualbox/%{version}/VirtualBox-%{version}.tar.bz2
Source1:    vboxservice.service
Source3:    VirtualBox-60-vboxguest.rules
Source4:    vboxclient.service
Source5:    mount.vboxsf

Patch60:    VirtualBox-7.0.2-xclient-cleanups.patch
#from Gentoo
Patch80:    029_virtualbox-7.1.4_C23.patch

BuildRequires:  gcc-c++
BuildRequires:  kBuild >= 0.1.9998.r3093
BuildRequires:  openssl-devel
BuildRequires:  yasm
BuildRequires:  alsa-lib-devel
BuildRequires:  pulseaudio-libs-devel
# for xsltproc
BuildRequires:  libxslt
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  desktop-file-utils
BuildRequires:  pam-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  makeself
BuildRequires:  libXmu-devel
BuildRequires:  libX11-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXt-devel
# For the OpenGL passthru libs, these are statically linked against libstdc++
# like mesa itself is to avoid trouble with game-runtimes providing their
# own older libstdc++ (e.g. steam does this)
BuildRequires:  libstdc++-static
%{?systemd_requires}
BuildRequires: systemd

# Obsoletes/provides for upgrade path from the rpmfusion guest-additions pkg
Obsoletes:      VirtualBox-guest-additions < %{version}-%{release}
Provides:       VirtualBox-guest-additions = %{version}-%{release}
# VirtualBox guests are always x86, no need to build for other archs
ExclusiveArch:  i686 x86_64

# kernel 5.6.14 have the fixes for vboxguest on VBox 6.1.x
Requires: kernel >= 5.6.14

# VBoxOGL was removed in 6.1.0
# we need obsolete it to fix upgrade path
Obsoletes:  %{name}-ogl < 6.0.14-2

%description
This package replaces the application of Virtualbox's own methodology to
install Guest Additions (in menu: Devices -> Insert Guest Additions CD Image).
VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for
enterprise as well as home use. This package contains the VirtualBox
Guest Additions which support better integration of VirtualBox guests
with the Host, including file sharing, clipboard sharing and Seamless mode.
Additional note: this package can be installed on an non-guest system, because
it is harmless and services would not run anyway.

%prep
%autosetup -p1 -n VirtualBox-%{version}
# Remove prebuilt binaries
find -name '*.py[co]' -delete
rm -r src/VBox/Additions/win
rm -r src/VBox/Additions/os2
rm -r kBuild/
rm -r tools/
# Remove bundle X11 sources and some lib sources, before patching.
rm -r src/VBox/Additions/x11/x11include/
rm -r src/VBox/Additions/3D/mesa/mesa-24.0.2/
rm -r src/VBox/Runtime/r3/darwin
rm -r src/VBox/Runtime/r0drv/darwin
rm -r src/VBox/Runtime/darwin
rm -r src/libs/liblzf-3.*/
rm -r src/libs/libpng-1.6.*/
rm -r src/libs/libxml2-2.*/
rm -r src/libs/openssl-3.*/
rm -r src/libs/zlib-1.3.*/
rm -r src/libs/curl-8.*/
rm -r src/libs/libvorbis-1.3.*/
rm -r src/libs/libogg-1.3.*/
rm -r src/libs/liblzma-5.*/
rm -r src/libs/libtpms-0.10.*/

# Create a sysusers.d config file
cat >virtualbox-guest-additions.sysusers.conf <<EOF
# Group "vboxsf" for Shared Folders access.
# All users which want to access the auto-mounted Shared Folders
# have to be added to this group.
g vboxsf -
u vboxadd -:1 - /var/run/vboxadd -
EOF

%build
./configure --only-additions --disable-kmods
. ./env.sh
umask 0022

# VirtualBox build system installs and builds in the same step,
# not always looking for the installed files in places they have
# really been installed to. Therefore we do not override any of
# the installation paths
kmk %{_smp_mflags}                                             \
    VBOX_ONLY_ADDITIONS=1                                      \
    KBUILD_VERBOSE=2                                           \
    TOOL_YASM_AS=yasm                                          \
    VBOX_USE_SYSTEM_XORG_HEADERS=1                             \
    VBOX_USE_SYSTEM_GL_HEADERS=1                               \
    VBOX_NO_LEGACY_XORG_X11=1                                  \
    SDK_VBoxLibPng_INCS=/usr/include/libpng16                 \
    SDK_VBoxLibXml2_INCS=/usr/include/libxml2                 \
    SDK_VBoxLzf_LIBS="lzf"                                    \
    SDK_VBoxLzf_INCS="/usr/include/liblzf"                    \
    SDK_VBoxOpenSslStatic_INCS="/usr/include/openssl"                                   \
    SDK_VBoxOpenSslStatic_LIBS="ssl crypto"                         \
    SDK_VBoxLibLzma_INCS=""                                 \
    SDK_VBoxZlib_INCS=""                                      \
    VBOX_BUILD_PUBLISHER=_Fedora

%install
# The directory layout created below attempts to mimic the one of
# the commercially supported version to minimize confusion
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_libdir}/security

# Guest-additions tools
install -m 0755 -t %{buildroot}%{_sbindir}   \
    out/linux.*/release/bin/additions/VBoxService            \
    %{SOURCE5}

install -m 0755 -t %{buildroot}%{_bindir}    \
    out/linux.*/release/bin/additions/VBoxDRMClient          \
    out/linux.*/release/bin/additions/VBoxClient             \
    out/linux.*/release/bin/additions/VBoxControl            \
    out/linux.*/release/bin/additions/vboxwl

# Guest libraries
install -m 0755 -t %{buildroot}%{_libdir}/security \
    out/linux.*/release/bin/additions/pam_vbox.so

install -p -m 0755 -D src/VBox/Additions/x11/Installer/98vboxadd-xclient \
    %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d/98vboxadd-xclient.sh
ln -s ../..%{_sysconfdir}/X11/xinit/xinitrc.d/98vboxadd-xclient.sh \
    %{buildroot}%{_bindir}/VBoxClient-all
desktop-file-install --dir=%{buildroot}%{_sysconfdir}/xdg/autostart/ \
    --remove-key=Encoding src/VBox/Additions/x11/Installer/vboxclient.desktop
desktop-file-validate \
    %{buildroot}%{_sysconfdir}/xdg/autostart/vboxclient.desktop

install -p -m 0644 -D %{SOURCE1} %{buildroot}%{_unitdir}/vboxservice.service
install -p -m 0644 -D %{SOURCE3} %{buildroot}%{_udevrulesdir}/60-vboxguest.rules
install -p -m 0644 -D %{SOURCE4} %{buildroot}%{_unitdir}/vboxclient.service

install -m0644 -D virtualbox-guest-additions.sysusers.conf %{buildroot}%{_sysusersdir}/virtualbox-guest-additions.conf

%post
%systemd_post vboxclient.service
%systemd_post vboxservice.service

%preun
%systemd_preun vboxclient.service
%systemd_preun vboxservice.service

%postun
%systemd_postun_with_restart vboxclient.service
%systemd_postun_with_restart vboxservice.service

%files
%license COPYING*
%{_bindir}/vboxwl
%{_bindir}/VBoxClient
%{_bindir}/VBoxControl
%{_bindir}/VBoxClient-all
%{_bindir}/VBoxDRMClient
%{_sbindir}/VBoxService
%{_sbindir}/mount.vboxsf
%{_libdir}/security/pam_vbox.so
%{_sysconfdir}/X11/xinit/xinitrc.d/98vboxadd-xclient.sh
%{_sysconfdir}/xdg/autostart/vboxclient.desktop
%{_unitdir}/vboxclient.service
%{_unitdir}/vboxservice.service
%{_udevrulesdir}/60-vboxguest.rules
%{_sysusersdir}/virtualbox-guest-additions.conf

%changelog
%autochangelog
