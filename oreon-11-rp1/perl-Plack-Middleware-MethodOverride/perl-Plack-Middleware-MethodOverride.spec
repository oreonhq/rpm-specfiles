%global source0_hash dbfb5a2efb48bfeb01cb3ae1e1c677e155dc7bfe210c7e7f221bae3cb6aab5f1

Name:           perl-Plack-Middleware-MethodOverride
Version:        0.20
Release:        25%{?dist}
Summary:        Override REST methods to Plack apps via POST
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Plack-Middleware-MethodOverride
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Plack-Middleware-MethodOverride-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Plack) >= 0.9929
BuildRequires:  perl(Plack::Middleware)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Plack::Util::Accessor)
BuildRequires:  perl(Test::More) >= 0.70
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(URI)
BuildRequires:  perl(blib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
This Plack middleware allows your apps to override any HTTP method over POST.
Specifically, you can provide a query parameter named "x-tunneled-method"
or a header named "x-http-method-override" (as used by Google's APIs).
Either way, the overriding works only via POST requests, not GET.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Plack-Middleware-MethodOverride-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Plack*
%{_mandir}/man3/Plack*

%changelog
%autochangelog
