%global source0_hash a072b5011505cf4fa663a764c9969783941e2e3fda28c90cc2d4fff30f6a2449

Name:           perl-IPC-Filter
Version:        0.005
Release:        24%{?dist}
Summary:        Filter data through an external process
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IPC-Filter
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/IPC-Filter-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Errno) >= 1.00
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::Handle) >= 1.12
BuildRequires:  perl(IO::Poll) >= 0.01
BuildRequires:  perl(IPC::Open3) >= 1.01
BuildRequires:  perl(IPC::Signal) >= 1.00
BuildRequires:  perl(parent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Symbol)
# Tests
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)

%{?perl_default_filter}

%description
The filter function provided by this module passes data through an external
command, thus providing filtering in non-pipeline situations.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IPC-Filter-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
