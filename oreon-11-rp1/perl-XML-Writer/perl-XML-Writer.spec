%global source0_hash 73c8f5bd3ecf2b350f4adae6d6676d52e08ecc2d7df4a9f089fa68360d400d1f
Name:           perl-XML-Writer
Version:        0.900
Release:        18%{?dist}
Summary:        A simple Perl module for writing XML documents
License:        LicenseRef-Fedora-UltraPermissive
URL:            https://metacpan.org/release/XML-Writer
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JOSEPHW/XML-Writer-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(XML::Writer)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Algorithm::Diff)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Errno)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
XML::Writer is a simple Perl module for writing XML documents: it
takes care of constructing markup and escaping data correctly, and by
default, it also performs a significant amount of well-formedness
checking on the output, to make certain (for example) that start and
end tags match, that there is exactly one document element, and that
there are not duplicate attribute names.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Recommends:     perl(IO::Scalar)
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n XML-Writer-%{version}
find examples -type f -exec chmod -x {} +
# Remove executable flag from library
chmod -x Writer.pm
# Help generators to recognize Perl scripts
perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "t/selfcontained_output.t"
chmod +x "t/selfcontained_output.t"

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}/%{_libexecdir}/%{name}/t/pod-coverage.t
rm %{buildroot}/%{_libexecdir}/%{name}/t/pod.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-XML-Writer-tests -f %{oreon_filedir}/perl-XML-Writer-tests.list

%changelog

%autochangelog
