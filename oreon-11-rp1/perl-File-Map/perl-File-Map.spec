%global source0_hash c8e26933804e870d4aba92623b7886ac8b3c760c98fbfcd3bdc4b2305c464759

Name:           perl-File-Map
Version:        0.71
Release:        12%{?dist}
Summary:        Memory mapping made simple and safe
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/File-Map
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/File-Map-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-interpreter >= 0:5.008
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(PerlIO::Layers)
BuildRequires:  perl(Sub::Exporter::Progressive) >= 0.001005
BuildRequires:  perl(subs)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(open)
# Pod::Coverage::TrustPod 1.08 not used
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
# Test::Pod 1.41 not used
# Test::Pod::Coverage 1.08 not used
BuildRequires:  perl(Test::Warnings) >= 0.005
BuildRequires:  perl(threads)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(utf8)

%{?perl_default_filter}

%description
File::Map maps files or anonymous memory into perl variables.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-Map-%{version}
chmod -x examples/fastsearch.pl

%build
/usr/bin/perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes examples README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/File*
%{_mandir}/man3/*

%changelog
%autochangelog
