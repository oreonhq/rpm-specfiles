%global source0_hash ed1ce473ec869089e52016cfc8355165ebc37be9694ba4e829c7eb4ba1c45f8d
Name:		perl-Jcode
Version:	2.07
Release:        1%{?dist}
Summary:        Perl extension interface for converting Japanese text
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Jcode
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DANKOGAI/Jcode-%{version}.tar.gz
Patch0:		Jcode-2.07-UTF-8.patch
BuildArch:	noarch
Requires:	perl(Encode)
Requires:	perl(Encode::Alias)
Requires:	perl(Encode::Guess)
Requires:	perl(Encode::JP::H2Z)
Requires:	perl(MIME::Base64)
Requires:	perl(Scalar::Util)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Alias)
BuildRequires:  perl(Encode::Guess)
BuildRequires:  perl(Encode::JP::H2Z)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(diagnostics)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Jcode-%{version}

# Fix character encoding of pod file
%patch -P 0 -p1 -b .timestamp
touch --reference=Jcode/Nihongo.pod.timestamp Jcode/Nihongo.pod
rm Jcode/Nihongo.pod.timestamp

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
