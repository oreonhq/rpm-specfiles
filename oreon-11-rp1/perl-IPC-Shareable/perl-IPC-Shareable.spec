%global source0_hash 11ed7bedefe1e331f7461a3c6177fe18f2ea0a2977b32fc53a7249b6b616b663

Name:           perl-IPC-Shareable
Version:        1.12
Release:        12%{?dist}
Summary:        Share Perl variables between processes

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/IPC-Shareable
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSOUTH/IPC-Shareable-%{version}.tar.gz

BuildArch:      noarch
# Module Build
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.72
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IPC::Semaphore)
BuildRequires:  perl(IPC::SysV)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable) >= 0.607
BuildRequires:  perl(strict)
BuildRequires:  perl(String::CRC32)
BuildRequires:  perl(vars)
# Test Suite
BuildRequires:  perl(Mock::Sub)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::SharedFork) >= 0.35
# (no additional requirements)
# Runtime
Requires:       perl(Carp)
Requires:       perl(Data::Dumper)

%description
IPC::Shareable allows you to tie a variable to shared memory making it
easy to share the contents of that variable with other Perl processes.
Scalars, arrays, and hashes can be tied.  The variable being tied may
contain arbitrarily complex data structures - including references to
arrays, hashes of hashes, etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IPC-Shareable-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} $RPM_BUILD_ROOT

%check
make test CI_TESTING=1

%files
%doc COPYING CREDITS DISCLAIMER README
%{perl_vendorlib}/IPC/
%{_mandir}/man3/IPC::Shareable.3pm*
%{_mandir}/man3/IPC::Shareable::SharedMem.3pm*

%changelog
%autochangelog
