# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash c5505ae075a871a9cd8d9801859b0ff1c09782075df281c72c23e72115d9f159

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: cscope
Version: 15.9
Release: 1%{?dist}
Summary: C source code browser
License: BSD-3-Clause
URL: https://cscope.sourceforge.net/
Source0: https://downloads.sourceforge.net/project/cscope/cscope/v%{version}/cscope-%{version}.tar.gz
Patch0: cscope-1-modified-from-patch-81-Fix-reading-include-files-in-.patch
Patch1: cscope-2-Cull-extraneous-declaration.patch
Patch2: cscope-3-Avoid-putting-directories-found-during-header-search.patch
Patch3: cscope-4-Avoid-double-free-via-double-fclose-in-changestring.patch
Patch4: cscope-5-contrib-ocs-Fix-bashims-Closes-480591.patch
Patch5: cscope-6-doc-cscope.1-Fix-hyphens.patch
Patch6: cscope-7-fscanner-swallow-function-as-parameters.patch
Patch7: cscope-8-emacs-plugin-fixup-GNU-Emacs-27.1-removes-function-p.patch
Patch8: cscope-9-fix-access-beyond-end-of-string.patch
Patch9: cscope-a-docs-typo-fixes-in-man-page-and-comments.patch

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: pkgconfig(ncurses)

%description
cscope is a developers tool for browsing C source code.

%prep
%oreon_sha256
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README*
%{_bindir}/cscope
%{_bindir}/ocs
%{_mandir}/man1/cscope.1*

%changelog
%autochangelog
