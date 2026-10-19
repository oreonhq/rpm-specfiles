%global source0_hash 4bd29a17f0c2c792d12c1005b3c276f2ab0fae39c00859ae1741d7941846a488
Summary:        Line wrapping with support for several locale setups
Name:           perl-Text-WrapI18N
Version:        0.06
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-WrapI18N
Source0:        https://cpan.metacpan.org/authors/id/K/KU/KUBOTA/Text-WrapI18N-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(Text::CharWidth)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a module which intends to substitute Text::Wrap,
which supports internationalized texts including:
 - multi-byte encodings such as UTF-8, EUC-JP, EUC-KR, GB2312, and Big5,
 - full width characters like east Asian characters which appear in
   UTF-8, EUC-JP, EUC-KR, GB2312, Big5, and so on,
 - combining characters like diacritical marks which appear in UTF-8,
   ISO-8859-11 (aka TIS-620), and so on, and
 - languages which don't use white spaces between words, like Chinese
   and Japanese.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Text-WrapI18N-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.06-53
- Prepare for Oreon 11 (RP1)
