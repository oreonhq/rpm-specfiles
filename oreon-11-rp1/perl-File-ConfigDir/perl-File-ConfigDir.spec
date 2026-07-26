%global source0_hash 6b405a14f69ce49d4982ed9b75400a445d0f6224fd7687fb907e79c5578314c6

Name:           perl-File-ConfigDir
Version:        0.021
Release:        24%{?dist}
Summary:        Get directories of configuration files
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-ConfigDir
Source0:        https://cpan.metacpan.org/modules/by-module/File/File-ConfigDir-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::HomeDir) >= 0.50
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(parent)
BuildRequires:  perl(vars)
# Recommended:
BuildRequires:  perl(List::MoreUtils) >= 0.419
BuildRequires:  perl(List::MoreUtils::XS) >= 0.418
# Tests:
BuildRequires:  perl(File::Path) >= 2.00
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(local::lib) >= 1.008008
BuildRequires:  perl(Test::More) >= 0.9
BuildRequires:  perl(Test::Without::Module)
Requires:       perl(File::HomeDir) >= 0.50
# Recommended:
Requires:       perl(List::MoreUtils) >= 0.419
# Suggests:
Suggests:       perl(local::lib) >= 1.008008

%description
This module is a helper for installing, reading and finding configuration
file locations. It's intended to work in every supported Perl5 environment
and will always try to Do The Right Thing(TM).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-ConfigDir-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license ARTISTIC-1.0 GPL-1 LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
