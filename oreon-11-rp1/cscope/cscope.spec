%global source0_hash c5505ae075a871a9cd8d9801859b0ff1c09782075df281c72c23e72115d9f159
%bcond_with xemacs
Summary:        C source code tree search and browse tool
Name: cscope
Version: 15.9
Release:        1%{?dist}
Source0:        https://downloads.sourceforge.net/project/%{name}/%{name}/v%{version}/%{name}-%{version}.tar.gz
URL: http://cscope.sourceforge.net
License: BSD-3-Clause AND GPL-2.0-or-later
Requires: emacs-filesystem coreutils ed
%if %{with xemacs}
Requires: xemacs-filesystem
%endif
Patch1: cscope-1-modified-from-patch-81-Fix-reading-include-files-in-.patch
Patch2: cscope-2-Cull-extraneous-declaration.patch
Patch3: cscope-3-Avoid-putting-directories-found-during-header-search.patch
Patch4: cscope-4-Avoid-double-free-via-double-fclose-in-changestring.patch
Patch5: cscope-5-contrib-ocs-Fix-bashims-Closes-480591.patch
Patch6: cscope-6-doc-cscope.1-Fix-hyphens.patch
Patch7: cscope-7-fscanner-swallow-function-as-parameters.patch
Patch8: cscope-8-emacs-plugin-fixup-GNU-Emacs-27.1-removes-function-p.patch
Patch9: cscope-9-fix-access-beyond-end-of-string.patch
Patch10: cscope-a-docs-typo-fixes-in-man-page-and-comments.patch
Patch11: dist-1-coverity-fixes.patch
Patch12: dist-2-cscope-indexer-help.patch
Patch13: dist-3-add-selftests.patch
Patch14: dist-4-fix-printf.patch
Patch15: dist-5-fix-signal-handler.patch
%define cscope_share_path %{_datadir}/cscope
%if %{with xemacs}
%define xemacs_lisp_path %{_datadir}/xemacs/site-packages/lisp
%else
%define xemacs_lisp_path %nil
%endif
%define emacs_lisp_path %{_datadir}/emacs/site-lisp
%define vim_plugin_path %{_datadir}/vim/vimfiles/plugin
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pkgconf-pkg-config
# /oreon:deps
%description
cscope is a mature, ncurses based, C source code tree browsing tool.  It
allows users to search large source code bases for variables, functions,
macros, etc, as well as perform general regex and plain text searches.
Results are returned in lists, from which the user can select individual
matches for use in file editing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

aclocal
autoheader
autoconf
automake --add-missing
%configure
make
%install
rm -rf $RPM_BUILD_ROOT %{name}-%{version}.files
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT/var/lib/cs
mkdir -p $RPM_BUILD_ROOT%{cscope_share_path}
cp -a contrib/xcscope/xcscope.el $RPM_BUILD_ROOT%{cscope_share_path}
install -m 755 contrib/xcscope/cscope-indexer $RPM_BUILD_ROOT%{_bindir}
cp -a contrib/cctree.vim $RPM_BUILD_ROOT%{cscope_share_path}
for dir in %{xemacs_lisp_path} %{emacs_lisp_path} ; do
  mkdir -p $RPM_BUILD_ROOT$dir
  ln -s %{cscope_share_path}/xcscope.el $RPM_BUILD_ROOT$dir
  touch $RPM_BUILD_ROOT$dir/xcscope.elc
  echo "%ghost $dir/xcscope.el*" >> %{name}-%{version}.files
done
%oreon_autofiles main

%check

make check
%triggerin -- xemacs

ln -sf %{cscope_share_path}/xcscope.el %{xemacs_lisp_path}/xcscope.el
%triggerin -- emacs, emacs-nox, emacs-nw, emacs-lucid, emacs-gtk+x11

ln -sf %{cscope_share_path}/xcscope.el %{emacs_lisp_path}/xcscope.el
%triggerin -- vim-filesystem

ln -sf %{cscope_share_path}/cctree.vim %{vim_plugin_path}/cctree.vim
%if %{with xemacs}
%triggerun -- xemacs

[ $2 -gt 0 ] && exit 0
rm -f %{xemacs_lisp_path}/xcscope.el
%endif
%triggerun -- emacs, emacs-nox, emacs-nw, emacs-lucid, emacs-gtk+x11

[ $2 -gt 0 ] && exit 0
rm -f %{emacs_lisp_path}/xcscope.el
%triggerun -- vim-filesystem

[ $2 -gt 0 ] && exit 0
rm -f %{vim_plugin_path}/cctree.vim
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 15.9-30
- Prepare for Oreon 11 (RP1)
