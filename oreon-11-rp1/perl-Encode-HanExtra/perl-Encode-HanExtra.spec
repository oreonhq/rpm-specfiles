%global source0_hash 1fd4b06cada70858003af153f94c863b3b95f2e3d03ba18d0451a81d51db443a

Name:           perl-Encode-HanExtra
Version:        0.23
Release:        48%{?dist}
Summary:        Extra sets of Chinese encodings
License:        MIT
URL:            https://metacpan.org/release/Encode-HanExtra
Source0:        https://cpan.metacpan.org/modules/by-module/Encode/Encode-HanExtra-%{version}.tar.gz
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-Encode-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::External)
BuildRequires:  perl(Module::Install::Makefile)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Encoding)
BuildRequires:  perl(vars)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
Perl 5.7.3 and later ships with an adequate set of Chinese encodings,
including the commonly used CP950, CP936 (also known as GBK), Big5 (alias
for Big5-Eten), Big5-HKSCS, EUC-CN, HZ, and ISO-IR-165.
However, the numbers of Chinese encodings are staggering, and a complete
coverage will easily increase the size of perl distribution by several
megabytes; hence, this CPAN module tries to provide the rest of them.
If you are using Perl 5.8 or later, Encode::CN and Encode::TW will
automatically load the extra encodings for you, so there's no need to
explicitly write use Encode::HanExtra if you are using one of them already.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Encode-HanExtra-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
# Remove the next line from noarch packages (unneeded)
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/
%{_mandir}/man3/*

%changelog
%autochangelog
