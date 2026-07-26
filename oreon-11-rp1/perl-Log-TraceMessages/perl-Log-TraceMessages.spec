%global source0_hash 343ab47c1d69200df6d37bc1dd0127132e6f0a469b77ee6b71eca1146ce6cf8f

Name:           perl-Log-TraceMessages
Version:        1.4
Release:        50%{?dist}
Summary:        Perl extension for trace messages used in debugging

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Log-TraceMessages
Source0:        https://cpan.metacpan.org/modules/by-module/Log/Log-TraceMessages-%{version}.tar.gz
# Restore compatibility with Perl 5.26.0, CPAN RT#115089
Patch0:         Log-TraceMessages-1.4-Use-File-Temp-tempfile-instead-of-POSIX-tmpnam.patch

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTML::FromText) >= 1.004

%{?perl_default_filter}

%description
This module is a better way of putting 'hello there' trace messages in
your code.  It lets you turn tracing on and off without commenting out
trace statements, and provides other useful things like HTML-ified
trace messages for CGI scripts and an easy way to trace out data
structures using Data::Dumper.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Log-TraceMessages-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Log/
%{perl_vendorlib}/auto/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
