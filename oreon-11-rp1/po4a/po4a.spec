# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 6e390eb7707501a86f2e648d78fddb0d211d1e8699aa1ee201176e9f966a798b

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: po4a
Version: 0.74
Release: 1%{?dist}
Summary: Tools for translating documentation with gettext
License: GPL-2.0-or-later
URL: https://po4a.org/
Source0: https://github.com/mquinson/po4a/archive/v%{version}/po4a-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: /usr/bin/xsltproc
BuildRequires: coreutils
BuildRequires: docbook-style-xsl
BuildRequires: findutils
BuildRequires: grep
BuildRequires: glibc-all-langpacks
BuildRequires: perl-interpreter >= 4:5.10.1
BuildRequires: perl-generators
BuildRequires: perl(lib)
BuildRequires: perl(Encode)
BuildRequires: perl(ExtUtils::Install)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::stat)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Pod::Man)
BuildRequires: gettext
BuildRequires: opensp
BuildRequires: perl(Carp)
BuildRequires: perl(Config)
BuildRequires: perl(Cwd)
BuildRequires: perl(DynaLoader)
BuildRequires: perl(Encode::Guess)
BuildRequires: perl(Exporter)
BuildRequires: perl(Fcntl)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(Getopt::Std)
BuildRequires: perl(IO::File)
BuildRequires: perl(Pod::Parser)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(POSIX)
BuildRequires: perl(SGMLS) >= 1.03ii
BuildRequires: perl(strict)
BuildRequires: perl(subs)
BuildRequires: perl(Time::Local)
BuildRequires: perl(vars)
BuildRequires: perl(warnings)
BuildRequires: texlive-base
BuildRequires: perl(I18N::Langinfo)
BuildRequires: perl(Locale::gettext) >= 1.01
BuildRequires: perl(Term::ReadKey)
BuildRequires: perl(Text::WrapI18N)
BuildRequires: perl(Unicode::GCString)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
%bcond_with extra_perl
%if %{with extra_perl}
BuildRequires: perl(Syntax::Keyword::Try)
BuildRequires: perl(YAML::Tiny)
BuildRequires: tex(article.cls)
%endif

Requires: /usr/bin/xsltproc
Requires: gettext
Requires: opensp
Requires: texlive-kpathsea
Requires: texlive-kpathsea-bin
Requires: perl(Locale::gettext) >= 1.01
Requires: perl(I18N::Langinfo)
Requires: perl(Term::ReadKey)
Requires: perl(Text::WrapI18N)
Requires: perl(Unicode::GCString)

%description
po4a eases translations using gettext tools on documentation.

%prep
%oreon_sha256
%autosetup -p1
chmod +x scripts/*

%build
export PO4AFLAGS="-v -v -v"
%{__perl} ./Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'
%{_fixperms} %{buildroot}/*
%find_lang %{name}

%check
./Build test

%files -f %{name}.lang
%license COPYING
%doc README* TODO
%{_bindir}/*
%{perl_vendorlib}/Locale/
%{perl_vendorlib}/Po4a/
%{_mandir}/man*/*
%{_datadir}/po4a/

%changelog
%autochangelog
