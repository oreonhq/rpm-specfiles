%global source0_hash d347b2292ffc6332e5bac1aece73796cb75c1eb4a79b1a4de9c54ab08f1c2565

Name:           perl-Exporter-Easy
Version:        0.18
Release:        26%{?dist}
Summary:        Takes the drudgery out of Exporting symbols
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Exporter-Easy
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Exporter-Easy-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter >= 0:5.006
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)

%{?perl_default_filter}

%description
Exporter::Easy makes using Exporter easy. In its simplest case, it allows
you to drop the boilerplate code that comes with using Exporter, so more
complicated situations where you use tags to build lists and more tags
become easy.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Exporter-Easy-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README TODO
%license LICENSE
%{perl_vendorlib}/Exporter*
%{_mandir}/man3/Exporter*

%changelog
%autochangelog
