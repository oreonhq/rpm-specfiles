%global source0_hash 559af28d5310302ca63599e59f0dd76c3247b4523449c2745c5ef159968051a1

Name:           perl-MCE
Version:        1.902
Release:        2%{?dist}
Summary:        Many-core Engine for Perl providing parallel processing capabilities
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MCE
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARIOROY/MCE-%{version}.tar.gz
Patch0:         MCE-1.818-Fix-sharp-bang-line.patch
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(if)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sereal) >= 3.015
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable) >= 2.04
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)
# Script Runtime
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(lib)
BuildRequires:  perl(vars)
# Test Suite
BuildRequires:  perl(open)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(utf8)
# Dependencies
Requires:       perl(File::Path)
Requires:       perl(POSIX)
Requires:       perl(Sereal) >= 3.015
Requires:       perl(Storable) >= 2.04
Requires:       perl(threads::shared)

Provides:       perl(MCE::Grep)
Provides:       perl(MCE)
%description
Many-core Engine (MCE) for Perl helps enable a new level of performance by
maximizing all available cores. MCE spawns a pool of workers and therefore
does not fork a new process per each element of data. Instead, MCE follows
a bank queuing model. Imagine the line being the data and bank-tellers the
parallel workers. MCE enhances that model by adding the ability to chunk
the next n elements from the input stream to the next available worker.

%package tools
Summary:        Many-core Engine command line tools
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       grep, gzip

%description tools
This package delivers command line tools like mce_grep(1) that utilize
the Many-core Engine (MCE) Perl library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MCE-%{version}

# Fix sharp-bang line
%patch -P 0

%build
MCE_INSTALL_TOOLS=1 perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

# Add symlinks for grep variants
ln -s mce_grep %{buildroot}%{_bindir}/mce_egrep
ln -s mce_grep %{buildroot}%{_bindir}/mce_fgrep
ln -s mce_grep %{buildroot}%{_bindir}/mce_zgrep
ln -s mce_grep %{buildroot}%{_bindir}/mce_zegrep
ln -s mce_grep %{buildroot}%{_bindir}/mce_zfgrep

%check
make test

%files
%license LICENSE Copying
%doc Changes Credits README.md
%doc %{perl_vendorlib}/MCE.pod
%doc %{perl_vendorlib}/MCE/Core.pod
%doc %{perl_vendorlib}/MCE/Examples.pod
%dir %{perl_vendorlib}/MCE/
%dir %{perl_vendorlib}/MCE/Core/
%{perl_vendorlib}/MCE.pm
%{perl_vendorlib}/MCE/Candy.pm
%{perl_vendorlib}/MCE/Channel/
%{perl_vendorlib}/MCE/Channel.pm
%{perl_vendorlib}/MCE/Child.pm
%{perl_vendorlib}/MCE/Core.pm
%{perl_vendorlib}/MCE/Core/Input/
%{perl_vendorlib}/MCE/Core/Manager.pm
%{perl_vendorlib}/MCE/Core/Validation.pm
%{perl_vendorlib}/MCE/Core/Worker.pm
%{perl_vendorlib}/MCE/Flow.pm
%{perl_vendorlib}/MCE/Grep.pm
%{perl_vendorlib}/MCE/Loop.pm
%{perl_vendorlib}/MCE/Map.pm
%{perl_vendorlib}/MCE/Mutex.pm
%{perl_vendorlib}/MCE/Mutex/
%{perl_vendorlib}/MCE/Queue.pm
%{perl_vendorlib}/MCE/Relay.pm
%{perl_vendorlib}/MCE/Signal.pm
%{perl_vendorlib}/MCE/Step.pm
%{perl_vendorlib}/MCE/Stream.pm
%{perl_vendorlib}/MCE/Subs.pm
%{perl_vendorlib}/MCE/Util.pm
%{_mandir}/man3/MCE.3*
%{_mandir}/man3/MCE::Candy.3*
%{_mandir}/man3/MCE::Channel.3*
%{_mandir}/man3/MCE::Channel::Mutex.3*
%{_mandir}/man3/MCE::Channel::MutexFast.3*
%{_mandir}/man3/MCE::Channel::Simple.3*
%{_mandir}/man3/MCE::Channel::SimpleFast.3*
%{_mandir}/man3/MCE::Channel::Threads.3*
%{_mandir}/man3/MCE::Channel::ThreadsFast.3*
%{_mandir}/man3/MCE::Child.3*
%{_mandir}/man3/MCE::Core.3*
%{_mandir}/man3/MCE::Core::Input::Generator.3*
%{_mandir}/man3/MCE::Core::Input::Handle.3*
%{_mandir}/man3/MCE::Core::Input::Iterator.3*
%{_mandir}/man3/MCE::Core::Input::Request.3*
%{_mandir}/man3/MCE::Core::Input::Sequence.3*
%{_mandir}/man3/MCE::Core::Manager.3*
%{_mandir}/man3/MCE::Core::Validation.3*
%{_mandir}/man3/MCE::Core::Worker.3*
%{_mandir}/man3/MCE::Examples.3*
%{_mandir}/man3/MCE::Flow.3*
%{_mandir}/man3/MCE::Grep.3*
%{_mandir}/man3/MCE::Loop.3*
%{_mandir}/man3/MCE::Map.3*
%{_mandir}/man3/MCE::Mutex.3*
%{_mandir}/man3/MCE::Mutex::Channel.3*
%{_mandir}/man3/MCE::Mutex::Channel2.3*
%{_mandir}/man3/MCE::Mutex::Flock.3*
%{_mandir}/man3/MCE::Queue.3*
%{_mandir}/man3/MCE::Relay.3*
%{_mandir}/man3/MCE::Signal.3*
%{_mandir}/man3/MCE::Step.3*
%{_mandir}/man3/MCE::Stream.3*
%{_mandir}/man3/MCE::Subs.3*
%{_mandir}/man3/MCE::Util.3*

%files tools
%{_bindir}/mce_grep
%{_bindir}/mce_egrep
%{_bindir}/mce_fgrep
%{_bindir}/mce_zgrep
%{_bindir}/mce_zegrep
%{_bindir}/mce_zfgrep

%changelog
%autochangelog
