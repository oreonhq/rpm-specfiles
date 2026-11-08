# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4d7e4fdef2eca6afe07a2682151cea78781e0a4e8f9622142d9f70c083a2fd4f

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
# Supported build option:
#
# --with nls ... build this package with --enable-nls 

Name:           help2man
Summary:        Create simple man pages from --help output
Version:        1.49.3
Release:        1%{?dist}
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/help2man/
Source0:        https://mirror.cs.odu.edu/gnu/help2man/help2man-%{version}.tar.xz

%bcond_with nls

%{!?with_nls:BuildArch: noarch}

BuildRequires:  gcc
BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Text::Tabs)
BuildRequires:  perl(strict)
BuildRequires:  oreon-rpm-macros
%{?with_nls:BuildRequires: perl(Locale::gettext) /usr/bin/msgfmt}
%{?with_nls:BuildRequires: perl(Encode)}
%{?with_nls:BuildRequires: perl(I18N::Langinfo)}

%description
help2man is a script to create simple man pages from the --help and
--version output of programs.

Since most GNU documentation is now in info format, this provides a
way to generate a placeholder man page pointing to that resource while
still providing some useful information.

%prep
%oreon_sha256

%setup -q -n help2man-%{version}

%build
%configure --%{!?with_nls:disable}%{?with_nls:enable}-nls --libdir=%{_libdir}/help2man
%{make_build}

%install
%{__make} install_l10n DESTDIR=$RPM_BUILD_ROOT
%{make_install}
%find_lang %name --with-man

%files -f %name.lang
%doc README NEWS THANKS
%license COPYING
%{_bindir}/help2man
%{_infodir}/*
%{_mandir}/man1/*

%if %{with nls}
%{_libdir}/help2man
%endif

