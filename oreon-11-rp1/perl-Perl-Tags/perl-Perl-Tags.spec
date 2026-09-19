%global source0_hash 0230551d9379f857f596c149190c5f35422dfd6df24ce104ec070c287daf5741

Name:           perl-Perl-Tags
Version:        0.32
Release:        33%{?dist}
Summary:        Generate Ctags style tags for Perl source code
License:        ( GPL-1.0-or-later OR Artistic-1.0-Perl ) OR Vim
URL:            https://metacpan.org/release/Perl-Tags
Source0:        https://cpan.metacpan.org/authors/id/O/OS/OSFAMERON/Perl-Tags-%{version}.tar.gz
# Remove /usr/bin/env from shebang
Patch0:         Perl-Tags-0.32-Remove-usr-bin-perl-from-shebang.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Locate)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(PPI)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  vim-enhanced
# Tests
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(Test::More) >= 0.42
BuildRequires:  perl(Test::Strict)

%{?perl_default_filter}

%description
Generate (possibly exuberant) Ctags style tags for Perl source code.

Recursively follows use and require statements, up to a maximum of max_level.

The implemented tagger, Perl::Tags::Naive is a more-or-less straight ripoff,
slightly updated, of the original pltags code, and is rather naive. It should
be possible to subclass using something like PPI or Text::Balanced, though be
aware that this is alpha software and the internals are subject to change.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Perl-Tags-%{version}
%patch -P0 -p1
# Remove bundled modules
rm -r inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
find -type f -exec chmod -x {} +

%build
PERL5_CPANPLUS_IS_RUNNING=1 perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README TODO
%{perl_vendorlib}/App*
%{perl_vendorlib}/Perl*
%{perl_vendorlib}/Test*
%{_bindir}/perl-tags
%{_bindir}/require-perl-tags
%{_bindir}/require-perl-tags-packed
%{_mandir}/man1/perl-tags*
%{_mandir}/man3/*Perl::Tags*

%changelog
%autochangelog
