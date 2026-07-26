%global source0_hash cbb72bc34b2b952bdffa244d90f0ed3566bc2b9026d76d25d5bd1d8f0314a059

Name:           perl-Perl6-Export-Attrs
Summary:        Perl 6 'is export(...)' trait as a Perl 5 attribute
Version:        0.000006
Release:        24%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl6-Export-Attrs
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/Perl6-Export-Attrs-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl(Attribute::Handlers)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

%{?perl_default_filter}

%description
Implements a Perl 5 native version of what the Perl 6 symbol export
mechanism will look like.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Perl6-Export-Attrs-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/Perl6
%{_mandir}/man3/Perl6::Export::Attrs.3pm*

%changelog
%autochangelog
