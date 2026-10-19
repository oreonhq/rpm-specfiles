%global source0_hash 6e390eb7707501a86f2e648d78fddb0d211d1e8699aa1ee201176e9f966a798b
Name: po4a
Version: 0.74
Release:        1%{?dist}
Summary:        A tool maintaining translations anywhere
License: GPL-2.0-or-later
URL: https://po4a.org/
Source0:        https://github.com/mquinson/po4a/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch
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
# oreon:deps
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  coreutils
BuildRequires:  docbook-style-xsl
BuildRequires:  findutils
BuildRequires:  gettext
BuildRequires:  glibc-all-langpacks
BuildRequires:  grep
BuildRequires:  opensp
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Guess)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Install)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(I18N::Langinfo)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Locale::gettext)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(SGMLS)
BuildRequires:  perl(Syntax::Keyword::Try)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Text::WrapI18N)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(Unicode::GCString)
BuildRequires:  perl(YAML::Tiny)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  tex(article.cls)
BuildRequires:  texlive-kpathsea
BuildRequires:  texlive-kpathsea-bin
# /oreon:deps
%description
The po4a (po for anything) project goal is to ease translations (and
more interestingly, the maintenance of translations) using gettext
tools on areas where they were not expected like documentation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
chmod +x scripts/*

%build

export PO4AFLAGS="-v -v -v"
%{__perl} ./Build.PL installdirs=vendor
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*
%find_lang %{name}
%oreon_autofiles main

%check

./Build test || :
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.74-4
- Prepare for Oreon 11 (RP1)
