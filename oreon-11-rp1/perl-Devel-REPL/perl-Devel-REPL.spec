%global source0_hash 7c87ebd88fe3abab2ff8c3fb681c6446ee7a2dc1390a6df7aa604f2634473c69

Name:           perl-Devel-REPL
Version:        1.003029
Release:        12%{?dist}
Summary:        Modern perl interactive shell
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-REPL
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Devel-REPL-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Config)
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.120620
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(App::Nopaste)
BuildRequires:  perl(B::Concise) >= 0.62
BuildRequires:  perl(B::Keywords)
BuildRequires:  perl(Data::Dump::Streamer) >= 2.39
BuildRequires:  perl(Data::Dumper::Concise)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(File::Next)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Lexical::Persistence)
BuildRequires:  perl(Module::Refresh)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose) >= 0.93
BuildRequires:  perl(Moose::Meta::Role)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Getopt) >= 0.18
BuildRequires:  perl(MooseX::Object::Pluggable) >= 0.0009
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(PPI)
BuildRequires:  perl(PPI::Dumper)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sys::SigAction)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(Time::HiRes)
# Tests only
BuildRequires:  perl(if)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.94
Requires:       perl(Moose) >= 0.93
Requires:       perl(Moose::Meta::Role)
Requires:       perl(MooseX::Getopt) >= 0.18
Requires:       perl(MooseX::Object::Pluggable) >= 0.0009
# Require plugins used by default, see Devel::REPL::Profile::Minimal
Requires:       perl(Devel::REPL::Plugin::Commands)
Requires:       perl(Devel::REPL::Plugin::DDS)
Requires:       perl(Devel::REPL::Plugin::History)
Requires:       perl(Devel::REPL::Plugin::LexEnv)
Requires:       perl(Devel::REPL::Plugin::MultiLine::PPI)
Requires:       perl(Devel::REPL::Plugin::Packages)

%{?perl_default_filter}

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Data::Dump::Streamer|Moose)\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::More\\)

%description
This is an interactive shell for Perl, commonly known as a REPL - Read,
Evaluate, Print, Loop. The shell provides for rapid development or testing
of code without the need to create a temporary source code file.

Through a plugin system, many features are available on demand. These plugins
are available:

    Completion
    CompletionDriver::INC
    CompletionDriver::Keywords
    DDC
    DDS
    Interrupt
    LexEnv
    MultiLine::PPI
    Nopaste
    PPI
    Refresh

The plugins are available in standalone RPM packages. For example the
MultiLine::PPI plugin is delivered within %{name}-MultiLine-PPI package.

%package Plugin-Completion
Summary:        Devel-REPL plugin for tab completion
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-Completion
This Perl interactive shell plugin provides extensible tab completion. By
default, the Completion plugin explicitly does not use the GNU Readline or
Term::ReadLine::Perl fallback file name completion.

%package Plugin-CompletionDriver-INC
Summary:        Devel-REPL plugin for completing module names
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-CompletionDriver-INC
This Perl interactive shell plugin provides module names completion.

%package Plugin-CompletionDriver-Keywords
Summary:        Devel-REPL plugin for completing keywords and operators
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-CompletionDriver-Keywords
This Perl interactive shell plugin provides keyword and operator names
completion.

%package Plugin-DDC
Summary:        Devel-REPL plugin for formatting results with Data::Dumper::Concise
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-DDC
This Perl interactive shell plugin formats results with Data::Dumper::Concise.

%package Plugin-DDS
Summary:        Devel-REPL plugin for formatting results with Data::Dump::Streamer
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Data::Dump::Streamer) >= 2.39

%description Plugin-DDS
This Perl interactive shell plugin formats results with Data::Dump::Streamer.

%package Plugin-Interrupt
Summary:        Devel-REPL plugin for trapping INT signal
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-Interrupt
By default Devel::REPL exits on SIGINT (usually Ctrl-C). If you load this
module, SIGINT will be trapped and used to kill long-running commands
(statements) and also to kill the line being edited (like e.g. BASH do).
(You can still use Ctrl-D to exit.)

%package Plugin-LexEnv
Summary:        Devel-REPL plugin for lexical environments
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-LexEnv
This Perl interactive shell plugin provides environments for lexical variables.

%package Plugin-MultiLine-PPI
Summary:        Devel-REPL plugin for multi-line blocks
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-MultiLine-PPI
This Perl interactive shell plugin will collect lines until you have no
unfinished structures.  This lets you write subroutines, "if" statements,
loops, etc. more naturally.

%package Plugin-Nopaste
Summary:        Devel-REPL plugin for uploading data to a nopaste site
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(App::Nopaste)

%description Plugin-Nopaste
This Perl interactive shell plugin allows you to upload session's input and
output to a nopaste site.

%package Plugin-PPI
Summary:        Devel-REPL plugin for dumping Perl code
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-PPI
This Perl interactive shell plugin provides a "ppi" command that uses
PPI::Dumper to dump PPI-parsed Perl documents.

%package Plugin-Refresh
Summary:        Devel-REPL plugin for reloading libraries
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-Refresh
This Perl interactive shell plugin allows you to reload Perl libraries with
Module::Refresh module.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Devel::REPL)
Requires:       perl(Test::More) >= 0.94

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-REPL-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset AUTHOR_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENCE
%doc Changes CONTRIBUTING README examples
%{_bindir}/re.pl
%dir %{perl_vendorlib}/Devel
%{perl_vendorlib}/Devel/REPL
%{perl_vendorlib}/Devel/REPL.pm
%{_mandir}/man3/Devel::REPL.*
%{_mandir}/man3/Devel::REPL::*

# Plugin-Completion
%exclude %{perl_vendorlib}/Devel/REPL/Plugin/Completion.pm
%exclude %{_mandir}/man3/Devel::REPL::Plugin::Completion.*

# Plugin-CompletionDriver-INC
%exclude %{perl_vendorlib}/Devel/REPL/Plugin/CompletionDriver/INC.pm
%exclude %{_mandir}/man3/Devel::REPL::Plugin::CompletionDriver::INC.*

# Plugin-CompletionDriver-Keywords
%exclude %{perl_vendorlib}/Devel/REPL/Plugin/CompletionDriver/Keywords.pm
%exclude %{_mandir}/man3/Devel::REPL::Plugin::CompletionDriver::Keywords.*

# Plugin-DDC
%exclude %{perl_vendorlib}/Devel/REPL/Plugin/DDC.pm
%exclude %{_mandir}/man3/Devel::REPL::Plugin::DDC.*

# Plugin-DDS
%exclude %{perl_vendorlib}/Devel/REPL/Plugin/DDS.pm
%exclude %{_mandir}/man3/Devel::REPL::Plugin::DDS.*

# Plugin-Interrupt
%exclude %{perl_vendorlib}/Devel/REPL/Plugin/Interrupt.pm
%exclude %{_mandir}/man3/Devel::REPL::Plugin::Interrupt.*

# Plugin-LexEnv
%exclude %{perl_vendorlib}/Devel/REPL/Plugin/LexEnv.pm
%exclude %{_mandir}/man3/Devel::REPL::Plugin::LexEnv.*

# Plugin-MultiLine-PPI
%exclude %{perl_vendorlib}/Devel/REPL/Plugin/MultiLine
%exclude %{_mandir}/man3/Devel::REPL::Plugin::MultiLine::*

# Plugin-Nopaste
%exclude %{perl_vendorlib}/Devel/REPL/Plugin/Nopaste.pm
%exclude %{_mandir}/man3/Devel::REPL::Plugin::Nopaste.*

# Plugin-PPI
%exclude %{perl_vendorlib}/Devel/REPL/Plugin/PPI.pm
%exclude %{_mandir}/man3/Devel::REPL::Plugin::PPI.*

# Plugin-Refresh
%exclude %{perl_vendorlib}/Devel/REPL/Plugin/Refresh.pm
%exclude %{_mandir}/man3/Devel::REPL::Plugin::Refresh.*

%files Plugin-Completion
%{perl_vendorlib}/Devel/REPL/Plugin/Completion.pm
%{_mandir}/man3/Devel::REPL::Plugin::Completion.*

%files Plugin-CompletionDriver-INC
%{perl_vendorlib}/Devel/REPL/Plugin/CompletionDriver/INC.pm
%{_mandir}/man3/Devel::REPL::Plugin::CompletionDriver::INC.*

%files Plugin-CompletionDriver-Keywords
%{perl_vendorlib}/Devel/REPL/Plugin/CompletionDriver/Keywords.pm
%{_mandir}/man3/Devel::REPL::Plugin::CompletionDriver::Keywords.*

%files Plugin-DDC
%{perl_vendorlib}/Devel/REPL/Plugin/DDC.pm
%{_mandir}/man3/Devel::REPL::Plugin::DDC.*

%files Plugin-DDS
%{perl_vendorlib}/Devel/REPL/Plugin/DDS.pm
%{_mandir}/man3/Devel::REPL::Plugin::DDS.*

%files Plugin-Interrupt
%{perl_vendorlib}/Devel/REPL/Plugin/Interrupt.pm
%{_mandir}/man3/Devel::REPL::Plugin::Interrupt.*

%files Plugin-LexEnv
%{perl_vendorlib}/Devel/REPL/Plugin/LexEnv.pm
%{_mandir}/man3/Devel::REPL::Plugin::LexEnv.*

%files Plugin-MultiLine-PPI
%{perl_vendorlib}/Devel/REPL/Plugin/MultiLine
%{_mandir}/man3/Devel::REPL::Plugin::MultiLine::*

%files Plugin-Nopaste
%{perl_vendorlib}/Devel/REPL/Plugin/Nopaste.pm
%{_mandir}/man3/Devel::REPL::Plugin::Nopaste.*

%files Plugin-PPI
%{perl_vendorlib}/Devel/REPL/Plugin/PPI.pm
%{_mandir}/man3/Devel::REPL::Plugin::PPI.*

%files Plugin-Refresh
%{perl_vendorlib}/Devel/REPL/Plugin/Refresh.pm
%{_mandir}/man3/Devel::REPL::Plugin::Refresh.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
