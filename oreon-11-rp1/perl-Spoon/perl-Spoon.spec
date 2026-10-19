%global source0_hash a68924dfea85b783c309c279013ce06b0f77d712231ac7d01ba4ca52f0d6cdf6
Name:           perl-Spoon
Version:        0.24
Release:        1%{?dist}
Summary:        Spiffy Application Building Framework
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Spoon
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Spoon-%{version}.tar.gz
BuildArch:      noarch
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
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(CGI)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DB_File)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::All)
BuildRequires:  perl(Module::Install::Makefile)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Spiffy)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Template)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
