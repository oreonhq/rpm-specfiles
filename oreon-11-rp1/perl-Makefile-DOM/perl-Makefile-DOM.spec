%global source0_hash df54998f4c523489ab0c4d8b2fae44c9bb04a98c63a7d5004d0179e5dcf75824
Name:           perl-Makefile-DOM
Version:        0.008
Release:        1%{?dist}
Summary:        Simple DOM parser for Makefiles
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Makefile-DOM
Source0:        https://cpan.metacpan.org/authors/id/A/AG/AGENT/Makefile-DOM-%{version}.tar.gz
Patch0:         Makefile-DOM-0.008-Do-not-use-_-in-a-List-Moreutils-any-code-argument.patch
BuildArch:      noarch
Requires:       perl(Clone) >= 0.18
Requires:       perl(List::MoreUtils) >= 0.21
Requires:       perl(Params::Util) >= 0.22
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Clone|List::MoreUtil|Params::Util)\\)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(CPAN)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This libary can serve as an advanced lexer for (GNU) makefiles. It parses
makefiles as "documents" and the parsing is lossless. The results are data
structures similar to DOM trees. The DOM trees hold every single bit of the
information in the original input files, including white spaces, blank
lines and makefile comments. That means it's possible to reproduce the
original makefiles from the DOM trees. In addition, each node of the DOM
trees is modifiable and so is the whole tree, just like the PPI module used
for Perl source parsing and the HTML::TreeBuilder module used for parsing
HTML source.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Makefile-DOM-%{version}
%patch -P0 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
