%global source0_hash ad55abbd3d06a58ec3e134349a794b86670dd3c79fee9078c2fc1d35ceaebdfd

Name:           perl-Olson-Abbreviations
Version:        0.04
Release:        36%{?dist}
Summary:        Globally unique timezones abbreviation handling
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Olson-Abbreviations
Source0:        https://cpan.metacpan.org/authors/id/E/EC/ECARROLL/Olson-Abbreviations-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::ClassAttribute) >= 0.25
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
BuildRequires:  sed
Requires:       perl(MooseX::ClassAttribute) >= 0.25

%{?perl_default_filter}

%description
This module should help you with converting commonly used and often
ambigious olson abbreviations into TZ offset notation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Olson-Abbreviations-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
