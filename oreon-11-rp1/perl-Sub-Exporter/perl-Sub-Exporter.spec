%global source0_hash 2a95695d35c5d0d5373a7e145c96b9b016113b74e94116835ac05450cae4d445
%bcond_with perl_Sub_Exporter_enables_extra_test
Name:		perl-Sub-Exporter
Version:	0.991
Release:        1%{?dist}
Summary:        Sophisticated exporter for custom-built routines
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Sub-Exporter
Source0:        https://cpan.metacpan.org/modules/by-module/Sub/Sub-Exporter-%{version}.tar.gz
BuildArch:	noarch
%if %{with perl_Sub_Exporter_enables_extra_test}
%endif
Requires:	perl(Package::Generator)
%global our_docdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}
%global __provides_exclude_from ^%{our_docdir}/
%global __requires_exclude_from ^%{our_docdir}/
Provides:       perl(Sub::Exporter)
Provides:       perl(Sub::Exporter::Util)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::OptList)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Package::Generator)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Sub::Exporter provides a sophisticated alternative to Exporter.pm. It allows
for renaming, currying/sub-generation, and other cool stuff.

ACHTUNG! If you're not familiar with Exporter or exporting, read
Sub::Exporter::Tutorial first!

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main

%check

make test
%if %{with perl_Sub_Exporter_enables_extra_test}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.991-7
- Prepare for Oreon 11 (RP1)
