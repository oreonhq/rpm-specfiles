%global source0_hash 5762340732421f2502a770d6a126e584f2cd963351d2bc257bd278c39bce8be7

Name:           perl-MP3-Info
Version:        1.26
Release:        24%{?dist}
Summary:        Manipulate / fetch info from MP3 audio files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MP3-Info
Source0:        https://cpan.metacpan.org/authors/id/J/JM/JMERELO/MP3-Info-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(CPAN)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Runtime
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Detect::Detector)
BuildRequires:  perl(Encode::Guess)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(overload)
# Tests only
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More)
Recommends:     perl(Encode)
Recommends:     perl(Encode::Detect::Detector)
Recommends:     perl(Encode::Guess)

%description
This module is used for getting info out of and into MP3 files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn MP3-Info-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README.md eg
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
