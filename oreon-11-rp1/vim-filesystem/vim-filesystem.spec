# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

Name: vim-filesystem
Version: 9.1
Release: 1%{?dist}
Summary: VIM filesystem layout
License: Vim
URL: https://www.vim.org/
BuildArch: noarch

BuildRequires: oreon-rpm-macros

Provides: vim-common = %{version}-%{release}

%description
Directories used by Vim add-on packages.

%prep
:

%build
:

%install
install -m 0755 -d \
  %{buildroot}%{_datadir}/vim \
  %{buildroot}%{_datadir}/vim/vimfiles \
  %{buildroot}%{_datadir}/vim/vimfiles/after \
  %{buildroot}%{_datadir}/vim/vimfiles/autoload \
  %{buildroot}%{_datadir}/vim/vimfiles/colors \
  %{buildroot}%{_datadir}/vim/vimfiles/doc \
  %{buildroot}%{_datadir}/vim/vimfiles/ftdetect \
  %{buildroot}%{_datadir}/vim/vimfiles/ftplugin \
  %{buildroot}%{_datadir}/vim/vimfiles/indent \
  %{buildroot}%{_datadir}/vim/vimfiles/plugin \
  %{buildroot}%{_datadir}/vim/vimfiles/syntax

%check
test -d %{buildroot}%{_datadir}/vim/vimfiles

%files
%dir %{_datadir}/vim
%dir %{_datadir}/vim/vimfiles
%dir %{_datadir}/vim/vimfiles/after
%dir %{_datadir}/vim/vimfiles/autoload
%dir %{_datadir}/vim/vimfiles/colors
%dir %{_datadir}/vim/vimfiles/doc
%dir %{_datadir}/vim/vimfiles/ftdetect
%dir %{_datadir}/vim/vimfiles/ftplugin
%dir %{_datadir}/vim/vimfiles/indent
%dir %{_datadir}/vim/vimfiles/plugin
%dir %{_datadir}/vim/vimfiles/syntax

%changelog
%autochangelog
