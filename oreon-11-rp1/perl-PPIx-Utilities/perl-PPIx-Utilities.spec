%global source0_hash 03a483386fd6a2c808f09778d44db06b02c3140fb24ba4bf12f851f46d3bcb9b

# Run extra test
%if ! (0%{?rhel})
%bcond_without perl_PPIx_Utilities_enables_extra_test
%else
%bcond_with perl_PPIx_Utilities_enables_extra_test
%endif

Name:		perl-PPIx-Utilities
Version:	1.001000
Release:	56%{?dist}
Summary:	Extensions to PPI
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/PPIx-Utilities
Source0:	https://cpan.metacpan.org/authors/id/E/EL/ELLIOTJS/PPIx-Utilities-%{version}.tar.gz
BuildArch:	noarch
# Build:
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	sed
# Run-time:
BuildRequires:	perl(base)
BuildRequires:	perl(Exception::Class)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(PPI) >= 1.208
BuildRequires:	perl(PPI::Document::Fragment) >= 1.208
BuildRequires:	perl(Readonly)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Tests:
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(PPI::Document) >= 1.208
BuildRequires:	perl(PPI::Dumper) >= 1.208
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::More)
# Extra tests:
# PPI needed by Perl::Critic, so don't run extra tests when bootstrapping
%if 0%{!?perl_bootstrap:1} && %{with perl_PPIx_Utilities_enables_extra_test}
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(Perl::Critic::Policy::Miscellanea::RequireRcsKeywords)
BuildRequires:	perl(Test::Perl::Critic)
BuildRequires:	perl(Test::Distribution)
BuildRequires:	perl(Test::Kwalitee)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
%endif
# Dependencies:
# (none)

%description
This is a collection of functions for dealing with PPI objects, many of
which originated in Perl::Critic. They are organized into modules by the
kind of PPI class they relate to, by replacing the "PPI" at the front of
the module name with "PPIx::Utilities", e.g. functionality related to
PPI::Nodes is in PPIx::Utilities::Node.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n PPIx-Utilities-%{version}

# Remove date-sensitive copyright.t, which also upsets Perl::Critic
# (#1139503)
rm xt/author/copyright.t
sed -i -e '/copyright\.t/d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test
%if 0%{!?perl_bootstrap:1} && %{with perl_PPIx_Utilities_enables_extra_test}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/PPIx/
%{_mandir}/man3/PPIx::Utilities.3*
%{_mandir}/man3/PPIx::Utilities::Exception::Bug.3*
%{_mandir}/man3/PPIx::Utilities::Node.3*
%{_mandir}/man3/PPIx::Utilities::Statement.3*

%changelog
%autochangelog
