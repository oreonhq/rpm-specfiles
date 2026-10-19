%global source0_hash 7bc86193e0c8973c7cb8f761ef51cb89d3bd8023b5f912af4c36a113a96454a8
Name:           perl-Catalyst-View-Mason
Version:        0.19
Release:        1%{?dist}
Summary:        Mason View Class
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-View-Mason
Source0:        https://cpan.metacpan.org/authors/id/J/JJ/JJNAPIORK/Catalyst-View-Mason-%{version}.tar.gz
Patch0:         Catalyst-View-Mason-0.19-Use-Capture-Tiny-IO-Capture.patch
BuildArch:      noarch
Requires:       perl(Catalyst) >= 5.50
Requires:       perl(Catalyst::View)
Requires:       perl(parent)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Helper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Mason)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::File)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(parent)
BuildRequires:  perl-generators
# /oreon:deps
%description
Want to use a Mason component in your Catalyst views? No problem!
Catalyst::View::Mason comes to the rescue.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-View-Mason-%{version}
%patch -P0 -p1

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
