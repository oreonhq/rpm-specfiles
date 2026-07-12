%global source0_hash 04eae3e0a124eb2479ebd9a167319f4db4d920be65e59e16ae0cd6cf7e59e6a5

# Perform optinal tests
%bcond_without perl_meta_enables_optional_test

Name:           perl-meta
Version:        0.015
Release:        2%{?dist}
Summary:        Meta-programming API
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/meta
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/meta-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(experimental)
BuildRequires:  perl(feature)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::V0)
%if %{with perl_meta_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
%endif

Provides:       perl(meta)
%description
This package provides an API for Perl meta programming; that is, allowing code
to inspect or manipulate parts of its own program structure. Parts of the perl
interpreter itself can be accessed by means of "meta"-objects provided by this
package. Methods on these objects allow inspection of details, as well as
creating new items or removing existing ones.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n meta-%{version}
%if !%{with perl_meta_enables_optional_test}
rm t/99pod.t
perl -i -ne 'print $_ unless m{t/99pod\.t}' MANIFEST
%endif
chmod +x t/*.t

%build
perl Build.PL --installdirs=vendor --optimize='%{optflags}'
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_meta_enables_optional_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/99pod.t
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/meta
%{perl_vendorarch}/meta.pm
%{_mandir}/man3/meta.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
