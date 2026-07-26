%global source0_hash 6b50b1aab6ec6998a017f6403c2735b3bc1e1cf46187bd134d7eb6df3fc45144

Name:           perl-File-Modified
Version:        0.10
Release:        29%{?dist}
Summary:        Checks intelligently if files have changed
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Modified
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/File-Modified-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Digest::MD5)
# Tests only
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Digest::MD2)
BuildRequires:  perl(Digest::SHA1)
Requires:       perl(Digest::MD5)

%description
The Modified module is intended as a simple method for programs to detect
whether configuration files (or modules they rely on) have changed. There
are currently two methods of change detection implemented, mtime and MD5.
The MD5 method will fall back to use timestamps if the Digest::MD5 module
cannot be loaded.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-Modified-%{version}
find . -type f -exec chmod -c -x {} +
sed -i 's/\r//' README

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README example
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
