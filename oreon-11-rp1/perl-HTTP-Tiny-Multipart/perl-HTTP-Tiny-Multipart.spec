%global source0_hash ed0d43d470797c236be7f83e414e31561560ef3f88fab1ec09def20d98c361d6

Name:           perl-HTTP-Tiny-Multipart
Version:        0.08
Release:        21%{?dist}
Summary:        Add post_multipart to HTTP::Tiny

License:        Artistic-2.0
URL:            https://search.cpan.org/dist/HTTP-Tiny-Multipart/
Source0:        https://www.cpan.org/modules/by-module/HTTP/HTTP-Tiny-Multipart-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >=  1.41
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n HTTP-Tiny-Multipart-%{version} -p 1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
%make_build test

%files
%doc Changes
%license CONTRIBUTORS LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
