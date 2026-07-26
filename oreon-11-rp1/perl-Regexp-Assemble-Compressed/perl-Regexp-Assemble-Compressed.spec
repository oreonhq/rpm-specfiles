%global source0_hash d568d0d4937887ee5c5b9a4393c382e4d287e7cab19d3c4a0e381e0fe051ec38

Name:           perl-Regexp-Assemble-Compressed
Summary:        Assemble more compressed Regular Expression
Version:        0.02
Release:        38%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Regexp-Assemble-Compressed
Source0:        https://cpan.metacpan.org/authors/id/T/TA/TANIGUCHI/Regexp-Assemble-Compressed-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Include)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Regexp::Assemble)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
Regexp::Assemble::Compressed is a subclass of Regexp::Assemble. It
assembles more compressed regular expressions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Regexp-Assemble-Compressed-%{version}
# Remove bundled modules
rm -r ./inc/*
sed -i -e '/^inc\//d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Regexp
%{_mandir}/man3/Regexp::Assemble::Compressed.3pm*

%changelog
%autochangelog
