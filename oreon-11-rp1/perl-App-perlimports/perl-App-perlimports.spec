%global source0_hash 15e5192e9595df15f21b12fe9b5a911149b614a6f6aeb1b7febb6434fcc74d57
Name:           perl-App-perlimports
Version:        0.000058
Release:        1%{?dist}
Summary:        A command line utility for cleaning up imports in your Perl code
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/App-perlimports
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/App-perlimports-%{version}.tar.gz
BuildArch:      noarch
Requires:  perl(File::XDG) >= 1.01
Requires:  perl(Perl::Tidy) >= 20220613
Requires:  perl(Symbol::Get) >= 0.10
Requires:  perl(TOML::Tiny) >= 0.16
%{?perl_default_filter}
# oreon:deps
BuildRequires:  /usr/bin/chmod
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(Cpanel::JSON::XS)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::XDG)
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Geo::IP)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Getopt::Long::Descriptive)
BuildRequires:  perl(HTML::TableExtract)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(Import::Into)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Lingua::EN::Inflect)
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Dispatch)
BuildRequires:  perl(Log::Dispatch::Array)
BuildRequires:  perl(Memoize)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Mojo::URL)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(Mojolicious)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::StrictConstructor)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(MooseX::Types::Path::Class)
BuildRequires:  perl(PPI)
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(PPI::Dumper)
BuildRequires:  perl(PPIx::Utils::Classification)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Path::Iterator::Rule)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Perl::Critic::Utils)
BuildRequires:  perl(Perl::Tidy)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sereal::Decoder)
BuildRequires:  perl(Sereal::Encoder)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::HandlesVia)
BuildRequires:  perl(Symbol::Get)
BuildRequires:  perl(TOML::Tiny)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::HTML::Lint)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::RequiresInternet)
BuildRequires:  perl(Test::Script)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(Text::SimpleTable::AutoWidth)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(UUID)
BuildRequires:  perl(feature)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This distribution provides the perlimports command line interface (CLI),
which automates the cleanup and maintenance of Perl use and require
statements. Loosely inspired by goimports, this tool aims to be part of
your linting and tidying workflow, in much the same way you might use
perltidy or perlcritic.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir App-perlimports-%{version}
%oreon_prep
%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
