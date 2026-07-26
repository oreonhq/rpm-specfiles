%global source0_hash 946bf8a2f856e466ebdc06113d0258e277abdc701ad542aa4b5672d8d8dc3b45

Name:           perl-Template-Alloy
Version:        1.022
Release:        15%{?dist}
Summary:        Templating tool supporting multiple markup formats 
# see lib/Template/Alloy.pod
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Template-Alloy
Source0:        https://cpan.metacpan.org/authors/id/R/RH/RHANDOM/Template-Alloy-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5) >= 1
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(JSON)
BuildRequires:  perl(overload)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Optional run-time:
BuildRequires:  perl(Encode)
BuildRequires:  perl(Scalar::Util)
# Tests:
BuildRequires:  perl(Taint::Runtime)
BuildRequires:  perl(Template::Filters)
BuildRequires:  perl(Template::Stash)
BuildRequires:  perl(Template::View)
BuildRequires:  perl(Test::More) 
# Optional tests:
BuildRequires:  perl(utf8)
Requires:       perl(Carp)
Requires:       perl(Data::Dumper)
Requires:       perl(Digest::MD5) >= 1
Requires:       perl(File::Path)
Requires:       perl(JSON)
Requires:       perl(overload)
Requires:       perl(Storable)

%{?perl_default_filter}

%description
"An alloy is a homogeneous mixture of two or more elements"
(http://en.wikipedia.org/wiki/Alloy).

Template::Alloy represents the mixing of features and capabilities from all of
the major mini-language based template systems (support for non-mini-language
based systems will happen eventually).  With Template::Alloy you can use your
favorite template interface and syntax and get features from each of the other
major template systems.  And Template::Alloy is fast - whether you're using
mod_perl, CGI, or running from the command line.  There is even
Template::Alloy::XS for getting a little more speed when that is necessary.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(Encode)
Requires:       perl(File::Path)
Requires:       perl(Taint::Runtime)
Requires:       perl(Template::Filters)
Requires:       perl(Template::Stash)
Requires:       perl(Template::View)
Requires:       perl(utf8)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Template-Alloy-%{version}
find . -type f -exec chmod -c -x {} +
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# t/02_cache.t writes into PWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/t "$DIR"
pushd "$DIR"
unset REQUEST_METHOD USE_TT
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset REQUEST_METHOD USE_TT
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README samples/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
