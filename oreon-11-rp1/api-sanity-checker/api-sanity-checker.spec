%global source0_hash 3c324fc1af24398ea2347d4e7265b2d58daa787c9d4d12dcac5908068ee152e4

%global commit ed74fbc05c007696b31db207d44af1372067ccf9

Name:           api-sanity-checker
Version:        1.98.7
Release:        25%{?dist}
Summary:        An automatic generator of basic unit tests for a shared C/C++ library

License:        GPL-2.0-only
URL:            http://forge.ispras.ru/projects/api-sanity-autotest
# https://github.com/lvc/api-sanity-checker/archive/%%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  abi-compliance-checker >= 1.98.7
BuildRequires:  coreutils
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
BuildRequires:  sed
Requires:       abi-compliance-checker >= 1.98.7
Requires:       binutils

%{?perl_default_filter}

%description
API Sanity Checker (ASC) is an automatic generator of basic unit tests for
shared C/C++ libraries. It is able to generate reasonable (in most, but
unfortunately not all, cases) input data for parameters and compose simple
("sanity" or "shallow"-quality) test cases for every function in the API through
the analysis of declarations in header files. The quality of generated tests
allows to check absence of critical errors in simple use cases. The tool is able
to build and execute generated tests and detect crashes (segfaults), aborts, all
kinds of emitted signals, non-zero program return code and program hanging. It
may be considered as a tool for out-of-the-box low-cost sanity checking
(fuzzing) of the library API or as a test development framework for initial
generation of templates for advanced tests. Also it supports universal format of
tests, random test generation mode, specialized data types and other useful
features.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
chmod -x LICENSE

%build
# Nothing to build.

%install
mkdir -p %{buildroot}%{_bindir}
perl ./Makefile.pl -install --destdir=%{buildroot} --prefix=%{_prefix}

# Create a man page.
mkdir -p %{buildroot}%{_mandir}/man1
help2man -h --info -o %{buildroot}%{_mandir}/man1/api-sanity-checker.1 \
         -N %{buildroot}%{_bindir}/api-sanity-checker
sed -i 's|API(1)|API-SANITY-CHECKER(1)|g' %{buildroot}%{_mandir}/man1/api-sanity-checker.1
sed -i '3,5d' %{buildroot}%{_mandir}/man1/api-sanity-checker.1

%files
%license LICENSE
%doc README doc/*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/%{name}

%changelog
%autochangelog
