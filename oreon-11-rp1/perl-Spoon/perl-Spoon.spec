%global source0_hash a68924dfea85b783c309c279013ce06b0f77d712231ac7d01ba4ca52f0d6cdf6

Name:           perl-Spoon
Version:        0.24
Release:        57%{?dist}
Summary:        Spiffy Application Building Framework
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Spoon
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Spoon-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Makefile)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CGI)
# CGI::Util not used for tests
BuildRequires:  perl(Config)
# Data::Dumper not used for tests
BuildRequires:  perl(DB_File)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(IO::All) >= 0.32
# MIME::Base64 not used for tests
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Spiffy) >= 0.24
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Template) >= 2.10
BuildRequires:  perl(Time::HiRes)
# Tests only
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(warnings)
# Optional tests only
BuildRequires:  perl(Test::Memory::Cycle)
Requires:       perl(Carp)
Requires:       perl(CGI::Util)
Requires:       perl(Config)
Requires:       perl(Data::Dumper)
Requires:       perl(Encode)
Requires:       perl(File::Path)
Requires:       perl(IO::All) >= 0.32
Requires:       perl(MIME::Base64)
Requires:       perl(Spiffy) >= 0.24
Requires:       perl(Storable)
Requires:       perl(strict)
Requires:       perl(Template) >= 2.10

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(IO::All|Spiffy|Template\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(IO::All\\)$

%description
Spoon is an Application Framework that is designed primarily for
building Social Software web applications. The Kwiki wiki software is
built on top of Spoon.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Spoon-%{version}
# Remove bundled modules
rm -r ./inc/*
sed -i -e '/^inc\//d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
