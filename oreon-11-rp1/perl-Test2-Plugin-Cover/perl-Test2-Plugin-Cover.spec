%global source0_hash ce9e798a42417f784cb537baeceb3a5cfa65a0d8def4d386642661c390dfa01f

Name:           perl-Test2-Plugin-Cover
%global cpan_version 0.000027
Version:        0.0.27
Release:        16%{?dist}
Summary:        Collect minimal file coverage data
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test2-Plugin-Cover
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test2-Plugin-Cover-%{cpan_version}.tar.gz
# Adjust line numbers after adding shebangs, no suitable for upstream
Patch0:         Test2-Plugin-Cover-0.000027-Adapt-tests-to-added-shebangs.patch
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Path::Tiny) >= 0.048
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test2::API) >= 1.302166
BuildRequires:  perl(Test2::EventFacet) >= 1.302166
BuildRequires:  perl(Test2::Util::HashBase)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Test2::V0) >= 0.000130
Requires:       perl(Path::Tiny) >= 0.048
Requires:       perl(Test2::API) >= 1.302166
Requires:       perl(Test2::EventFacet) >= 1.302166

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Path::Tiny|Test2::API|Test2::V0)\\)$
# Remove private modules
%global __requires_exclude %{__requires_exclude}|^perl\\((Fake.|OpenXXX)\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((Fake.|OpenXXX)\\)

%description
This Test2 plugin will collect minimal file coverage data, and will do so with
a minimal performance impact.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Path::Tiny) >= 0.048
Requires:       perl(Test2::V0) >= 0.000130

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Test2-Plugin-Cover-%{cpan_version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Test2*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
