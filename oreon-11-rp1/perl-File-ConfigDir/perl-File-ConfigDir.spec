%global source0_hash 6b405a14f69ce49d4982ed9b75400a445d0f6224fd7687fb907e79c5578314c6
Name:           perl-File-ConfigDir
Version:        0.021
Release:        1%{?dist}
Summary:        Get directories of configuration files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-ConfigDir
Source0:        https://cpan.metacpan.org/modules/by-module/File/File-ConfigDir-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(File::HomeDir) >= 0.50
Requires:       perl(List::MoreUtils) >= 0.419
Suggests:       perl(local::lib) >= 1.008008
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::MoreUtils::XS)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(local::lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
