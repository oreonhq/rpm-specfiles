%global source0_hash 229aa0e9f049efa760f3c2f6e61d9d539af43d8f764b50a6e03064b4729a35ff

# Run optional test
%bcond_without perl_Image_Sane_enables_optional_test

Name:           perl-Image-Sane
Version:        5
Release:        26%{?dist}
Summary:        Perl extension for the SANE (Scanner Access Now Easy) Project
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Image-Sane
Source0:        https://cpan.metacpan.org/authors/id/R/RA/RATCLIFFE/Image-Sane-%{version}.tar.gz
# Adapt to Perl 5.37.10, CPAN RT#148487
Patch0:         Image-Sane-5-Replace-deprecated-given-and-when-operators.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Config)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  pkgconfig(sane-backends) >= 1.0.19
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.8.5
BuildRequires:  perl(base)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(if)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(sigtrap)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Try::Tiny)
%if %{with perl_Image_Sane_enables_optional_test}
# Optional tests:
# ImageMagick for identify tool
BuildRequires:  ImageMagick
BuildRequires:  perl(Test::Pod) >= 1.00
# sane-backensds for scanimage tool
BuildRequires:  sane-backends
# sane-backends-drivers-scanners for "test" Sane driver
BuildRequires:  sane-backends-drivers-scanners
%endif

%description
These Perl bindings for the SANE (Scanner Access Now Easy) Project allow
you to access SANE-compatible scanners in a Perlish and object-oriented
way, freeing you from the casting and memory management in C, yet remaining
very close in spirit to original API.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
%if %{with perl_Image_Sane_enables_optional_test}
# ImageMagick for identify tool
Requires:       ImageMagick
# sane-backensds for scanimage tool
Requires:       sane-backends
# sane-backends-drivers-scanners for "test" Sane driver
Requires:       sane-backends-drivers-scanners
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Image-Sane-%{version}
# Remove author tests
rm t/91_critic.t
perl -i -ne 'print $_ unless m{\At/91_critic\.t}' MANIFEST
# Correct file permissions
chmod -x examples/*
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
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a examples t %{buildroot}%{_libexecdir}/%{name}
# Minimize examples
chmod +x %{buildroot}%{_libexecdir}/%{name}/examples/*
rm %{buildroot}%{_libexecdir}/%{name}/examples/scanadf-perl
# t/pod.t is usless on an empty ./blib
rm %{buildroot}%{_libexecdir}/%{name}/t/pod.t
# t/90_MANIFEST.t fails with empty ./lib
rm %{buildroot}%{_libexecdir}/%{name}/t/90_MANIFEST.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Many tests write into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes examples README
%dir %{perl_vendorarch}/auto/Image
%{perl_vendorarch}/auto/Image/Sane
%dir %{perl_vendorarch}/Image
%{perl_vendorarch}/Image/Sane{,.pm}
%{_mandir}/man3/Image::Sane.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
