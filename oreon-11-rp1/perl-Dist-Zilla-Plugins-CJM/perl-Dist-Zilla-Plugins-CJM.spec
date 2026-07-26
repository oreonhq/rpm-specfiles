%global source0_hash c00753d7c4319eb7eae93deef418303a0f7a8b658151e9dd97ab2198683cf340

# Run optinonal test
%bcond_without perl_Dist_Zilla_Plugins_CJM_enables_optional_test

Name:           perl-Dist-Zilla-Plugins-CJM
Version:        6.000
Release:        25%{?dist}
Summary:        Christopher J. Madsen's Dist::Zilla plugins
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugins-CJM
Source0:        https://cpan.metacpan.org/modules/by-module/Dist/Dist-Zilla-Plugins-CJM-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(autodie)
BuildRequires:  perl(CPAN::Meta::Converter) >= 2.101550
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.121
BuildRequires:  perl(Data::Dumper)
# A Dist::Zilla plugin, version from META
BuildRequires:  perl(Dist::Zilla) >= 6
BuildRequires:  perl(Dist::Zilla::Plugin::InlineFiles)
BuildRequires:  perl(Dist::Zilla::Plugin::MakeMaker) >= 4.300009
BuildRequires:  perl(Dist::Zilla::Plugin::ModuleBuild)
BuildRequires:  perl(Dist::Zilla::Role::BeforeRelease)
BuildRequires:  perl(Dist::Zilla::Role::FilePruner)
BuildRequires:  perl(Dist::Zilla::Role::MetaProvider)
BuildRequires:  perl(Dist::Zilla::Role::Releaser)
BuildRequires:  perl(Dist::Zilla::Role::VersionProvider)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::HomeDir) >= 0.81
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(Git::Wrapper)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(version) >= 0.77
# Tests:
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Try::Tiny)
%if %{with perl_Dist_Zilla_Plugins_CJM_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Fatal)
%endif
Requires:       perl(CPAN::Meta::Converter) >= 2.101550
Requires:       perl(CPAN::Meta::Requirements) >= 2.121
Requires:       perl(Data::Dumper)
# A Dist::Zilla plugin, version from META
Requires:       perl(Dist::Zilla) >= 6
Requires:       perl(Dist::Zilla::Plugin::InlineFiles)
Requires:       perl(Dist::Zilla::Plugin::ModuleBuild)
Requires:       perl(Dist::Zilla::Role::BeforeRelease)
Requires:       perl(Dist::Zilla::Role::FilePruner)
Requires:       perl(Dist::Zilla::Role::MetaProvider)
Requires:       perl(Dist::Zilla::Role::Releaser)
Requires:       perl(Dist::Zilla::Role::VersionProvider)
Requires:       perl(File::Copy)
Requires:       perl(File::HomeDir) >= 0.81

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(CPAN::Meta::Requirements\\)$

%description
This is a collection of plugins Christopher J. Madsen has written for
Dist::Zilla, a Perl build an release management tool.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Zilla-Plugins-CJM-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
