%global source0_hash 02f86e62206e5f8eb5665ca2627e2a2480c92f34adee7ed3f5193e69f068891a

Name:           perl-Test-Unit
Version:        0.29
Release:        2%{?dist}
Summary:        The PerlUnit testing framework

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://perlunit.sourceforge.net/
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Test-Unit-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Inner)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Symdump)
BuildRequires:  perl(Error)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(Tk)
BuildRequires:  perl(Tk::BrowseEntry)
BuildRequires:  perl(Tk::Canvas)
BuildRequires:  perl(Tk::Derived)
BuildRequires:  perl(Tk::DialogBox)
BuildRequires:  perl(Tk::ROText)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude}|perl\\(Experimental::Sample\\)|perl\\(fail_example\\)|perl\\(fail_example_testsuite_setup\\)
%global __requires_exclude %{?__requires_exclude}|perl\\(Exporter\\)


%description
This framework is intended to support unit testing in an object-oriented
development paradigm (with support for inheritance of tests etc.) and is
derived from the JUnit testing framework for Java by Kent Beck and Erich
Gamma.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Unit-%{version}
perl -pi -e 's/\r//' examples/Experimental/Sample.pm
chmod a+x TkTestRunner.pl TestRunner.pl


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}


%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT


%check
make test


%files
%license COPYING.Artistic COPYING.GPL-2
%doc AUTHORS ChangeLog Changes doc examples README
%{perl_vendorlib}/Test*
%{_mandir}/man3/Test::Unit*.3*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.29-2
- Import
