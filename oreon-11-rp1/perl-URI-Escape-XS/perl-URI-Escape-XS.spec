%global source0_hash c39ac50c6c2b831ae4bf08692e6ca5d4a3f9c57dc4d7f9c4cb0663e2c86c2759
Name:           perl-URI-Escape-XS
Version:        0.14
Release:        1%{?dist}
Summary:        Drop-In replacement for URI::Escape
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/URI-Escape-XS
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DANKOGAI/URI-Escape-XS-%{version}.tar.gz
Requires:       perl(Carp)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a drop-in replacement for the URI::Escape module. Since it
uses XS, it is really fast except for uri_escape("noop").

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n URI-Escape-XS-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1
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
