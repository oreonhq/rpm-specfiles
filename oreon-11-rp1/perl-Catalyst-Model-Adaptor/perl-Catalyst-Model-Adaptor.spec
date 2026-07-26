%global source0_hash 9312eb4c022ae2990d394c4f4902683b853d5456a40004dbd1829640f913cbba

Name:           perl-Catalyst-Model-Adaptor
Version:        0.10
Release:        41%{?dist}
Summary:        Use a plain class as a Catalyst model
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Model-Adaptor
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Model-Adaptor-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Catalyst::Runtime)
BuildRequires:  perl(inc::Module::Install) >= 0.91
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::ReadmeFromPod)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(ok)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::WWW::Mechanize::Catalyst)

%{?perl_default_filter}

%description
The idea is that you don't want your Catalyst model to be anything other
than a line or two of glue. Using this module ensures that your Model
classes are separate from your application and therefore are well-
abstracted, reusable, and easily testable.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Model-Adaptor-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
