%global source0_hash b67bf61f4308698fdd7cd492be60b60bea5cc7af9bc797b7a2178151e5159135
Name:           perl-Graphics-ColorNames
Version:        3.5.0
Release:        20%{?dist}
Summary:        Defines RGB values for common color names
License:        Artistic-2.0
URL:            https://metacpan.org/release/Graphics-ColorNames
Source0:        https://cpan.metacpan.org/authors/id/R/RR/RRWO/Graphics-ColorNames-v%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(DirHandle)
Requires:       perl(File::Spec)
Requires:       perl(IO::File)
Requires:       perl(Tie::Sub)
Requires:       perl(version)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Color::Library)
BuildRequires:  perl(Color::Library::Dictionary::NBS_ISCC::B)
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Module::Loaded)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Tie::Sub)
BuildRequires:  perl(constant)
BuildRequires:  perl(integer)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides a common interface for obtaining the RGB values of
colors by standard names. The intention is to (1) provide a common module
that authors can use with other modules to specify colors by name; and (2)
free module authors from having to "re-invent the wheel" whenever they
decide to give the users the option of specifying a color by name rather
than RGB value.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Graphics-ColorNames-v%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

unset AUTHOR_TESTING RELEASE_TESTING
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
