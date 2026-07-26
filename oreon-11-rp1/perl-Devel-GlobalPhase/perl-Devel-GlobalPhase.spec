%global source0_hash 8da3022f7ca71dfdbf4aa60698944d7200ac3149f4737d8a9c91bf4387ff32f5

Name:           perl-Devel-GlobalPhase
Version:        0.003003
Release:        24%{?dist}
Summary:        Detect perl's global phase on older perls
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-GlobalPhase
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Devel-GlobalPhase-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
# Tests
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(threads) >= 1.07
BuildRequires:  perl(threads::shared)

%description
This gives access to ${^GLOBAL_PHASE} in versions of perl that don't
provide it. The built-in variable will be used if it is available.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-GlobalPhase-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
