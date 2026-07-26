%global source0_hash aaa13fcbc149fe0f3f391f933279580f74a96fd312d6ed06b8ff03c2d46672e8

Name:           rxvt-unicode
Version:        9.31
Release:        15%{?dist}
Summary:        Unicode version of rxvt

License:        GPL-3.0-or-later
URL:            http://software.schmorp.de/pkg/rxvt-unicode.html
Source0:        http://dist.schmorp.de/%{name}/%{name}-%{version}.tar.bz2
Source1:        http://dist.schmorp.de/%{name}/%{name}-%{version}.tar.bz2.sig
Source2:        http://dist.schmorp.de/signing-key.pub
Source3:        http://dist.schmorp.de/signing-key.pub.gpg.sig
Source4:        gpgkey-84874CAB6D1A397A.gpg
Source5:        rxvt-unicode.desktop
# To recreate Source4:
#     gpg --recv-key 84874CAB6D1A397A
#     gpg --export --export-options export-minimal 84874CAB6D1A397A \
#         > gpgkey-84874CAB6D1A397A.gpg

Patch0:         rxvt-unicode-9.21-Fix-hard-coded-wrong-path-to-xsubpp.patch
Patch1:         rxvt-unicode-0001-Prefer-XDG_RUNTIME_DIR-over-the-HOME.patch
# Backport of https://github.com/exg/rxvt-unicode/commit/417b540d6dba67d440e3617bc2cf6d7cea1ed968
Patch2:         Fix-OSC-responses-with-7-bit-ST.patch

BuildRequires:  desktop-file-utils
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  gnupg2
BuildRequires:  libptytty-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXt-devel
BuildRequires:  libev-source
BuildRequires:  make
BuildRequires:  ncurses ncurses-base ncurses-devel
BuildRequires:  perl-devel, perl-generators, perl(ExtUtils::Embed)
BuildRequires:  signify
BuildRequires:  startup-notification-devel
BuildRequires:  xorg-x11-proto-devel
Requires:       startup-notification

# We just provide a single binary now.
Obsoletes:      rxvt-unicode-ml <= 9.22-17
Obsoletes:      rxvt-unicode-256color <= 9.22-17
Obsoletes:      rxvt-unicode-256color-ml <= 9.22-17

# There's only one rxvt in the distro; this is the last one
Obsoletes:      rxvt <= 2.7.10-36

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

%if 0%{?fedora} >= 15
rm -rf libev
ln -s %{_datadir}/libev-source libev
%endif

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
%if 0%{?fedora} > 13
    --enable-pixbuf \
%endif
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

# This isn't something we need
rm %{buildroot}%{_bindir}/urclock
rm %{buildroot}%{_mandir}/man1/urclock.1*

# install desktop files
desktop-file-install \
%if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
    --vendor=fedora \
%endif
    --dir=%{buildroot}%{_datadir}/applications %{SOURCE5}

# create compat symlinks
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

%files
%doc README.FAQ
%doc INSTALL
%doc doc/README.xvt
%doc doc/etc
%doc doc/changes.txt
%license COPYING
%{_bindir}/rxvt
%{_bindir}/urxvt
%{_bindir}/urxvtc
%{_bindir}/urxvtd
%{_bindir}/urxvt-ml
%{_bindir}/urxvt-mlc
%{_bindir}/urxvt-mld
%{_bindir}/urxvt256c
%{_bindir}/urxvt256cc
%{_bindir}/urxvt256cd
%{_bindir}/urxvt256c-ml
%{_bindir}/urxvt256c-mlc
%{_bindir}/urxvt256c-mld
%{_mandir}/man1/urxvt.1*
%{_mandir}/man1/urxvtc.1*
%{_mandir}/man1/urxvtd.1*
%{_mandir}/man1/urxvt-background.1*
%{_mandir}/man1/urxvt-bell-command.1*
%{_mandir}/man1/urxvt-block-graphics-to-ascii.1*
%{_mandir}/man1/urxvt-clipboard-osc.1*
%{_mandir}/man1/urxvt-clickthrough.1*
%{_mandir}/man1/urxvt-confirm-paste.1*
%{_mandir}/man1/urxvt-digital-clock.1*
%{_mandir}/man1/urxvt-eval.1*
%{_mandir}/man1/urxvt-example-refresh-hooks.1*
%{_mandir}/man1/urxvt-extensions.1*
%{_mandir}/man1/urxvt-keysym-list.1*
%{_mandir}/man1/urxvt-kuake.1*
%{_mandir}/man1/urxvt-matcher.1*
%{_mandir}/man1/urxvt-option-popup.1*
%{_mandir}/man1/urxvt-overlay-osc.1*
%{_mandir}/man1/urxvt-readline.1*
%{_mandir}/man1/urxvt-remote-clipboard.1*
%{_mandir}/man1/urxvt-searchable-scrollback.1*
%{_mandir}/man1/urxvt-selection-autotransform.1*
%{_mandir}/man1/urxvt-selection-pastebin.1*
%{_mandir}/man1/urxvt-selection-popup.1*
%{_mandir}/man1/urxvt-selection-to-clipboard.1*
%{_mandir}/man1/urxvt-selection.1*
%{_mandir}/man1/urxvt-tabbed.1*
%{_mandir}/man1/urxvt-xim-onthespot.1*
%{_mandir}/man3/urxvtperl.3*
%{_mandir}/man7/urxvt.7*
%{_datadir}/applications/*rxvt-unicode.desktop
%{_libdir}/urxvt

%changelog
%autochangelog
