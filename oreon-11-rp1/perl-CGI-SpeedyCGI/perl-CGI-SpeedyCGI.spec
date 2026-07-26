%global source0_hash 9021a5c6d8ed205422f091209addf7d1be27222adbcbd17bc52fbc527bcc6f98

# Module Magic Number
%{!?_httpd_mmn: %global _httpd_mmn %(cat %{_includedir}/httpd/.mmn 2> /dev/null || echo 0-0)}

%global pkgname CGI-SpeedyCGI

Summary:        Speed up perl scripts by running them persistently
Name:           perl-CGI-SpeedyCGI
Version:        2.22
Release:        60%{?dist}
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/%{pkgname}
Source0:        https://cpan.metacpan.org/modules/by-authors/id/H/HO/HORROCKS/%{pkgname}-%{version}.tar.gz
Source1:        10-speedycgi.conf
Source2:        example.conf
Patch0:         perl-CGI-SpeedyCGI-2.22-documentation.patch
Patch1:         perl-CGI-SpeedyCGI-2.22-empty_param.patch
Patch2:         perl-CGI-SpeedyCGI-2.22-strerror.patch
Patch3:         perl-CGI-SpeedyCGI-2.22-brigade_foreach.patch
Patch4:         perl-CGI-SpeedyCGI-2.22-exit_messages.patch
Patch5:         perl-CGI-SpeedyCGI-2.22-perl_510.patch
Patch6:         perl-CGI-SpeedyCGI-2.22-c99_inline.patch
Patch7:         CGI-SpeedyCGI-2.22-Fix-building-on-Perl-without-dot-in-INC.patch
# Fix building with GCC 10, bug #1793916, CPAN RT#131596
Patch8:         CGI-SpeedyCGI-2.22-Fix-building-with-GCC-10.patch
Patch9:         perl-CGI-SpeedyCGI-c99.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-interpreter >= 5.8.0
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(strict)
BuildRequires:  sed

%description
SpeedyCGI is a way to run perl scripts persistently, which can make
them run much more quickly. After the script is initially run, instead
of exiting, the perl interpreter is kept running. During subsequent
runs, this interpreter is used to handle new executions instead of
starting a new perl interpreter each time. It is a very fast frontend
program, written in C, is executed for each request.

%package -n mod_speedycgi
Summary:        SpeedyCGI module for the Apache HTTP Server
BuildRequires:  httpd-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}, httpd >= 2.0.40
Requires:       httpd-mmn = %{_httpd_mmn}

%description -n mod_speedycgi
The SpeedyCGI module for the Apache HTTP Server. It can be used to run
perl scripts for web application persistently to make them more quickly.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}
cp -pf %{SOURCE2} .

%build
sed -i 's@apxs -@%{_httpd_apxs} -@g' Makefile.PL src/SpeedyMake.pl \
  mod_speedycgi/t/ModTest.pm mod_speedycgi/t/mod_perl.t
sed -i 's@APXS=apxs@APXS=%{_httpd_apxs}@g' mod_speedycgi/Makefile.tmpl

echo yes | perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
make OPTIMIZE="$RPM_OPT_FLAGS -Wno-incompatible-pointer-types" # doesn't understand %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

%if 0%{?rhel} && 0%{?rhel} <= 7
find $RPM_BUILD_ROOT \( -name perllocal.pod -o -name .packlist \) -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
%endif
chmod -R u+w $RPM_BUILD_ROOT/*

install -D -p -m 0755 mod_speedycgi2/mod_speedycgi.so $RPM_BUILD_ROOT%{_httpd_moddir}/mod_speedycgi.so
install -D -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_httpd_modconfdir}/10-speedycgi.conf

%files
%license COPYING
%doc Changes README docs/*
%{_bindir}/speedy*
%{perl_vendorlib}/CGI

%files -n mod_speedycgi
%doc example.conf
%{_httpd_moddir}/mod_speedycgi.so
%config(noreplace) %{_httpd_modconfdir}/*.conf

%changelog
%autochangelog
