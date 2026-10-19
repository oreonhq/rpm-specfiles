%global source0_hash ab970b50349f87975ac7e3d5f0297f8d67e4f6fe09564778f27f42eca27ea154
%bcond_without perl_Dist_Zilla_Plugin_CheckChangesHasContent_enables_optional_test
Name:           perl-Dist-Zilla-Plugin-CheckChangesHasContent
Version:        0.011
Release:        25%{?dist}
Summary:        Ensure Changes file has content before releasing
License:        Apache-2.0
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-CheckChangesHasContent
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Dist-Zilla-Plugin-CheckChangesHasContent-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Dist_Zilla_Plugin_CheckChangesHasContent_enables_optional_test}
%endif
Requires:       perl(Dist::Zilla::File::InMemory)
Requires:       perl(Dist::Zilla::Role::BeforeRelease)
Requires:       perl(Dist::Zilla::Role::FileGatherer)
Requires:       perl(Dist::Zilla::Role::FileMunger)
Requires:       perl(Dist::Zilla::Role::TextTemplate)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Section)
BuildRequires:  perl(Dist::Zilla)
BuildRequires:  perl(Dist::Zilla::File::InMemory)
BuildRequires:  perl(Dist::Zilla::Plugin::NextRelease)
BuildRequires:  perl(Dist::Zilla::Role::BeforeRelease)
BuildRequires:  perl(Dist::Zilla::Role::FileGatherer)
BuildRequires:  perl(Dist::Zilla::Role::FileMunger)
BuildRequires:  perl(Dist::Zilla::Role::TextTemplate)
BuildRequires:  perl(Dist::Zilla::Tester)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Sub::Exporter::ForMethods)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(autodie)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a "before release" Dist::Zilla plugin that ensures that your
Changes file actually has some content since the last release. If it
doesn't find any, it will abort the release process.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Zilla-Plugin-CheckChangesHasContent-%{version}

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
