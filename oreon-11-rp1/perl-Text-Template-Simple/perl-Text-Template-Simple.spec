%global source0_hash f5f6678e5487de9ae88c87296269d8a7d43eff72b289de00a0ebd64495e119ac
Name:           perl-Text-Template-Simple
Version:        0.91
Release:        23%{?dist}
Summary:        Simple text template engine
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Template-Simple
Source0:        https://cpan.metacpan.org/authors/id/B/BU/BURAK/Text-Template-Simple-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Data::Dumper) >= 2.101
Requires:       perl(Devel::Size) >= 0.77
Requires:       perl(Digest::MD5)
Requires:       perl(Fcntl) >= 1.03
Requires:       perl(File::Find)
Requires:       perl(File::Spec) >= 0.6
Requires:       perl(File::stat)
Requires:       perl(IO::File)
Requires:       perl(IO::Handle)
Requires:       perl(Perl::Tidy)
Requires:       perl(Safe) >= 2.06
Requires:       perl(Symbol)
Requires:       perl(Text::Table) >= 1.107
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Spec\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Size)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Text::Table)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Template-Simple-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
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
