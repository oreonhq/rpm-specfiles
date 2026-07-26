%global source0_hash e389bcf18001017fe476a8fc244ccd81cdcaa6406b537322c7576f575d878026

Name:           perl-Dist-Zilla-Role-PluginBundle-PluginRemover
Version:        0.105
Release:        25%{?dist}
Summary:        Remove plugins from a Dist::Zilla plugin bundle
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Role-PluginBundle-PluginRemover
Source0:        https://cpan.metacpan.org/authors/id/R/RW/RWSTAUNER/Dist-Zilla-Role-PluginBundle-PluginRemover-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Dist::Zilla::Util)
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Moose::Role)
# Tests:
BuildRequires:  perl(blib) >= 1.01
BuildRequires:  perl(Dist::Zilla::Role::PluginBundle)
BuildRequires:  perl(Dist::Zilla::Role::PluginBundle::Easy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(List::Util) >= 1.45

%description
This role enables your Dist::Zilla plugin bundle to automatically remove
any plugins specified by the "-remove" attribute.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Zilla-Role-PluginBundle-PluginRemover-%{version}

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
