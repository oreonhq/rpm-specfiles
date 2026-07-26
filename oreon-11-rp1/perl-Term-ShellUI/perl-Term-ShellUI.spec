%global source0_hash 3279c01c76227335eeff09032a40f4b02b285151b3576c04cacd15be05942bdb

Name:           perl-Term-ShellUI
Version:        0.92
Release:        34%{?dist}
Summary:        Perl module to implement a full-featured shell-like command line environment
License:        MIT
URL:            https://metacpan.org/release/Term-ShellUI
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRONSON/Term-ShellUI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Simple)

%description
Term::ShellUI is a Perl module, which tries to make every feature that
one would expect to see in a fully interactive shell trivial to implement. 
It uses the history and autocompletion features of Term::ReadLine to present
a sophisticated command-line interface to the user. You simply declare your
command set and let ShellUI take care of the heavy lifting.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Term-ShellUI-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
