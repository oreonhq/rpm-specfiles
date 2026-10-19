%global source0_hash c00753d7c4319eb7eae93deef418303a0f7a8b658151e9dd97ab2198683cf340
%bcond_without perl_Dist_Zilla_Plugins_CJM_enables_optional_test
Name:           perl-Dist-Zilla-Plugins-CJM
Version:        6.000
Release:        1%{?dist}
Summary:        Christopher J. Madsen's Dist::Zilla plugins
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugins-CJM
Source0:        https://cpan.metacpan.org/modules/by-module/Dist/Dist-Zilla-Plugins-CJM-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Dist_Zilla_Plugins_CJM_enables_optional_test}
%endif
Requires:       perl(CPAN::Meta::Converter) >= 2.101550
Requires:       perl(CPAN::Meta::Requirements) >= 2.121
Requires:       perl(Data::Dumper)
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
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(CPAN::Meta::Requirements\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(CPAN::Meta::Converter)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Dist::Zilla)
BuildRequires:  perl(Dist::Zilla::Plugin::InlineFiles)
BuildRequires:  perl(Dist::Zilla::Plugin::MakeMaker)
BuildRequires:  perl(Dist::Zilla::Plugin::ModuleBuild)
BuildRequires:  perl(Dist::Zilla::Role::BeforeRelease)
BuildRequires:  perl(Dist::Zilla::Role::FilePruner)
BuildRequires:  perl(Dist::Zilla::Role::MetaProvider)
BuildRequires:  perl(Dist::Zilla::Role::Releaser)
BuildRequires:  perl(Dist::Zilla::Role::VersionProvider)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(Git::Wrapper)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(autodie)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
