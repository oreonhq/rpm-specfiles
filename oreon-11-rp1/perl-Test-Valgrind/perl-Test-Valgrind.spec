%global source0_hash 1838a7a15fee7a8f069e4e6b461c5e169058b615b8dfb43784b3d5da1a60811b

# Build --with debug_valgrind for multi-arch build and additional valgrind debugging
%bcond_with debug_valgrind

# A noarch-turned-arch package should not have debuginfo
%global debug_package %{nil}

Name:		perl-Test-Valgrind
Summary:	Generate suppressions, analyze and test any command with valgrind
Version:	1.19
Release:	29%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-Valgrind
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-Valgrind-%{version}.tar.gz
Patch1:		Test-Valgrind-1.19-Perl_pp_entersub.patch
%if !%{with debug_valgrind}
BuildArch:	noarch
%endif
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::Install) >= 1.38
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	sed
# Module Runtime
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Config)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(Env::Sanctify)
BuildRequires:	perl(ExtUtils::MM)
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(File::HomeDir) >= 0.86
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp) >= 0.19
BuildRequires:	perl(Filter::Util::Call)
BuildRequires:	perl(IO::Select)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(overload)
BuildRequires:	perl(Perl::Destruct::Level)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XML::Twig)
BuildRequires:	perl(XML::Twig::Elt)
BuildRequires:	valgrind >= 3.1.0
# Test Suite
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(XSLoader)
# Dependencies
Requires:	perl(Carp)
Requires:	perl(Config)
Requires:	perl(Digest::MD5)
Requires:	perl(DynaLoader)
Requires:	perl(File::HomeDir) >= 0.86
Requires:	perl(File::Path)
Requires:	perl(File::Temp) >= 0.14
Requires:	perl(Filter::Util::Call)
Requires:	perl(Perl::Destruct::Level)
Requires:	perl(XML::Twig)
Requires:	perl(XML::Twig::Elt)
Requires:	valgrind >= 3.1.0

Provides:       perl(Test::Valgrind)
%description
The Test::Valgrind::* API lets you run Perl code through the memcheck tool of
the valgrind memory debugger, to test for memory errors and leaks. The
Test::Valgrind module itself is a front-end to this API. If they aren't
available yet, it will first generate suppressions for the current perl
interpreter and store them in the portable flavor of
~/.perl/Test-Valgrind/suppressions/$VERSION. The actual run will then take
place, and tests will be passed or failed according to the result of the
analysis.

The complete API is much more versatile than this. By declaring an appropriate
Test::Valgrind::Command class, you can run any executable (that is, not only
Perl scripts) under valgrind, generate the corresponding suppressions
on-the-fly and convert the analysis result to TAP output so that it can be
incorporated into your project's test suite. If you're not interested in
producing TAP, you can output the results in whatever format you like (for
example HTML pages) by defining your own Test::Valgrind::Action class.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Valgrind-%{version}

# Without debuginfo, the symbol 'Perl_pp_entersub' is not always
# appearing in the valgrind trace report, causing t/20-bad.t to fail
# as a result of not recognizing the trace record
#
# This is a workaround to help the test identify the trace correctly
%patch -P 1

# Avoid doc-file deps and fix shellbangs
sed -i -e 's|^#!/usr/bin/env perl|#!/usr/bin/perl|' samples/map.pl
chmod -c -x samples/map.pl

%if %{with debug_valgrind}
# Create a wrapper script for valgrind so we can see how it's being used
mkdir bin
cat << 'EOF' > bin/valgrind
#!/bin/bash

echo "### valgrind " "$@" >> valgrind.output
/usr/bin/valgrind "$@" | tee -a valgrind.output
EOF
chmod 755 bin/valgrind
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

# The package is noarch; the XS code included is for testing purposes and is
# not part of the module itself
if [ "%{perl_vendorarch}" != "%{perl_vendorlib}" ]; then
	mkdir -p %{buildroot}%{perl_vendorlib}
	mv %{buildroot}%{perl_vendorarch}/* %{buildroot}%{perl_vendorlib}/
fi

%check
%if %{with debug_valgrind}
# Pick up our local valgrind script
PATH=$(pwd)/bin:$PATH
%endif
make test

%files
%doc Changes README samples/
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Valgrind.3*
%{_mandir}/man3/Test::Valgrind::Action.3*
%{_mandir}/man3/Test::Valgrind::Action::Captor.3*
%{_mandir}/man3/Test::Valgrind::Action::Suppressions.3*
%{_mandir}/man3/Test::Valgrind::Action::Test.3*
%{_mandir}/man3/Test::Valgrind::Carp.3*
%{_mandir}/man3/Test::Valgrind::Command.3*
%{_mandir}/man3/Test::Valgrind::Command::Aggregate.3*
%{_mandir}/man3/Test::Valgrind::Command::Perl.3*
%{_mandir}/man3/Test::Valgrind::Command::PerlScript.3*
%{_mandir}/man3/Test::Valgrind::Component.3*
%{_mandir}/man3/Test::Valgrind::Parser.3*
%{_mandir}/man3/Test::Valgrind::Parser::Suppressions::Text.3*
%{_mandir}/man3/Test::Valgrind::Parser::Text.3*
%{_mandir}/man3/Test::Valgrind::Parser::XML.3*
%{_mandir}/man3/Test::Valgrind::Parser::XML::Twig.3*
%{_mandir}/man3/Test::Valgrind::Report.3*
%{_mandir}/man3/Test::Valgrind::Session.3*
%{_mandir}/man3/Test::Valgrind::Suppressions.3*
%{_mandir}/man3/Test::Valgrind::Tool.3*
%{_mandir}/man3/Test::Valgrind::Tool::memcheck.3*
%{_mandir}/man3/Test::Valgrind::Util.3*
%{_mandir}/man3/Test::Valgrind::Version.3*

%changelog
%autochangelog
