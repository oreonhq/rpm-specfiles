%global source0_hash 5c515707a5433796a5697b118ddbf1f216d13c5cd52f2b64292e76f7d9b7e8f1

Name:           perl-Hash-FieldHash
Version:        0.15
Release:        33%{?dist}
Summary:        Lightweight field hash implementation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Hash-FieldHash
Source0:        https://cpan.metacpan.org/modules/by-module/Hash/Hash-FieldHash-%{version}.tar.gz
Patch0:         Hash-FieldHash-0.15-Fix-building-on-Perl-without-dot-in-INC.patch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Devel::PPPort) >= 3.19
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::ParseXS) >= 2.21
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build) >= 0.40.05
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Module Runtime
BuildRequires:  perl(Exporter)
BuildRequires:  perl(parent) >= 0.221
BuildRequires:  perl(strict)
BuildRequires:  perl(XSLoader) >= 0.02
# Test Suite
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(if)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More) >= 0.62
BuildRequires:  perl(threads)
# Optional Tests
BuildRequires:  perl(Hash::Util::FieldHash)
BuildRequires:  perl(Test::LeakTrace) >= 0.07
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::Synopsis)
# Dependencies
# (none)

# Avoid provides from private shared objects
%{?perl_default_filter}

%description
Hash::FieldHash provides the field hash mechanism, which supports the inside-
out technique.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Hash-FieldHash-%{version}

# Fix building on Perl without '.' in @INC
%patch -P 0 -p1

%build
RELEASE_TESTING=1 perl Build.PL --installdirs=vendor --optimize="%{optflags}"
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%license LICENSE
%doc Changes README.md benchmark/ example/
%{perl_vendorarch}/auto/Hash/
%{perl_vendorarch}/Hash/
%{_mandir}/man3/Hash::FieldHash.3*

%changelog
%autochangelog
