%global source0_hash f45a1cf2ad2637b29dd1b13d7221ea12e3923ea09d107ced446400f19070a42f
%define real_name libwhisker2
Name:           perl-%{real_name}
Version:        2.5
Release:        44%{?dist}
Summary:        Perl module geared specifically for HTTP testing
License:        LicenseRef-Callaway-BSD
URL:            http://www.wiretrip.net/rfp/lw.asp
Source0:        http://downloads.sourceforge.net/whisker/%{real_name}-%{version}.tar.gz
Patch0:         %{real_name}-2.4-vendorlib.patch
Patch1:         %{real_name}-2.4-lw1bridge.patch
Patch2:         %{real_name}-2.5-Editing-iterated-hash-is-undefined.patch
BuildArch:      noarch
Recommends:     perl(MIME::Base64)
Obsoletes:      perl-libwhisker <= 1.8
Provides:       perl-libwhisker = %{version}-%{release}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Net::SSLeay)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
mkdir -p $RPM_BUILD_ROOT%{perl_vendorlib}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3
%{make_install}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a docs scripts $RPM_BUILD_ROOT%{_datadir}/%{name}
chmod 0644 $RPM_BUILD_ROOT/%{perl_vendorlib}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

cd t 
perl ./test.pl
%files -f %{oreon_filedir}/main.list
%files -n perl-libwhisker2-doc -f %{oreon_filedir}/perl-libwhisker2-doc.list

%changelog

%autochangelog
