%global source0_hash ad24bc60cc6743148b6935e9ec55737d9380374c26571946ab9c3123964cd0be
Name:           perl-Dist-Metadata
Version:        0.927
Release:        28%{?dist}
Summary:        Information about a perl module distribution
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Metadata
Source0:        https://cpan.metacpan.org/authors/id/R/RW/RWSTAUNER/Dist-Metadata-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Digest) >= 1.03
Requires:       perl(Digest::MD5) >= 2
Requires:       perl(Digest::SHA) >= 5
Requires:       perl(File::Basename)
Requires:       perl(File::Spec::Native) >= 1.002
Requires:       perl(File::Temp) >= 0.19
Requires:       perl(Module::Metadata)
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(CPAN::DistnameInfo)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Digest)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Native)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(blib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test AUTOMATED_TESTING=1
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
