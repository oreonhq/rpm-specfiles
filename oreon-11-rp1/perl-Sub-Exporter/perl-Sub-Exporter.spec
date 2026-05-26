# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 2a95695d35c5d0d5373a7e145c96b9b016113b74e94116835ac05450cae4d445
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# Run extra test
%if ! (0%{?rhel})
%bcond_without perl_Sub_Exporter_enables_extra_test
%else
%bcond_with perl_Sub_Exporter_enables_extra_test
%endif

Name:		perl-Sub-Exporter
Version:	0.991
Release:	7%{?dist}
Summary:	Sophisticated exporter for custom-built routines
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Sub-Exporter
Source0:	https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Sub-Exporter-0.991.tar.gz

BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(:VERSION) >= 5.12.0
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.78
# Module
BuildRequires:	perl(Carp)
BuildRequires:	perl(Data::OptList) >= 0.1
BuildRequires:	perl(Package::Generator)
BuildRequires:	perl(Params::Util) >= 0.14
BuildRequires:	perl(strict)
BuildRequires:	perl(Sub::Install) >= 0.92
BuildRequires:	perl(warnings)
# Test suite
BuildRequires:	perl(base)
BuildRequires:	perl(blib)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(lib)
BuildRequires:	perl(subs)
BuildRequires:	perl(Test::More) >= 0.96
# Optional tests
BuildRequires:	perl(CPAN::Meta) >= 2.120900
# Extra tests
%if %{with perl_Sub_Exporter_enables_extra_test}
BuildRequires:	perl(Encode)
BuildRequires:	perl(Test::Pod) >= 1.41
%endif
# Dependencies
Requires:	perl(Package::Generator)

# Don't want doc-file provides or dependencies
%global our_docdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}
%global __provides_exclude_from ^%{our_docdir}/
%global __requires_exclude_from ^%{our_docdir}/

%description
Sub::Exporter provides a sophisticated alternative to Exporter.pm. It allows
for renaming, currying/sub-generation, and other cool stuff.

ACHTUNG! If you're not familiar with Exporter or exporting, read
Sub::Exporter::Tutorial first!

%prep
%oreon_verify_sources
%setup -q -n Sub-Exporter-%{version}

# Fix shellbangs
find t/ -type f -exec \
	perl -MExtUtils::MakeMaker -e 'ExtUtils::MM_Unix->fixin(qw{{}})' \;

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test
%if %{with perl_Sub_Exporter_enables_extra_test}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif

%files
%doc Changes README t/
%dir %{perl_vendorlib}/Sub/
%dir %{perl_vendorlib}/Sub/Exporter/
%{perl_vendorlib}/Sub/Exporter.pm
%{perl_vendorlib}/Sub/Exporter/Util.pm
%doc %{perl_vendorlib}/Sub/Exporter/Cookbook.pod
%doc %{perl_vendorlib}/Sub/Exporter/Tutorial.pod
%{_mandir}/man3/Sub::Exporter.3*
%{_mandir}/man3/Sub::Exporter::Cookbook.3*
%{_mandir}/man3/Sub::Exporter::Tutorial.3*
%{_mandir}/man3/Sub::Exporter::Util.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.991-7
- Prepare for Oreon 11 (RP1)
