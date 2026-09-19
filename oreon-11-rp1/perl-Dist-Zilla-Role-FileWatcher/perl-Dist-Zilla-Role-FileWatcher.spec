%global source0_hash fe3a44b9586daf1277fcbbbaf7216b02ce23efbbd694f0df11b7f75344be4e96

Name:           perl-Dist-Zilla-Role-FileWatcher
Version:        0.006
Release:        27%{?dist}
Summary:        Receive notification when something changes a file's contents
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Role-FileWatcher
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Dist-Zilla-Role-FileWatcher-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.6
# Module::Build::Tiny 0.039 not helpful
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Digest::MD5)
# This is a Dist::Zilla plugin
BuildRequires:  perl(Dist::Zilla) >= 4.300039
BuildRequires:  perl(Encode)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Safe::Isa)
# Tests:
BuildRequires:  perl(Dist::Zilla::File::InMemory)
BuildRequires:  perl(Dist::Zilla::Role::FileGatherer)
BuildRequires:  perl(Dist::Zilla::Role::FileMunger)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(if)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
# Test::Warnings not used
# Optional tests:
BuildRequires:  perl(Moose::Conflicts)
# This is a Dist::Zilla plugin
Requires:       perl(Dist::Zilla) >= 4.300039

%description
This is a role for Dist::Zilla plugins which gives you a mechanism for
detecting and acting on files changing their content. This is useful if
your plugin performs an action based on a file's content (perhaps copying
that content to another file), and then later in the build process, that
source file's content is later modified.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Zilla-Role-FileWatcher-%{version}

%build
export PERL_MM_FALLBACK_SILENCE_WARNING=1
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
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
