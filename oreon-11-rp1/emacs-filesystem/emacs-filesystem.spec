# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

Name: emacs-filesystem
Epoch: 1
Version: 30.2
Release: 1%{?dist}
Summary: Emacs filesystem layout
License: CC0-1.0
URL: https://www.gnu.org/software/emacs/
BuildArch: noarch

BuildRequires: oreon-rpm-macros

%description
Directories required by packages that add functionality to Emacs.

%prep
:

%build
:

%install
install -m 0755 -d %{buildroot}%{_datadir}/emacs \
                   %{buildroot}%{_datadir}/emacs/site-lisp \
                   %{buildroot}%{_datadir}/emacs/site-lisp/site-start.d \
                   %{buildroot}%{_libdir}/emacs/site-lisp

%check
test -d %{buildroot}%{_datadir}/emacs/site-lisp

%files
%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/site-lisp
%dir %{_datadir}/emacs/site-lisp/site-start.d
%dir %{_libdir}/emacs
%dir %{_libdir}/emacs/site-lisp

%changelog
%autochangelog
