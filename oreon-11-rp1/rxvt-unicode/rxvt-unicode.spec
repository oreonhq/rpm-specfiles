%global source3_hash 8d00077fa8b16f489f3355911564de647f468b4e7a8516375a2c0ca2ee32427b
%global source2_hash 48ef5720d77a870f25737b8f66fe2c1f88a01810013df70cb8155add904288e4
%global source1_hash afea78dc25db8cd15da9959baf347b0634f4ef62dd3eeaff0c0a3389986b6a3e
%global source0_hash aaa13fcbc149fe0f3f391f933279580f74a96fd312d6ed06b8ff03c2d46672e8
Name:           rxvt-unicode
Version:        9.31
Release:        1%{?dist}
Summary:        Unicode version of rxvt
License:        GPL-3.0-or-later
URL:            http://software.schmorp.de/pkg/rxvt-unicode.html
Source0:        http://dist.schmorp.de/%{name}/%{name}-%{version}.tar.bz2
Source1:        http://dist.schmorp.de/%{name}/%{name}-%{version}.tar.bz2.sig
Source2:        http://dist.schmorp.de/signing-key.pub
Source3:        http://dist.schmorp.de/signing-key.pub.gpg.sig
Source4:        gpgkey-84874CAB6D1A397A.gpg
Source5:        rxvt-unicode.desktop
Patch0:         rxvt-unicode-9.21-Fix-hard-coded-wrong-path-to-xsubpp.patch
Patch1:         rxvt-unicode-0001-Prefer-XDG_RUNTIME_DIR-over-the-HOME.patch
Patch2:         Fix-OSC-responses-with-7-bit-ST.patch
Requires:       startup-notification
Obsoletes:      rxvt-unicode-ml <= 9.22-17
Obsoletes:      rxvt-unicode-256color <= 9.22-17
Obsoletes:      rxvt-unicode-256color-ml <= 9.22-17
Obsoletes:      rxvt <= 2.7.10-36
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  gnupg2
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXt-devel
BuildRequires:  libev-source
BuildRequires:  libptytty-devel
BuildRequires:  make
BuildRequires:  ncurses
BuildRequires:  ncurses-base
BuildRequires:  ncurses-devel
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  signify
BuildRequires:  startup-notification-devel
BuildRequires:  xorg-x11-proto-devel
# /oreon:deps
%description
rxvt-unicode is a clone of the well known terminal emulator rxvt, modified to
store text in Unicode (either UCS-2 or UCS-4) and to use locale-correct input
and output. It also supports mixing multiple fonts at the same time, including
Xft fonts.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE4}' --signature='%{SOURCE3}' --data='%{SOURCE2}'
signify -V -p '%{SOURCE2}' -m '%{SOURCE0}'
%autosetup -S git

%build

CXXFLAGS="%{optflags} -std=gnu++11" \
%configure \
    --enable-keepscrolling \
    --enable-selectionscrolling \
    --enable-pointer-blank \
    --enable-utmp \
    --enable-wtmp \
    --enable-lastlog \
    --enable-unicode3 \
    --enable-combining \
    --enable-xft \
    --enable-font-styles \
    --enable-transparency \
    --enable-fading \
    --enable-rxvt-scroll \
    --enable-next-scroll \
    --enable-xterm-scroll \
    --enable-perl \
    --enable-mousewheel \
    --enable-xim \
    --with-codesets=all \
    --enable-slipwheeling \
    --enable-smart-resize \
    --enable-frills \
    --disable-iso14755 \
    --enable-startup-notification \
    --enable-256-color \
    --with-term=rxvt-unicode-256color
%make_build
%install
%make_install
rm %{buildroot}%{_bindir}/urclock
rm %{buildroot}%{_mandir}/man1/urclock.1*
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications %{SOURCE5}
pushd $RPM_BUILD_ROOT/%{_bindir}
ln -s urxvt rxvt
ln -s urxvt urxvt-ml
ln -s urxvtc urxvt-mlc
ln -s urxvtd urxvt-mld
ln -s urxvt urxvt256c
ln -s urxvtc urxvt256cc
ln -s urxvtd urxvt256cd
ln -s urxvt urxvt256c-ml
ln -s urxvtc urxvt256c-mlc
ln -s urxvtd urxvt256c-mld
popd
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
