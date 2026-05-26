# Run optional tests
%if ! (0%{?rhel})
%bcond_without perl_IPC_System_Simple_enables_optional_test
%else
%bcond_with perl_IPC_System_Simple_enables_optional_test
%endif

Name:		perl-IPC-System-Simple
Version:	1.30
Release:	17%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:	Run commands simply, with detailed diagnostics
URL:		https://metacpan.org/release/IPC-System-Simple
Source0:	https://cpan.metacpan.org/authors/id/J/JK/JKEENAN/IPC-System-Simple-1.30.tar.gz
# oreon url source checksums begin
%global source0_sha256 22e6f5222b505ee513058fdca35ab7a1eab80539b98e5ca4a923a70a8ae9ba9e
%global source0_file IPC-System-Simple-1.30.tar.gz
# oreon url source checksums end

BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Config)
BuildRequires:	perl(constant)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(re)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)
%if %{with perl_IPC_System_Simple_enables_optional_test}
# Optional Tests
BuildRequires:	perl(BSD::Resource)
BuildRequires:	perl(Test::NoWarnings)
%endif
# Dependencies
# (none)

%description
Calling Perl's in-built 'system()' function is easy; determining if it
was successful is _hard_. Let's face it, '$?' isn't the nicest variable
in the world to play with, and even if you _do_ check it, producing a
well-formatted error string takes a lot of work. 'IPC::System::Simple'
takes the hard work out of calling external commands. In fact, if you
want to be really lazy, you can just write:

    use IPC::System::Simple qw(system);

and all of your "system" commands will either succeed (run to completion and
return a zero exit value), or die with rich diagnostic messages.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/IPC-System-Simple-1.30.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "22e6f5222b505ee513058fdca35ab7a1eab80539b98e5ca4a923a70a8ae9ba9e" || { echo "oreon: Source0 SHA256 mismatch for IPC-System-Simple-1.30.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n IPC-System-Simple-%{version}

# Avoid doc-file dependencies
chmod -c -x examples/*.pl

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README examples/
%{perl_vendorlib}/IPC/
%{_mandir}/man3/IPC::System::Simple.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.30-17
- Prepare for Oreon 11 (RP1)
