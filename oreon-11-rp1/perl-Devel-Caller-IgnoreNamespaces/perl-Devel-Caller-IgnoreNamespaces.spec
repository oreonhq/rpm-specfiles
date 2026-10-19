%global source0_hash 59a5ef3749632a875fe7e51cf1dd0f2ad3935b8cb45c41df6a6583a8fc628b1b
Name:           perl-Devel-Caller-IgnoreNamespaces
Version:        1.1
Release:        24%{?dist}
Summary:        Make available a function which can ignore name-spaces that you tell it about
License:        GPL-2.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-Caller-IgnoreNamespaces
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/Devel-Caller-IgnoreNamespaces-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(lib)
BuildRequires:  perl-generators
# /oreon:deps
%description
If your module should be ignored by caller(), just like Hook::LexWrap is
by its magic caller(), then call this module's register() subroutine
with its name.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-Caller-IgnoreNamespaces-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
