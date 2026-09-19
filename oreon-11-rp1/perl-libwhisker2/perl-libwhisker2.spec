%global source0_hash f45a1cf2ad2637b29dd1b13d7221ea12e3923ea09d107ced446400f19070a42f

%define real_name libwhisker2
Name:           perl-%{real_name}
Version:        2.5
Release:        44%{?dist}
Summary:        Perl module geared specifically for HTTP testing
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.wiretrip.net/rfp/lw.asp
Source0:        http://downloads.sourceforge.net/whisker/%{real_name}-%{version}.tar.gz
#install to vendorlib, not sitelib
Patch0:         %{real_name}-2.4-vendorlib.patch
#include libwhisker1 compatibility bridge
Patch1:         %{real_name}-2.4-lw1bridge.patch
# Perl 5.18 compatibility
Patch2:         %{real_name}-2.5-Editing-iterated-hash-is-undefined.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(MIME::Base64)
# strict not used at tests
# vars not used at tests
# Tests:
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(Net::SSLeay)
BuildRequires:  perl(Test::Simple)
# All SSL and network related packages are optional at run time.
Recommends:     perl(MIME::Base64)
Obsoletes:      perl-libwhisker <= 1.8
Provides:       perl-libwhisker = %{version}-%{release}

%description
Libwhisker is a Perl library useful for HTTP testing scripts.  It
contains a pure-Perl implementation of functionality found in the LWP,
URI, Digest::MD5, Digest::MD4, Data::Dumper, Authen::NTLM, HTML::Parser,
HTML::FormParser, CGI::Upload, MIME::Base64, and GetOpt::Std modules.
Libwhisker is designed to be portable (a single perl file), fast (general
benchmarks show libwhisker is faster than LWP), and flexible (great care
was taken to ensure the library does exactly what you want to do, even
if it means breaking the protocol).

%package doc
Summary:        Development documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
This package provides examples how to use LW(2) Perl module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{real_name}-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
mv compat/{lw,LW}.pm
# Fix EOLs
for F in CHANGES KNOWNBUGS LICENSE README docs/* scripts/*; do
    sed -e 's/\r$//' "$F" > "${F}.new"
    touch -r "$F"{,.new}
    mv "$F"{.new,}
done
# Fix interpreter path
for F in scripts/*.pl; do
    sed -e '1 s|^#!perl|#!/usr/bin/perl|' "$F" > "${F}.new"
    chmod a+x "${F}.new"
    touch -r "$F"{,.new}
    mv "$F"{.new,}
done

%build
%{make_build}

%install
# Create directories, not created by Makefile.pl
mkdir -p $RPM_BUILD_ROOT%{perl_vendorlib}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3

%{make_install}

# Install documentation
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a docs scripts $RPM_BUILD_ROOT%{_datadir}/%{name}

#fix permissions
chmod 0644 $RPM_BUILD_ROOT/%{perl_vendorlib}/*

%check
cd t 
perl ./test.pl

%files
%license LICENSE
%doc CHANGES KNOWNBUGS README
%{perl_vendorlib}/*
%{_mandir}/man?/*

%files doc
%{_datadir}/%{name}

%changelog
%autochangelog
