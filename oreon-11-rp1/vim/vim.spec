%bcond_with hunspell

%bcond_without flakytests
%bcond_without gui
%bcond_without lua
%bcond_without netbeans
%bcond_without perl
%bcond_without selinux

%if 0%{?fedora}
%bcond_without default_editor
%bcond_without gpm
%bcond_without libsodium_crypt
%else
%bcond_with default_editor
%bcond_with gpm
%bcond_with libsodium_crypt
%endif

%if 0%{?flatpak}
%bcond_with ruby
%else
%bcond_without ruby
%endif

%if %{with gui}
%bcond_without desktop_file
%else
%bcond_with desktop_file
%endif


# VIm upstream wants to build with FORTIFY_SOURCE=1,
# because higher levels causes crashes of valid code constructs
# and their reimplementation would cost unnecessary maintenance
# https://github.com/vim/vim/pull/3507
%define _fortify_level 1

%define baseversion 9.2
# get bug url from /etc/os-release
%define bugurl %(source /etc/os-release; echo ${BUG_REPORT_URL})
%define patchlevel 148
%define vimdir vim92
# Git tags use zero-padded patch (v9.2.0148), archive dir vim-9.2.0148 (same tree as vim.org unix tarball)
%define vim_github_tag v%{baseversion}.%(LANG=C printf '%%04d' %{patchlevel})
%define vim_srcdirname vim-%{baseversion}.%(LANG=C printf '%%04d' %{patchlevel})
%define vim_archive_fname %{vim_srcdirname}.tar.gz

%if %{with desktop_file}
%define desktop_file_utils_version 0.2.93
%endif


Summary: The VIM editor
URL:     https://www.vim.org/
Name: vim
Version: %{baseversion}.%{patchlevel}
Release: 4%{?dist}
Epoch: 2
# swift.vim contains Apache 2.0 with runtime library exception:
# which is taken as Apache-2.0 WITH Swift-exception - reported to legal as https://gitlab.com/fedora/legal/fedora-license-data/-/issues/188
# resolution: the license is good for Fedora, but the file does not have a creativity from 
#
# Open Publication License 1.0 or later for Vim documentation - reported to legal for adding to the allowed licenses list
# response here: https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/message/4UTW5GFDELGMG6K3NQ7NBU42LC2FJOB5/
# resolution: take it as OPUBL-1.0, the license won't be added to allowed license list, but if a project uses it for documentation
# and don't use license options mentioned in the OPUBL 1.0 license text (which both are the case for Vim), the license is allowed
License: Vim AND LGPL-2.1-or-later AND MIT AND GPL-1.0-only AND (GPL-2.0-only OR Vim) AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-or-later AND GPL-3.0-or-later AND OPUBL-1.0 AND Apache-2.0 WITH Swift-exception
# GitHub tag matches vim.org releases (workers that cannot resolve ftp.vim.org still reach github.com)
# #/ forces local name vim-9.2.0148.tar.gz (not v9.2.0148.tar.gz) so %%prep and appstream date match SOURCES
Source0: https://github.com/vim/vim/archive/refs/tags/%{vim_github_tag}.tar.gz#/%{vim_archive_fname}
Source1: virc
Source2: vimrc
Source3: gvim16.png
Source4: gvim32.png
Source5: gvim48.png
Source6: gvim64.png
Source7: spec-template.new
Source8: macros.vim
Source9: vim-default-editor.sh
Source10: vim-default-editor.csh
Source11: vim-default-editor.fish
Source12: view_wrapper
Source13: vim.sh
Source14: vim.fish


Patch1: vim-7.0-fixkeys.patch
Patch2: vim-7.4-specsyntax.patch
Patch3: vim-7.3-manpage-typo-668894-675480.patch
Patch4: vim-manpagefixes-948566.patch
Patch5: vim-7.4-globalsyntax.patch
# migrate shebangs in script to /usr/bin/python3 and use python2 when necessary
Patch6: vim-python3-tests.patch
# fips warning (Fedora downstream patch)
Patch7: vim-crypto-warning.patch
# don't ever set mouse (Fedora downstream patch)
# as result, upstream test suite expects mouse to be set in some tests...
Patch8: vim-9.1-copy-paste.patch
# since F42+, if you let glibc to give you random port, it will give you two random ports
# - one for IPv4 address, another for IPv6 address by default. Vim counts on the port being
# the same, because the fake server used for testing (python script simulating netbeans or
# another language server with language server procotol - LSP) saves the port into a file
# for Vim to pick it up and use the informantion when connecting to the server. However,
# the problem appears when client gets localhost resolved into IPv4 address, but used
# the port which is used by fake server for IPv6 address.
# Since such tests are only mocking the real life behavior and in the real life Vim gets
# connection information by a different way, enforcing IPv4 in the test to prevent mismatch
# is a viable solution.
Patch9: vim-test-port-mismatch.patch

# Patch10000+ - Patches which applied in certain conditions:
# patch only when hunspell is enabled
Patch10000: vim-7.0-hunspell.patch
# remove stopinsert test for clientserver functionality - it sometimes fails in CI
# and sometimes not, which makes it difficult to investigate. Covered in 'flakytests'
# so we can remove it conditionally in CI
Patch10001: vim-9.2-remove-flakytests.patch


# uses autoconf in spec file
BuildRequires: autoconf

# gcc is no longer in buildroot by default
BuildRequires: gcc
# for translations
BuildRequires: gettext

# glibc in F35 bootstraped several conversion formats from
# iconv into a separate package. Vim needs those additional
# formats during compilation.
BuildRequires: glibc-gconv-extra

# for setting ACL on created files
BuildRequires: libacl-devel

# uses libtool for linking
BuildRequires: libtool

# uses make
BuildRequires: make
# screen handling library
BuildRequires: ncurses-devel

# for building function prototypes
BuildRequires: python3
BuildRequires: python3-clang

# for python plugin
BuildRequires: python3-devel


%if %{with desktop_file}
# for /usr/bin/desktop-file-install
BuildRequires: desktop-file-utils >= %{desktop_file_utils_version}
Requires: desktop-file-utils
%endif

%if %{with gpm}
# for mouse support in console
BuildRequires: gpm-devel
%endif

%if %{with hunspell}
BuildRequires: hunspell-devel
%endif

# for xchacha20 encryption
%if %{with libsodium_crypt}
BuildRequires: libsodium-devel
%endif

# for lua plugin
%if %{with lua}
BuildRequires: lua-devel
%endif

# for perl plugin
%if %{with perl}
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::Embed)
BuildRequires: perl(ExtUtils::ParseXS)
%endif

# for ruby plugin
%if %{with ruby}
BuildRequires: ruby
BuildRequires: ruby-devel
%endif

# selinux support
%if %{with selinux}
BuildRequires: libselinux-devel
%endif


%description
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.


%package common
Summary: The common files needed by any version of the VIM editor
# move evim manpage to common - remove the conflict after C11S is branched
Conflicts: %{name}-X11 < 2:9.1.1706-2
# shared files between common and minimal
Requires: %{name}-data = %{epoch}:%{version}-%{release}
Requires: %{name}-filesystem
# the hexdump binary was part of the package for long time, ship it with it
# still for convenience
Requires: xxd

%description common
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.  The
vim-common package contains files which every VIM binary will need in
order to run.

If you are installing vim-enhanced or vim-X11, you'll also need
to install the vim-common package.


%package minimal
Summary: A minimal version of the VIM editor
Provides: vi
Provides: %{_bindir}/vi
# shared files between common and minimal
Requires: %{name}-data = %{epoch}:%{version}-%{release}

%description minimal
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more. The
vim-minimal package includes a minimal version of VIM, providing
the commands vi, view, ex, rvi, and rview. NOTE: The online help is
only available when the vim-common package is installed.


%package enhanced
Summary: A version of the VIM editor which includes recent enhancements
# vim bundles libvterm, which is used during build - so we need to provide
# bundled libvterm for catching possible libvterm CVEs
Provides: bundled(libvterm)
Provides: vim
Provides: vim(plugins-supported)
Provides: %{_bindir}/mergetool
Provides: %{_bindir}/vim
Requires: vim-common = %{epoch}:%{version}-%{release}
# required for vimtutor (#395371)
Requires: which
Suggests: python3
Suggests: python3-libs

# suggest python3, python2, lua, ruby and perl packages because of their 
# embedded functionality in Vim/GVim
%if %{with lua}
Suggests: lua-libs
%endif

%if %{with perl}
Suggests: perl-devel
%endif

%if %{with ruby}
Suggests: ruby
Suggests: ruby-libs
%endif

%description enhanced
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.  The
vim-enhanced package contains a version of VIM with extra, recently
introduced features like Python and Perl interpreters.

Install the vim-enhanced package if you'd like to use a version of the
VIM editor which includes recently added enhancements like
interpreters for the Python and Perl scripting languages.  You'll also
need to install the vim-common package.


%package filesystem
Summary: VIM filesystem layout
BuildArch: noarch

%Description filesystem
This package provides some directories which are required by other
packages that add vim files, p.e.  additional syntax files or filetypes.


%package data
Summary: Shared data for Vi and Vim
BuildArch: noarch

%description data
The subpackage is used for shipping files and directories, which need to be
shared between vim-minimal and vim-common packages.


%package -n xxd
Summary: A hex dump utility

%description -n xxd
xxd creates a hex dump of a given file or standard input.  It can also convert
a hex dump back to its original binary form.


%if %{with default_editor}
%package default-editor
Summary: Set vim as the default editor
BuildArch: noarch
Conflicts: system-default-editor
Provides: system-default-editor
Requires: vim-enhanced

%description default-editor
This subpackage contains files needed to set Vim as the default editor.
%endif

%if %{with gui}
%package X11
Summary: The VIM version of the vi editor for the X Window System - GVim
# move evim manpage to common - remove the conflict after C11S is branched
Conflicts: %{name}-common < 2:9.1.1706-2
# devel of libICE, gtk3, libSM, libX11, libXpm and libXt are needed in buildroot
# so configure script can have correct macros enabled for GUI (#1603272)
# generic gnome toolkit for graphical support
BuildRequires: gtk3-devel
# inter-client exchange library - for X session management protocol
BuildRequires: libICE-devel
# X session management library
BuildRequires: libSM-devel
# core X11 protocol client library
BuildRequires: libX11-devel
# X Toolkit Intrinsics library - working with widgets?
BuildRequires: libXt-devel
# for testing validity of appdata file
BuildRequires: libappstream-glib
# for sound support
BuildRequires: libcanberra-devel

Provides: gvim
Provides: vim(plugins-supported)
Provides: %{_bindir}/mergetool
Provides: %{_bindir}/gvim

# glib2 in Fedora 40 introduced a new function, which is not used in GVim, but it is present
# in compiled gvim binary as symbol when Vim is compiled with glib2-2.79.1
# there does not seem to be a better solution than version based requires on glib2...
# https://bugzilla.redhat.com/show_bug.cgi?id=2262371
Requires: glib2 >= 2.79.1
# GVIM graphics are based on GTK3
Requires: gtk3
# needed for icons (#226526)
Requires: hicolor-icon-theme
# for getting/setting extended attributes - they are pairs (name:value)
# from inodes (files, dirs etc.)
Requires: libattr >= 2.4
Requires: vim-common = %{epoch}:%{version}-%{release} 
Suggests: python3
Suggests: python3-libs

# suggest python3, python2, lua, ruby and perl packages because of their 
# embedded functionality in Vim/GVim
  %if %{with lua}
Suggests: lua-libs
  %endif

  %if %{with perl}
Suggests: perl-devel
  %endif

  %if %{with ruby}
Suggests: ruby
Suggests: ruby-libs
  %endif

%description X11
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and
more. VIM-X11 is a version of the VIM editor which will run within the
X Window System.  If you install this package, you can run VIM as an X
application with a full GUI interface and mouse support by command gvim.

Install the vim-X11 package if you'd like to try out a version of vi
with graphics and mouse capabilities.  You'll also need to install the
vim-common package.
%endif


%prep
%setup -q -b 0 -n %{vim_srcdirname}
# Patches use vim92/ paths like the vim.org unix bundle, not vim-9.2.0148/
cd ..
mv %{vim_srcdirname} %{vimdir}
cd %{vimdir}

# use %%{__python3} macro for defining shebangs in python3 tests
sed -i -e 's,/usr/bin/python3,%{__python3},' %{PATCH6}

# fix rogue dependencies from sample code
chmod -x runtime/tools/mve.awk
%patch -P 1 -p1 -b .fixkeys
%patch -P 2 -p1 -b .spec-syntax

perl -pi -e "s,bin/nawk,bin/awk,g" runtime/tools/mve.awk

%patch -P 3 -p1 -b .mantypo
%patch -P 4 -p1 -b .manpagefixes
%patch -P 5 -p1 -b .globalsyntax
%patch -P 6 -p1 -b .python-tests
%patch -P 7 -p1 -b .fips-warning
%patch -P 8 -p1 -b .copypaste
%patch -P 9 -p1 -b .test-port-mismatch

%if %{with hunspell}
%patch -P 10000 -p1
%endif

%if %{without flakytests}
# there is upstream change in the test, stop removing the test for now
# and see if the error reappears
#%%patch -P 10001 -p1 -b .flakytests
%endif


%build
cd src
autoconf

# added -std=c17 because F42 uses c23 by default and dynamically loaded Ruby plugin fails to build
# with c23 due using `()` for callback arguments to be able to use callbacks with different number
# of arguments in one function
# reported upstream as https://github.com/vim/vim/issues/16575
export CFLAGS="%{optflags} -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -std=c17"
export CXXFLAGS="%{optflags} -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -std=c17"

cp -f os_unix.h os_unix.h.save

# Configure options:
# --enable-fail-if-missing - we need to fail if configure options aren't satisfied
# --with-features - for setting how big amount of features is enabled
# --enable-multibyte - enabling multibyte editing support - for editing files in languages, which one character
#                      cannot be represented by one byte - Asian languages, Unicode
# --disable-netbeans - disabling socket interface for integrating Vim into NetBeans IDE
# --enable-selinux - enabling selinux support
# --enable-Ninterp - enabling internal interpreter, where N can be perl, python3, ruby, lua, tcl
# --with-x - yes if we want X11 support (graphical Vim for X11)
# --with-tlib - which terminal library to use
# --disable-gpm - disabling support for General Purpose Mouse - Linux mouse daemon
# --disable-canberra - disable sounds support
# --enable-year2038 - enable support for timestamps after 2038
# --disable-libsodium - disable additional encryption support
# --without-wayland - without Wayland protocol support
# --enable-fips-warning - shows warning when using Vim encryption, which is not FIPS certified

perl -pi -e "s/vimrc/virc/"  os_unix.h
%configure \
  CFLAGS="${CFLAGS} -DSYS_VIMRC_FILE='\"/etc/virc\"'" \
  --enable-fail-if-missing \
  --enable-fips-warning \
  --enable-gui=no \
  --enable-multibyte \
  --enable-year2038 \
  --exec-prefix=/ \
  --disable-canberra \
  --disable-gpm \
  --disable-libsodium \
  --disable-netbeans \
  --disable-perlinterp \
  --disable-pythoninterp \
  --disable-tclinterp \
  --prefix=%{_prefix} \
  --with-compiledby="%{bugurl}" \
  --with-features=tiny \
  --with-modified-by="%{bugurl}" \
  --with-tlib=ncurses \
  --with-x=no \
  --without-wayland \
%if %{with selinux}
  --enable-selinux
%else
  --disable-selinux
%endif

%make_build
cp vim minimal-vim
make clean


mv -f os_unix.h.save os_unix.h

# --with-python3-stable-abi - python tends to change abi between minor version, but
#                             ensures some abi is kept stable for some time. Use it
#                             to prevent FTBFS that often.
# --enable-cscope - enable support for cscope, tool for browsing C/C++/Java code

%configure \
  CFLAGS="${CFLAGS} -DSYS_VIMRC_FILE='\"/etc/vimrc\"'" \
  --enable-cscope \
  --enable-fail-if-missing \
  --enable-fips-warning \
  --enable-gui=no \
  --enable-multibyte \
  --enable-python3interp=dynamic \
  --enable-year2038 \
  --exec-prefix=%{_prefix} \
  --disable-canberra \
  --disable-tclinterp \
  --prefix=%{_prefix} \
  --with-compiledby="%{bugurl}" \
  --with-features=huge \
  --with-modified-by="%{bugurl}" \
  --with-python3-stable-abi \
  --with-tlib=ncurses \
  --with-x=no \
  --without-wayland \
%if %{with gpm}
  --enable-gpm \
%else
  --disable-gpm \
%endif
%if %{with libsodium_crypt}
  --enable-libsodium \
%else
  --disable-libsodium \
%endif
%if %{with lua}
  --enable-luainterp=dynamic \
%else
  --disable-luainterp \
%endif
%if %{with netbeans}
  --enable-netbeans \
%else
  --disable-netbeans \
%endif
%if %{with perl}
  --enable-perlinterp=dynamic \
  --with-xsubpp=$(which xsubpp) \
%else
  --disable-perlinterp \
%endif
%if %{with ruby}
  --enable-rubyinterp=dynamic \
%else
  --disable-rubyinterp \
%endif
%if %{with selinux}
  --enable-selinux
%else
  --disable-selinux
%endif

%make_build
cp vim enhanced-vim


%if %{with gui}
# More configure options:
# --enable-xim - enabling X Input Method - international input module for X,
#                it is for multibyte languages in Vim with X
# --enable-gtk3-check - checks for GTK3
# --enable-socketserver - using unix domain socket for inter-Vim processes communication

%configure \
  CFLAGS="${CFLAGS} -DSYS_VIMRC_FILE='\"/etc/vimrc\"'" \
  --enable-canberra \
  --enable-cscope \
  --enable-fail-if-missing \
  --enable-fips-warning \
  --enable-gtk3-check \
  --enable-gui=gtk3 \
  --enable-multibyte \
  --enable-python3interp=dynamic \
  --enable-socketserver \
  --enable-xim \
  --enable-year2038 \
  --disable-tclinterp \
  --with-compiledby="%{bugurl}" \
  --with-features=huge \
  --with-modified-by="%{bugurl}" \
  --with-python3-stable-abi \
  --with-tlib=ncurses \
  --with-wayland \
  --with-x=yes \
  %if %{with gpm}
  --enable-gpm \
  %else
  --disable-gpm \
  %endif
  %if %{with libsodium_crypt}
  --enable-libsodium \
  %else
  --disable-libsodium \
  %endif
  %if %{with lua}
  --enable-luainterp=dynamic \
  %else
  --disable-luainterp \
  %endif
  %if %{with netbeans}
  --enable-netbeans \
  %else
  --disable-netbeans \
  %endif
  %if %{with perl}
  --enable-perlinterp=dynamic \
  --with-xsubpp=$(which xsubpp) \
  %else
  --disable-perlinterp \
  %endif
  %if %{with ruby}
  --enable-rubyinterp=dynamic \
  %else
  --disable-rubyinterp \
  %endif
  %if %{with selinux}
  --enable-selinux
  %else
  --disable-selinux
  %endif

%make_build
cp vim gvim
make clean
%endif


%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/%{name}/vimfiles/{after,autoload,colors,compiler,doc,ftdetect,ftplugin,indent,keymap,lang,plugin,print,spell,syntax,tutor}
mkdir -p %{buildroot}/%{_datadir}/%{name}/vimfiles/after/{autoload,colors,compiler,doc,ftdetect,ftplugin,indent,keymap,lang,plugin,print,spell,syntax,tutor}
cp -f %{SOURCE7} %{buildroot}/%{_datadir}/%{name}/vimfiles/template.spec
# Those aren't Linux info files but some binary files for Amiga:
rm -f README*.info

cd src
# related to the issue with `make depend`, auto/osdef.h
# has to be generated
make auto/osdef.h auto/gui_gtk_gresources.h auto/wayland/wlr-data-control-unstable-v1.h
# Adding STRIP=/bin/true, because Vim wants to strip the binaries by himself
# and put the stripped files into correct dirs. Build system (koji/brew) 
# does it for us, so there is no need to do it in Vim
%make_install BINDIR=%{_bindir} STRIP=/bin/true

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{16x16,32x32,48x48,64x64}/apps
install -m755 minimal-vim %{buildroot}%{_bindir}/vi
install -m755 enhanced-vim %{buildroot}%{_bindir}/vim
install -m755 %{SOURCE12} %{buildroot}%{_bindir}/view

%if %{with gui}
make installgtutorbin  DESTDIR=%{buildroot} BINDIR=%{_bindir}
install -m755 gvim %{buildroot}%{_bindir}/gvim
install -p -m644 %{SOURCE3} \
   %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/gvim.png
install -p -m644 %{SOURCE4} \
   %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/gvim.png
install -p -m644 %{SOURCE5} \
   %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/gvim.png
install -p -m644 %{SOURCE6} \
   %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/gvim.png

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p %{buildroot}%{_datadir}/metainfo
cat > %{buildroot}%{_datadir}/metainfo/gvim.appdata.xml <<"EOF"
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
EmailAddress: Bram@moolenaar.net>
SentUpstream: 2014-05-22
-->
<component type="desktop-application">
  <id>org.vim.Vim</id>
  <name>GVim</name>
  <metadata_license>CC0-1.0</metadata_license>
  <project_license>Vim</project_license>
  <summary>The VIM version of the vi editor for the X Window System</summary>
  <description>
    <p>
     Vim is an advanced text editor that seeks to provide the power of the
     de-facto Unix editor 'Vi', with a more complete feature set.
     It's useful whether you're already using vi or using a different editor.
    </p>
    <p>
     Vim is a highly configurable text editor built to enable efficient text
     editing.
     Vim is often called a "programmer's editor," and so useful for programming
     that many consider it an entire IDE. It is not just for programmers, though.
     Vim is perfect for all kinds of text editing, from composing email to
     editing configuration files.
    </p>
    <p>
     We ship the current Vim stable release - %{baseversion} - with the upstream
     patchlevel %{patchlevel} applied, which is combined into version %{version}
     used during packaging.
    </p>
  </description>
  <releases>
    <release version="%{version}" date="%(date +%F)" />
  </releases>
  <screenshots>
    <screenshot type="default">
      <image>https://raw.githubusercontent.com/zdohnal/vim/zdohnal-screenshot/gvim16_9.png</image>
    </screenshot>
  </screenshots>
  <url type="homepage">http://www.vim.org/</url>
  <content_rating type="oars-1.1"/>
  <!--
    Without this tag, the G-S does not display icon properly. But also the
    `appstream-builder` inserts into metadata generic
    `<launchable type="desktop-id">org.vim.Vim.desktop</launchable>`,
    which cannot be found. This results in `Vetos: Has no Icon` and
    therefore rejection of GVim from `appstream-data` package.
  -->
  <launchable type="desktop-id">gvim.desktop</launchable>
</component>
EOF

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml

# do not put gvim.1, gview.1, eview.1, rgvim and rgview here - they already contains the link,
# and changing it here will rewrite original vim.1 - bz#2392178
for i in gex.1 vimx.1 evim.1; do
  echo ".so man1/vim.1" > %{buildroot}/%{_mandir}/man1/$i
done

echo ".so man1/vimtutor.1" > %{buildroot}/%{_mandir}/man1/gvimtutor.1
%else
# Remove files included in X11 subpackage, but built by default:
rm %{buildroot}/%{_mandir}/man1/evim.*
rm %{buildroot}/%{_datadir}/applications/{vim,gvim}.desktop
rm %{buildroot}/%{_datadir}/icons/{hicolor,locolor}/*/apps/gvim.png
%endif

( cd %{buildroot}
  ln -sf ../..%{_bindir}/vi .%{_bindir}/rvi
  ln -sf ../..%{_bindir}/vi .%{_bindir}/rview
  ln -sf ../..%{_bindir}/vi .%{_bindir}/ex
  ln -sf vim .%{_bindir}/rvim
  ln -sf vim .%{_bindir}/vimdiff
  perl -pi -e "s,%{buildroot},," .%{_mandir}/man1/vim.1 .%{_mandir}/man1/vimtutor.1
  rm -f .%{_mandir}/man1/rvim.1
  cp -p .%{_mandir}/man1/vim.1 .%{_mandir}/man1/vi.1
  ln -sf vi.1.gz .%{_mandir}/man1/rvi.1.gz
  ln -sf vi.1.gz .%{_mandir}/man1/ex.1
  ln -sf vi.1.gz .%{_mandir}/man1/view.1
  ln -sf vi.1.gz .%{_mandir}/man1/rview.1
  ln -sf vim.1.gz .%{_mandir}/man1/vimdiff.1.gz

%if %{with gui}
  ln -sf gvim ./%{_bindir}/evim
  ln -sf gvim ./%{_bindir}/eview
  ln -sf gvim ./%{_bindir}/gview
  ln -sf gvim ./%{_bindir}/gex
  ln -sf gvim ./%{_bindir}/gvimdiff
  ln -sf gvim ./%{_bindir}/rgvim
  ln -sf gvim ./%{_bindir}/rgview
  ln -sf gvim ./%{_bindir}/vimx

  %if %{with desktop_file}
    desktop-file-install \
        --dir %{buildroot}/%{_datadir}/applications \
        %{buildroot}/%{_datadir}/applications/gvim.desktop
        # --add-category "Development;TextEditor;X-Red-Hat-Base" D\
  %else
    mkdir -p ./%{_sysconfdir}/X11/applnk/Applications
    cp %{buildroot}/%{_datadir}/applications/gvim.desktop ./%{_sysconfdir}/X11/applnk/Applications/gvim.desktop
  %endif

%endif

  # ja_JP.ujis is obsolete, ja_JP.eucJP is recommended.
  ( cd ./%{_datadir}/%{name}/%{vimdir}/lang; \
    ln -sf menu_ja_jp.ujis.vim menu_ja_jp.eucjp.vim )
)

# Dependency cleanups
chmod 644 %{buildroot}/%{_datadir}/%{name}/%{vimdir}/doc/vim2html.pl \
 %{buildroot}/%{_datadir}/%{name}/%{vimdir}/tools/*.pl \
 %{buildroot}/%{_datadir}/%{name}/%{vimdir}/tools/vim132
chmod 644 ../runtime/doc/vim2html.pl

mkdir -p %{buildroot}%{_sysconfdir}
install -p -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/virc
install -p -m644 %{SOURCE2} %{buildroot}%{_sysconfdir}/vimrc

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d/
install -p -m644 %{SOURCE8} %{buildroot}%{_rpmconfigdir}/macros.d/

(cd ../runtime; rm -rf doc; ln -svf ../../vim/%{vimdir}/doc docs;) 
rm -f %{buildroot}/%{_datadir}/vim/%{vimdir}/macros/maze/maze*.c
rm -rf %{buildroot}/%{_datadir}/vim/%{vimdir}/tools
rm -rf %{buildroot}/%{_datadir}/vim/%{vimdir}/doc/vim2html.pl
rm -f %{buildroot}/%{_datadir}/vim/%{vimdir}/tutor/tutor.gr.utf-8~

# Remove not UTF-8 manpages
for i in pl.ISO8859-2 it.ISO8859-1 ru.KOI8-R fr.ISO8859-1 da.ISO8859-1 de.ISO8859-1 tr.ISO8859-9 sv.ISO8859-1; do
  rm -rf %{buildroot}/%{_mandir}/$i
done

# use common man1/ru directory
mv %{buildroot}/%{_mandir}/ru.UTF-8 %{buildroot}/%{_mandir}/ru

# Remove duplicate man pages
for i in fr.UTF-8 it.UTF-8 pl.UTF-8 da.UTF-8 de.UTF-8 tr.UTF-8 sv.UTF-8; do
  rm -rf %{buildroot}/%{_mandir}/$i
done

# Install symlink for rvim man page
echo ".so man1/vim.1" > %{buildroot}/%{_mandir}/man1/rvim.1

mkdir -p %{buildroot}/%{_mandir}/man5
echo ".so man1/vim.1" > %{buildroot}/%{_mandir}/man5/vimrc.5
echo ".so man1/vi.1" > %{buildroot}/%{_mandir}/man5/virc.5
touch %{buildroot}/%{_datadir}/%{name}/vimfiles/doc/tags

# upstream now tries to install LICENSE and README into VIMDIR
# but we ship them in licensedir and docdir, so we remove the dupes
# from VIMDIR
rm %{buildroot}%{_datadir}/%{name}/%{vimdir}/LICENSE
rm %{buildroot}%{_datadir}/%{name}/%{vimdir}/README.txt

# if Vim isn't built for Fedora, use redhat augroup
%if 0%{?rhel} >= 7
sed -i -e "s/augroup fedora/augroup redhat/" %{buildroot}/%{_sysconfdir}/vimrc
sed -i -e "s/augroup fedora/augroup redhat/" %{buildroot}/%{_sysconfdir}/virc
%endif

# adding vi->vim aliases per rhbz#2439657 for bash, ksh, zsh and fish
# it won't work without bash reload and under sudo, but reporter was aware
mkdir -p %{buildroot}/%{_sysconfdir}/profile.d
install -p -m644 %{SOURCE13} %{buildroot}/%{_sysconfdir}/profile.d/vim.sh

mkdir -p %{buildroot}/%{_datadir}/fish/vendor_functions.d/
install -p -m644 %{SOURCE14} %{buildroot}/%{_datadir}/fish/vendor_functions.d/vim.fish

%if %{with default_editor}
install -p -m644 %{SOURCE9} %{buildroot}/%{_sysconfdir}/profile.d/vim-default-editor.sh
install -p -m644 %{SOURCE10} %{buildroot}/%{_sysconfdir}/profile.d/vim-default-editor.csh

mkdir -p %{buildroot}/%{_datadir}/fish/vendor_conf.d/
install -p -m644 %{SOURCE11} %{buildroot}/%{_datadir}/fish/vendor_conf.d/vim-default-editor.fish
%endif


# Refresh documentation helptags
%transfiletriggerin common -- %{_datadir}/%{name}/vimfiles/doc
%{_bindir}/vim -c ":helptags %{_datadir}/%{name}/vimfiles/doc" -c :q &> /dev/null || :

%transfiletriggerpostun common -- %{_datadir}/%{name}/vimfiles/doc
> %{_datadir}/%{name}/vimfiles/doc/tags || :
%{_bindir}/vim -c ":helptags %{_datadir}/%{name}/vimfiles/doc" -c :q &> /dev/null || :

%files common
%config(noreplace) %{_sysconfdir}/vimrc
%{!?_licensedir:%global license %%doc}
%doc README*
%doc runtime/docs
%{_datadir}/%{name}/%{vimdir}/autoload
%{_datadir}/%{name}/%{vimdir}/colors
%{_datadir}/%{name}/%{vimdir}/compiler
%{_datadir}/%{name}/%{vimdir}/pack
%{_datadir}/%{name}/%{vimdir}/doc
%{_datadir}/%{name}/%{vimdir}/*.vim
%exclude %{_datadir}/%{name}/%{vimdir}/defaults.vim
%{_datadir}/%{name}/%{vimdir}/ftplugin
%{_datadir}/%{name}/%{vimdir}/import/dist/vimhelp.vim
%{_datadir}/%{name}/%{vimdir}/import/dist/vimhighlight.vim
%{_datadir}/%{name}/%{vimdir}/indent
%{_datadir}/%{name}/%{vimdir}/keymap
%{_datadir}/%{name}/%{vimdir}/lang/*.vim
%{_datadir}/%{name}/%{vimdir}/lang/*.txt
%dir %{_datadir}/%{name}/%{vimdir}/lang
%{_datadir}/%{name}/%{vimdir}/macros
%{_datadir}/%{name}/%{vimdir}/plugin
%{_datadir}/%{name}/%{vimdir}/print
%{_datadir}/%{name}/%{vimdir}/syntax
%{_datadir}/%{name}/%{vimdir}/tutor
%{_datadir}/%{name}/%{vimdir}/spell
%lang(af) %{_datadir}/%{name}/%{vimdir}/lang/af
%lang(ca) %{_datadir}/%{name}/%{vimdir}/lang/ca
%lang(cs) %{_datadir}/%{name}/%{vimdir}/lang/cs
%lang(cs.cp1250) %{_datadir}/%{name}/%{vimdir}/lang/cs.cp1250
%lang(da) %{_datadir}/%{name}/%{vimdir}/lang/da
%lang(de) %{_datadir}/%{name}/%{vimdir}/lang/de
%lang(en_GB) %{_datadir}/%{name}/%{vimdir}/lang/en_GB
%lang(eo) %{_datadir}/%{name}/%{vimdir}/lang/eo
%lang(es) %{_datadir}/%{name}/%{vimdir}/lang/es
%lang(fi) %{_datadir}/%{name}/%{vimdir}/lang/fi
%lang(fr) %{_datadir}/%{name}/%{vimdir}/lang/fr
%lang(ga) %{_datadir}/%{name}/%{vimdir}/lang/ga
%lang(hu) %{_datadir}/%{name}/%{vimdir}/lang/hu
%lang(hy) %{_datadir}/%{name}/%{vimdir}/lang/hy
%lang(it) %{_datadir}/%{name}/%{vimdir}/lang/it
%lang(ja) %{_datadir}/%{name}/%{vimdir}/lang/ja
%lang(ja.euc-jp) %{_datadir}/%{name}/%{vimdir}/lang/ja.euc-jp
%lang(ja.sjis) %{_datadir}/%{name}/%{vimdir}/lang/ja.sjis
%lang(ko) %{_datadir}/%{name}/%{vimdir}/lang/ko
%lang(ko) %{_datadir}/%{name}/%{vimdir}/lang/ko.UTF-8
%lang(lv) %{_datadir}/%{name}/%{vimdir}/lang/lv
%lang(nb) %{_datadir}/%{name}/%{vimdir}/lang/nb
%lang(nl) %{_datadir}/%{name}/%{vimdir}/lang/nl
%lang(no) %{_datadir}/%{name}/%{vimdir}/lang/no
%lang(pl) %{_datadir}/%{name}/%{vimdir}/lang/pl
%lang(pl.UTF-8) %{_datadir}/%{name}/%{vimdir}/lang/pl.UTF-8
%lang(pl.cp1250) %{_datadir}/%{name}/%{vimdir}/lang/pl.cp1250
%lang(pt_BR) %{_datadir}/%{name}/%{vimdir}/lang/pt_BR
%lang(ru) %{_datadir}/%{name}/%{vimdir}/lang/ru
%lang(ru.cp1251) %{_datadir}/%{name}/%{vimdir}/lang/ru.cp1251
%lang(sk) %{_datadir}/%{name}/%{vimdir}/lang/sk
%lang(sk.cp1250) %{_datadir}/%{name}/%{vimdir}/lang/sk.cp1250
%lang(sr) %{_datadir}/%{name}/%{vimdir}/lang/sr
%lang(sv) %{_datadir}/%{name}/%{vimdir}/lang/sv
%lang(ta) %{_datadir}/%{name}/%{vimdir}/lang/ta
%lang(tr) %{_datadir}/%{name}/%{vimdir}/lang/tr
%lang(uk) %{_datadir}/%{name}/%{vimdir}/lang/uk
%lang(uk.cp1251) %{_datadir}/%{name}/%{vimdir}/lang/uk.cp1251
%lang(vi) %{_datadir}/%{name}/%{vimdir}/lang/vi
%lang(zh_CN) %{_datadir}/%{name}/%{vimdir}/lang/zh_CN
%lang(zh_CN.cp936) %{_datadir}/%{name}/%{vimdir}/lang/zh_CN.cp936
%lang(zh_TW) %{_datadir}/%{name}/%{vimdir}/lang/zh_TW
%lang(zh_CN.UTF-8) %{_datadir}/%{name}/%{vimdir}/lang/zh_CN.UTF-8
%lang(zh_TW.UTF-8) %{_datadir}/%{name}/%{vimdir}/lang/zh_TW.UTF-8
%{_mandir}/man1/rvim.*
%{_mandir}/man1/vim.*
%{_mandir}/man1/vimdiff.*
%{_mandir}/man1/vimtutor.*
%{_mandir}/man5/vimrc.*

%if %{with gui}
%{_mandir}/man1/eview.*
%{_mandir}/man1/evim.*
%{_mandir}/man1/gex.*
%{_mandir}/man1/gview.*
%{_mandir}/man1/gvim*
%{_mandir}/man1/rgvim.*
%{_mandir}/man1/rgview.*
%{_mandir}/man1/vimx.*
%endif

%lang(fr) %{_mandir}/fr/man1/*
%lang(da) %{_mandir}/da/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(ru) %{_mandir}/ru/man1/*
%lang(sv) %{_mandir}/sv/man1/*
%lang(tr) %{_mandir}/tr/man1/*

%files minimal
%config(noreplace) %{_sysconfdir}/virc
%{_bindir}/ex
%{_bindir}/rvi
%{_bindir}/rview
%{_bindir}/vi
%{_bindir}/view
%{_mandir}/man1/vi.*
%{_mandir}/man1/ex.*
%{_mandir}/man1/rvi.*
%{_mandir}/man1/rview.*
%{_mandir}/man1/view.*
%{_mandir}/man5/virc.*

%files enhanced
%{_bindir}/rvim
%{_bindir}/vim
%{_bindir}/vimdiff
%{_bindir}/vimtutor
%dir %{_datadir}/fish/vendor_functions.d/
%{_datadir}/fish/vendor_functions.d/vim.fish
%config(noreplace) %{_sysconfdir}/profile.d/vim.sh

%files filesystem
%{_rpmconfigdir}/macros.d/macros.vim
%dir %{_datadir}/%{name}/vimfiles/after
%dir %{_datadir}/%{name}/vimfiles/after/*
%dir %{_datadir}/%{name}/vimfiles/autoload
%dir %{_datadir}/%{name}/vimfiles/colors
%dir %{_datadir}/%{name}/vimfiles/compiler
%dir %{_datadir}/%{name}/vimfiles/doc
%ghost %{_datadir}/%{name}/vimfiles/doc/tags
%dir %{_datadir}/%{name}/vimfiles/ftdetect
%dir %{_datadir}/%{name}/vimfiles/ftplugin
%dir %{_datadir}/%{name}/%{vimdir}/import
%dir %{_datadir}/%{name}/%{vimdir}/import/dist
%dir %{_datadir}/%{name}/vimfiles/indent
%dir %{_datadir}/%{name}/vimfiles/keymap
%dir %{_datadir}/%{name}/vimfiles/lang
%dir %{_datadir}/%{name}/vimfiles/plugin
%dir %{_datadir}/%{name}/vimfiles/print
%dir %{_datadir}/%{name}/vimfiles/spell
%dir %{_datadir}/%{name}/vimfiles/syntax
%dir %{_datadir}/%{name}/vimfiles/tutor
%dir %{_sysconfdir}/profile.d

%if %{with gui}
%files X11
  %if %{with desktop_file}
%{_datadir}/metainfo/*.appdata.xml
/%{_datadir}/applications/*
%exclude /%{_datadir}/applications/vim.desktop
  %else
/%{_sysconfdir}/X11/applnk/*/gvim.desktop
  %endif
%{_bindir}/gvimtutor
%{_bindir}/gvim
%{_bindir}/gvimdiff
%{_bindir}/gview
%{_bindir}/gex
%{_bindir}/vimtutor
%{_bindir}/vimx
%{_bindir}/evim
%{_bindir}/eview
%{_bindir}/rgvim
%{_bindir}/rgview
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps
%{_datadir}/icons/hicolor/*/apps/*
%dir %{_datadir}/icons/locolor
%dir %{_datadir}/icons/locolor/*
%dir %{_datadir}/icons/locolor/*/apps
%{_datadir}/icons/locolor/*/apps/*
%endif

%files data
%license LICENSE
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{vimdir}
%{_datadir}/%{name}/%{vimdir}/defaults.vim
%dir %{_datadir}/%{name}/vimfiles
%{_datadir}/%{name}/vimfiles/template.spec

%if %{with default_editor}
%files default-editor
%dir %{_datadir}/fish/vendor_conf.d
%{_datadir}/fish/vendor_conf.d/vim-default-editor.fish
%config(noreplace) %{_sysconfdir}/profile.d/vim-default-editor.*
%endif

%files -n xxd
%license LICENSE
%{_bindir}/xxd
%{_mandir}/man1/xxd.*


%changelog
* Mon Apr 13 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.2.148-4
- Source0 from GitHub tag v9.2.0148 (ftp.vim.org DNS failed on worker), prep unpacks vim-9.2.0148 like unix tarball

* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.2.148-3
- Source0 from ftp.vim.org (NLUUG 404 on vim-9.2-148)

* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.2.148-2
- Source0 from NLUUG HTTPS mirror (spectool has no ftp)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.2.148-1
- Prepare for Oreon 11 (RP1)
