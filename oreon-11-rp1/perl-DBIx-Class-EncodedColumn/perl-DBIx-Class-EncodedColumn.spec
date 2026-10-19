%global source0_hash f66a76aa55fdd8446521c663b3485558c0edbcfdf20838536cec2062f4e54832
Name:           perl-DBIx-Class-EncodedColumn
%global cpan_version 0.11
Version:        0.11000
Release:        3%{?dist}
Summary:        Automatically encode columns
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBIx-Class-EncodedColumn
Source0:        https://cpan.metacpan.org/authors/id/W/WR/WREIS/DBIx-Class-EncodedColumn-%{cpan_version}.tar.gz
BuildArch:      noarch
Requires:       perl(Digest::SHA)
%{?perl_default_filter}
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DigestTest::Schema.*\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Config)
BuildRequires:  perl(Crypt::Eksblowfish::Bcrypt)
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Crypt::URandom::Token)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(DBIx::Class::TimeStamp)
BuildRequires:  perl(DateTime::Format::SQLite)
BuildRequires:  perl(Digest)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Dir::Self)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This DBIx::Class component can be used to automatically encode a column's

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(DBD::SQLite)
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".
contents whenever the value of that column is set.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-Class-EncodedColumn-%{cpan_version}
# Crypt::OpenPGP is not available in Fedora.
# It cannot be packaged because its dependency, Crypt::RIPEMD160,
# cannot be packaged.  See rhbz#182235.
rm lib/DBIx/Class/EncodedColumn/Crypt/OpenPGP.pm

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -rf %{buildroot}%{_libexecdir}/%{name}/t/author*
rm %{buildroot}%{_libexecdir}/%{name}/t/open_pgp.t
rm %{buildroot}%{_libexecdir}/%{name}/t/whirlpool*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset AUTHOR_TESTING
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-DBIx-Class-EncodedColumn-tests -f %{oreon_filedir}/perl-DBIx-Class-EncodedColumn-tests.list

%changelog

%autochangelog
