%global source0_hash 257f384091d33d340373a6153947039c698dc449d1ef989335644fc3d2da0069

# noarch, but to avoid debug* files interfering with manifest test:
%global debug_package %{nil}

# Similarly, for package note feature
%undefine _package_note_file

Name:		perl-MouseX-SimpleConfig
Summary:	A Mouse role for setting attributes from a simple configfile
Version:	0.11
Release:	39%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/MouseX-SimpleConfig
Source0:	https://cpan.metacpan.org/modules/by-module/MouseX/MouseX-SimpleConfig-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.31
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Config::Any) >= 0.13
BuildRequires:	perl(English)
BuildRequires:	perl(Mouse) >= 0.35
BuildRequires:	perl(Mouse::Role)
BuildRequires:	perl(MouseX::ConfigFromFile) >= 0.02
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(lib)
BuildRequires:	perl(Path::Class::File)
BuildRequires:	perl(Test::More) >= 0.88
# Optional Tests
BuildRequires:	perl(Config::General)
BuildRequires:	perl(Test::Script)
BuildRequires:	perl(YAML::Syck)
# Author Tests (not used as code is not tidy enough)
#BuildRequires:	perl(Perl::Critic::Policy::Lax::RequireExplicitPackage::ExceptForPragmata)
#BuildRequires:	perl(Perl::Critic::Policy::Subroutines::ProhibitCallsToUndeclaredSubs)
#BuildRequires:	perl(Test::Perl::Critic)
# Release Tests
BuildRequires:	perl(Pod::Coverage::TrustPod)
BuildRequires:	perl(Test::CheckChanges)
BuildRequires:	perl(Test::ConsistentVersion)
BuildRequires:	perl(Test::CPAN::Meta)
BuildRequires:	perl(Test::DistManifest)
BuildRequires:	perl(Test::EOL)
BuildRequires:	perl(Test::HasVersion)
BuildRequires:	perl(Test::Kwalitee)
BuildRequires:	perl(Test::MinimumVersion)
BuildRequires:	perl(Test::NoTabs)
BuildRequires:	perl(Test::Pod) >= 1.41
BuildRequires:	perl(Test::Pod::Coverage) >= 1.08
BuildRequires:	perl(Test::Portability::Files)
# Note: Test::Vars not used since it is FTBFS with Perl 5.38
#BuildRequires:	perl(Test::Vars)
# Dependencies
# (none)

%description
This role loads simple configfiles to set object attributes. It is based on the
abstract role MouseX::ConfigFromFile, and uses Config::Any to load your
configfile. Config::Any will in turn support any of a variety of different
config formats, detected by the file extension. See Config::Any for more
details about supported formats.

Like all MouseX::ConfigFromFile-derived configfile loaders, this module is
automatically supported by the MouseX::Getopt role as well, which allows
specifying -configfile on the command line.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MouseX-SimpleConfig-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test RELEASE_TESTING=1

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/MouseX/
%{_mandir}/man3/MouseX::SimpleConfig.3*

%changelog
%autochangelog
