%global source0_hash 7c87ebd88fe3abab2ff8c3fb681c6446ee7a2dc1390a6df7aa604f2634473c69
Name:           perl-Devel-REPL
Version:        1.003029
Release:        1%{?dist}
Summary:        Modern perl interactive shell
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-REPL
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Devel-REPL-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Moose) >= 0.93
Requires:       perl(Moose::Meta::Role)
Requires:       perl(MooseX::Getopt) >= 0.18
Requires:       perl(MooseX::Object::Pluggable) >= 0.0009
Requires:       perl(Devel::REPL::Plugin::Commands)
Requires:       perl(Devel::REPL::Plugin::DDS)
Requires:       perl(Devel::REPL::Plugin::History)
Requires:       perl(Devel::REPL::Plugin::LexEnv)
Requires:       perl(Devel::REPL::Plugin::MultiLine::PPI)
Requires:       perl(Devel::REPL::Plugin::Packages)
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Data::Dump::Streamer|Moose)\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::More\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(App::Nopaste)
BuildRequires:  perl(B::Concise)
BuildRequires:  perl(B::Keywords)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dump::Streamer)
BuildRequires:  perl(Data::Dumper::Concise)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Next)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Lexical::Persistence)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Refresh)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Meta::Role)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Getopt)
BuildRequires:  perl(MooseX::Object::Pluggable)
BuildRequires:  perl(PPI)
BuildRequires:  perl(PPI::Dumper)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sys::SigAction)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(if)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
unset AUTHOR_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Devel-REPL-Plugin-Completion -f %{oreon_filedir}/perl-Devel-REPL-Plugin-Completion.list
%files -n perl-Devel-REPL-Plugin-CompletionDriver-INC -f %{oreon_filedir}/perl-Devel-REPL-Plugin-CompletionDriver-INC.list
%files -n perl-Devel-REPL-Plugin-CompletionDriver-Keywords -f %{oreon_filedir}/perl-Devel-REPL-Plugin-CompletionDriver-Keywords.list
%files -n perl-Devel-REPL-Plugin-DDC -f %{oreon_filedir}/perl-Devel-REPL-Plugin-DDC.list
%files -n perl-Devel-REPL-Plugin-DDS -f %{oreon_filedir}/perl-Devel-REPL-Plugin-DDS.list
%files -n perl-Devel-REPL-Plugin-Interrupt -f %{oreon_filedir}/perl-Devel-REPL-Plugin-Interrupt.list
%files -n perl-Devel-REPL-Plugin-LexEnv -f %{oreon_filedir}/perl-Devel-REPL-Plugin-LexEnv.list
%files -n perl-Devel-REPL-Plugin-MultiLine-PPI -f %{oreon_filedir}/perl-Devel-REPL-Plugin-MultiLine-PPI.list
%files -n perl-Devel-REPL-Plugin-Nopaste -f %{oreon_filedir}/perl-Devel-REPL-Plugin-Nopaste.list
%files -n perl-Devel-REPL-Plugin-PPI -f %{oreon_filedir}/perl-Devel-REPL-Plugin-PPI.list
%files -n perl-Devel-REPL-Plugin-Refresh -f %{oreon_filedir}/perl-Devel-REPL-Plugin-Refresh.list
%files -n perl-Devel-REPL-tests -f %{oreon_filedir}/perl-Devel-REPL-tests.list

%changelog

%autochangelog
