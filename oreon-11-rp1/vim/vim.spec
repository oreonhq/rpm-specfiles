%global source0_hash a841d9490f573cf2696e157aade3568d327fc59374b7627f374dae3a600a5e0a
%bcond_with hunspell
%bcond_without flakytests
%bcond_without gui
%bcond_without lua
%bcond_without netbeans
%bcond_without perl
%bcond_without selinux
%bcond_with default_editor
%bcond_with gpm
%bcond_with libsodium_crypt
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
%define _fortify_level 1
%define baseversion 9.2
%define bugurl %(source /etc/os-release; echo ${BUG_REPORT_URL})
%define patchlevel 1162
%define vimdir vim92
%define vim_github_tag v%{baseversion}.%(LANG=C printf '%%04d' %{patchlevel})
%define vim_srcdirname vim-%{baseversion}.%(LANG=C printf '%%04d' %{patchlevel})
%define vim_archive_fname %{vim_srcdirname}.tar.gz
%if %{with desktop_file}
%define desktop_file_utils_version 0.2.93
%endif
Summary:        The VIM editor
URL:     https://www.vim.org/
Name: vim
Version: %{baseversion}.%{patchlevel}
Release:        1%{?dist}
Epoch: 2
License: Vim AND LGPL-2.1-or-later AND MIT AND GPL-1.0-only AND (GPL-2.0-only OR Vim) AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-or-later AND GPL-3.0-or-later AND OPUBL-1.0 AND Apache-2.0 WITH Swift-exception
Source0:        https://github.com/%{name}/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.bz2
Source1:        virc
Source2:        vimrc
Source3:        gvim16.png
Source4:        gvim32.png
Source5:        gvim48.png
Source6:        gvim64.png
Source7:        spec-template.new
Source8:        macros.vim
Source9:        vim-default-editor.sh
Source10:        vim-default-editor.csh
Source11:        vim-default-editor.fish
Source12:        view_wrapper
Source13:        vim.sh
Source14:        vim.fish
Patch1: vim-7.0-fixkeys.patch
Patch2: vim-7.4-specsyntax.patch
Patch3: vim-7.3-manpage-typo-668894-675480.patch
Patch4: vim-manpagefixes-948566.patch
Patch5: vim-7.4-globalsyntax.patch
Patch6: vim-python3-tests.patch
Patch7: vim-crypto-warning.patch
Patch8: vim-9.1-copy-paste.patch
Patch9: vim-test-port-mismatch.patch
Patch10000: vim-7.0-hunspell.patch
Patch10001: vim-9.2-remove-flakytests.patch
%if %{with desktop_file}
Requires: desktop-file-utils
%endif
%if %{with gpm}
%endif
%if %{with hunspell}
%endif
%if %{with libsodium_crypt}
%endif
%if %{with lua}
%endif
%if %{with perl}
%endif
%if %{with ruby}
%endif
%if %{with selinux}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glibc-gconv-extra
BuildRequires:  gpm-devel
BuildRequires:  gtk3-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  libacl-devel
BuildRequires:  libappstream-glib
BuildRequires:  libcanberra-devel
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  python3
BuildRequires:  python3-clang
BuildRequires:  python3-devel
BuildRequires:  ruby
BuildRequires:  ruby-devel
# /oreon:deps
%description
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.

%package common
Summary: The common files needed by any version of the VIM editor
Conflicts: %{name}-X11 < 2:9.1.1706-2
Requires: %{name}-data = %{epoch}:%{version}-%{release}
Requires: %{name}-filesystem
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
Provides: bundled(libvterm)
Provides: vim
Provides: vim(plugins-supported)
Provides: %{_bindir}/mergetool
Provides: %{_bindir}/vim
Requires: vim-common = %{epoch}:%{version}-%{release}
Requires: which
Suggests: python3
Suggests: python3-libs
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
Conflicts: %{name}-common < 2:9.1.1706-2
BuildRequires: gtk3-devel
BuildRequires: libICE-devel
BuildRequires: libSM-devel
BuildRequires: libX11-devel
BuildRequires: libXt-devel
BuildRequires: libappstream-glib
BuildRequires: libcanberra-devel
Provides: gvim
Provides: vim(plugins-supported)
Provides: %{_bindir}/mergetool
Provides: %{_bindir}/gvim
Requires: glib2 >= 2.79.1
Requires: gtk3
Requires: hicolor-icon-theme
Requires: libattr >= 2.4
Requires: vim-common = %{epoch}:%{version}-%{release} 
Suggests: python3
Suggests: python3-libs
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -b 0 -n %{vim_srcdirname}
# Patches use vim92/ paths like the vim.org unix bundle, not vim-9.2.0148/
# %%setup -n %%{vim_srcdirname} makes %%build auto-cd into that name, so keep a symlink after rename
cd ..
mv %{vim_srcdirname} %{vimdir}
ln -sfn %{vimdir} %{vim_srcdirname}
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
export CFLAGS="%{optflags} -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -std=c17"
export CXXFLAGS="%{optflags} -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -std=c17"
cp -f os_unix.h os_unix.h.save
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
rm -f README*.info
cd src
make auto/osdef.h auto/gui_gtk_gresources.h auto/wayland/wlr-data-control-unstable-v1.h
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
for i in gex.1 vimx.1 evim.1; do
  echo ".so man1/vim.1" > %{buildroot}/%{_mandir}/man1/$i
done
echo ".so man1/vimtutor.1" > %{buildroot}/%{_mandir}/man1/gvimtutor.1
%else
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
  %else
    mkdir -p ./%{_sysconfdir}/X11/applnk/Applications
    cp %{buildroot}/%{_datadir}/applications/gvim.desktop ./%{_sysconfdir}/X11/applnk/Applications/gvim.desktop
  %endif
%endif
  ( cd ./%{_datadir}/%{name}/%{vimdir}/lang; \
    ln -sf menu_ja_jp.ujis.vim menu_ja_jp.eucjp.vim )
)
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
for i in pl.ISO8859-2 it.ISO8859-1 ru.KOI8-R fr.ISO8859-1 da.ISO8859-1 de.ISO8859-1 tr.ISO8859-9 sv.ISO8859-1; do
  rm -rf %{buildroot}/%{_mandir}/$i
done
mv %{buildroot}/%{_mandir}/ru.UTF-8 %{buildroot}/%{_mandir}/ru
for i in fr.UTF-8 it.UTF-8 pl.UTF-8 da.UTF-8 de.UTF-8 tr.UTF-8 sv.UTF-8; do
  rm -rf %{buildroot}/%{_mandir}/$i
done
echo ".so man1/vim.1" > %{buildroot}/%{_mandir}/man1/rvim.1
mkdir -p %{buildroot}/%{_mandir}/man5
echo ".so man1/vim.1" > %{buildroot}/%{_mandir}/man5/vimrc.5
echo ".so man1/vi.1" > %{buildroot}/%{_mandir}/man5/virc.5
touch %{buildroot}/%{_datadir}/%{name}/vimfiles/doc/tags
rm %{buildroot}%{_datadir}/%{name}/%{vimdir}/LICENSE
rm %{buildroot}%{_datadir}/%{name}/%{vimdir}/README.txt
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
%transfiletriggerin common -- %{_datadir}/%{name}/vimfiles/doc
%{_bindir}/vim -c ":helptags %{_datadir}/%{name}/vimfiles/doc" -c :q &> /dev/null || :
%transfiletriggerpostun common -- %{_datadir}/%{name}/vimfiles/doc
> %{_datadir}/%{name}/vimfiles/doc/tags || :
%{_bindir}/vim -c ":helptags %{_datadir}/%{name}/vimfiles/doc" -c :q &> /dev/null || :
%oreon_autofiles xxd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n vim-common -f %{oreon_filedir}/vim-common.list
%files -n vim-minimal -f %{oreon_filedir}/vim-minimal.list
%files -n vim-enhanced -f %{oreon_filedir}/vim-enhanced.list
%files -n vim-filesystem -f %{oreon_filedir}/vim-filesystem.list
%files -n vim-data -f %{oreon_filedir}/vim-data.list
%files -n xxd -f %{oreon_filedir}/xxd.list
%files -n vim-X11 -f %{oreon_filedir}/vim-X11.list

%changelog

%autochangelog
