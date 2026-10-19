%global source0_hash 06eb47db74d594d2256cf4794f2c259e9f3f54b9f61b900544e6e1d879e244f5
Name:           perl-MIME-Lite
Version:        3.038
Release:        1%{?dist}
Summary:        MIME::Lite - low-calorie MIME generator
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MIME-Lite
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/MIME-Lite-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Email::Date::Format) >= 1.000
Recommends:     perl(MIME::Types) >= 1.28
Recommends:     perl(Mail::Address) >= 1.62
%{?perl_default_filter}
Provides:       perl(MIME::Lite)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Email::Date::Format)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(MIME::Types)
BuildRequires:  perl(Net::SMTP)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
MIME::Lite is intended as a simple, standalone module for generating (not
parsing!) MIME messages... Specifically, it allows you to output a simple,
decent single- or multi-part message with text or binary attachments.  It does
not require that you have the Mail:: or MIME:: modules installed.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MIME-Lite-%{version}
sed -i 's/\r//' examples/*
sed -i 's/\r//' contrib/*
chmod a-x examples/* contrib/*
# Help generators to recognize Perl scripts
for F in $(find t/ -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} +
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cp -a testin %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-MIME-Lite-tests -f %{oreon_filedir}/perl-MIME-Lite-tests.list

%changelog

%autochangelog
