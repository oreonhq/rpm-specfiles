%global source0_hash f5f6678e5487de9ae88c87296269d8a7d43eff72b289de00a0ebd64495e119ac

Name:           perl-Text-Template-Simple
Version:        0.91
Release:        23%{?dist}
Summary:        Simple text template engine
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Template-Simple
Source0:        https://cpan.metacpan.org/authors/id/B/BU/BURAK/Text-Template-Simple-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
# XXX: BuildRequires:  perl(File::Basename)
# XXX: BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec) >= 0.6
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Data::Dumper) >= 2.101
BuildRequires:  perl(Devel::Size) >= 0.77
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Fcntl) >= 1.03
BuildRequires:  perl(File::stat)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(overload)
# XXX: BuildRequires:  perl(Perl::Tidy)
BuildRequires:  perl(Safe) >= 2.06
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Text::Table) >= 1.107
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Temp) >= 0.12
BuildRequires:  perl(subs)
BuildRequires:  perl(Test::More) >= 0.40
BuildRequires:  perl(vars)
# Optional tests only
BuildRequires:  perl(Pod::Simple) >= 3.05
BuildRequires:  perl(Test::Pod) >= 1.26
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

%check
make test

%files
%license LICENSE
%doc Changes eg etc/flowchart.txt TODO
%{_bindir}/tts
%{_mandir}/man1/tts*
%{_mandir}/man3/Text*
%{perl_vendorlib}/Text*

%changelog
%autochangelog
