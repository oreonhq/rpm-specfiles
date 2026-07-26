%global source0_hash ad24bc60cc6743148b6935e9ec55737d9380374c26571946ab9c3123964cd0be

Name:           perl-Dist-Metadata
Version:        0.927
Release:        28%{?dist}
Summary:        Information about a perl module distribution
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Metadata
Source0:        https://cpan.metacpan.org/authors/id/R/RW/RWSTAUNER/Dist-Metadata-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Archive::Tar) >= 1
BuildRequires:  perl(Archive::Zip) >= 1.30
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN::DistnameInfo) >= 0.12
BuildRequires:  perl(CPAN::Meta) >= 2.1
BuildRequires:  perl(Digest) >= 1.03
BuildRequires:  perl(Digest::MD5) >= 2
BuildRequires:  perl(Digest::SHA) >= 5
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Native) >= 1.002
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(parent)
BuildRequires:  perl(Path::Class) >= 0.24
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::MockObject) >= 1.09
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Try::Tiny) >= 0.09
BuildRequires:  perl(warnings)
Requires:       perl(Digest) >= 1.03
Requires:       perl(Digest::MD5) >= 2
Requires:       perl(Digest::SHA) >= 5
Requires:       perl(File::Basename)
Requires:       perl(File::Spec::Native) >= 1.002
Requires:       perl(File::Temp) >= 0.19
Requires:       perl(Module::Metadata)

%description
This module provides an easy interface for getting various metadata about a
Perl module distribution.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Metadata-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test AUTOMATED_TESTING=1

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
