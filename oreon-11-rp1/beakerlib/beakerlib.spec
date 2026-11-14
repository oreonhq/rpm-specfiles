# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b4e1fd4a3ea39923583d9ac70d698b5313306f686020b857963e20b63e444d21

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           beakerlib
Version:        1.33.4
Release:        1%{?dist}
Summary:        A shell-level integration testing library
License:        GPL-2.0-only
URL:            https://github.com/beakerlib/beakerlib
Source0:        https://github.com/beakerlib/beakerlib/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-tmpfiles.conf
Patch0:         python3.patch
BuildArch:      noarch

BuildRequires:  oreon-rpm-macros
BuildRequires:  /usr/bin/pod2man
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  util-linux

Autoreq:        0
Requires:       /bin/bash
Requires:       /bin/sh
Requires:       /usr/bin/bc
Requires:       /usr/bin/time
Requires:       (wget or curl)
Requires:       coreutils
Requires:       dnf5-command(download)
Requires:       dnf5-command(repoquery)
Requires:       grep
Requires:       gzip
Requires:       iproute
Requires:       nfs-utils
Requires:       sed
Requires:       tar
Requires:       util-linux
Requires:       which
Recommends:     /usr/bin/perl
Recommends:     /usr/bin/python3
Recommends:     /usr/bin/xmllint
Recommends:     python3-lxml
Recommends:     python3-six
Suggests:       wget

%description
The BeakerLib project means to provide a library of various helpers, which
could be used when writing operating system level integration tests.

%package vim-syntax
Summary:        Files for syntax highlighting BeakerLib tests in VIM editor
Requires:       vim-common
BuildRequires:  vim-common

%description vim-syntax
Files for syntax highlighting BeakerLib tests in VIM editor.

%prep
%oreon_sha256
%autosetup -p1

%build
make build

%install
make PKGDOCDIR=%{buildroot}%{_pkgdocdir} DESTDIR=%{buildroot}%{_prefix} install
install -Dpm0644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/%{name}.conf

%check
make check

%files
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/xslt-templates
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/examples
%dir %{_pkgdocdir}/examples/*
%{_datadir}/%{name}/dictionary.vim
%{_datadir}/%{name}/*.sh
%{_datadir}/%{name}/xslt-templates/*
%{_bindir}/%{name}-*
%{_mandir}/man1/%{name}*1*
%doc %{_pkgdocdir}/*
%config %{_tmpfilesdir}/%{name}.conf

%files vim-syntax
%{_datadir}/vim/vimfiles/after/ftdetect/beakerlib.vim
%{_datadir}/vim/vimfiles/after/syntax/beakerlib.vim

%changelog
%autochangelog
