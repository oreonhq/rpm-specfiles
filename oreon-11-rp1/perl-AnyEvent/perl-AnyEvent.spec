#global subver 1

# Support Event
%if 0%{?rhel} >= 9
%bcond_with perl_AnyEvent_enables_Event
%else
%bcond_without perl_AnyEvent_enables_Event
%endif

# Support Glib
%if 0%{?rhel} >= 9
%bcond_with perl_AnyEvent_enables_Glib
%else
%bcond_without perl_AnyEvent_enables_Glib
%endif

# Support POE
%if 0%{?rhel} >= 9
%bcond_with perl_AnyEvent_enables_POE
%else
%bcond_without perl_AnyEvent_enables_POE
%endif

# Support Tk
%if 0%{?rhel} >= 9
%bcond_with perl_AnyEvent_enables_Tk
%else
%bcond_without perl_AnyEvent_enables_Tk
%endif

# A noarch-turned-arch package should not have debuginfo
%global debug_package %{nil}

# Use weak dependencies where available
%global have_weak_deps 0%{?fedora} > 20 || 0%{?rhel} > 7

Name:           perl-AnyEvent
Version:        7.17
Release:        23%{?dist}
Summary:        Framework for multiple event loops
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/AnyEvent
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/AnyEvent-7.17.tar.gz
# oreon url source checksums begin
%global source0_sha256 50beea689c098fe4aaeb83806c40b9fe7f946d5769acf99f849f099091a4b985
%global source0_file AnyEvent-7.17.tar.gz
# oreon url source checksums end


# Build requirements
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter >= 3:5.8.1
BuildRequires:  perl(Canary::Stability)
BuildRequires:  perl(ExtUtils::MakeMaker)

# Module requirements
BuildRequires:  perl(B)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Guard)
BuildRequires:  perl(integer)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Unicode::Normalize)

# Test suite requirements
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Net::SSLeay) >= 1.33
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

# Event loop testing
#
# Many of these modules require or build-require AnyEvent themselves,
# so don't do event loop testing when bootstrapping
#
# Cocoa, FLTK and UV are not in Fedora/EPEL
# AnyEvent::AIO, EV and IO::Async::Loop are not (yet) in EPEL-7
# Test suite does not currently test the Qt event loop
%if 0%{!?perl_bootstrap:1}
%if %{with perl_AnyEvent_enables_Event}
BuildRequires:  perl(Event)
%endif
%if %{with perl_AnyEvent_enables_Glib}
BuildRequires:  perl(Glib) >= 1.210
%endif
%if %{with perl_AnyEvent_enables_POE}
BuildRequires:  perl(POE) >= 1.312
%endif
%if %{with perl_AnyEvent_enables_Tk}
BuildRequires:  perl(Tk)
%endif
%if 0%{?fedora}
BuildRequires:  perl(AnyEvent::AIO)
BuildRequires:  perl(EV) >= 4.00
BuildRequires:  perl(IO::AIO) >= 4.13
BuildRequires:  perl(IO::Async::Loop) >= 0.33
%endif
%endif

# Runtime requires
Requires:       perl(File::Temp)
%if %{have_weak_deps}
# Optional but recommended
Recommends:     perl(Guard)
Recommends:     perl(Storable)
Recommends:     perl(Sys::Syslog)
Recommends:     perl(Task::Weaken)
Recommends:     perl(Unicode::Normalize)
# Heavier optional modules
Suggests:       perl(CBOR::XS)
Suggests:       perl(Coro)
Suggests:       perl(Coro::Debug)
Suggests:       perl(JSON::XS)
Suggests:       perl(Net::SSLeay) >= 1.33
%else
Requires:       perl(Guard)
Requires:       perl(Storable)
Requires:       perl(Sys::Syslog)
Requires:       perl(Task::Weaken)
Requires:       perl(Unicode::Normalize)
%endif

# Optional dependencies we don't want to require
%global optional_deps                  AnyEvent::AIO
%global optional_deps %{optional_deps}|Cocoa::EventLoop
%global optional_deps %{optional_deps}|EV
%if %{with perl_AnyEvent_enables_Event}
%global optional_deps %{optional_deps}|Event
%endif
%global optional_deps %{optional_deps}|Event::Lib
%global optional_deps %{optional_deps}|EventLoop
%global optional_deps %{optional_deps}|FLTK
%if %{with perl_AnyEvent_enables_Glib}
%global optional_deps %{optional_deps}|Glib
%endif
%global optional_deps %{optional_deps}|IO::AIO
%global optional_deps %{optional_deps}|IO::Async::Loop
%global optional_deps %{optional_deps}|Irssi
%if %{with perl_AnyEvent_enables_POE}
%global optional_deps %{optional_deps}|POE
%endif
%global optional_deps %{optional_deps}|Qt
%global optional_deps %{optional_deps}|Qt::isa
%global optional_deps %{optional_deps}|Qt::slots
%if %{with perl_AnyEvent_enables_Tk}
%global optional_deps %{optional_deps}|Tk
%endif
%global optional_deps %{optional_deps}|UV

# Don't include optional dependencies
%global __requires_exclude ^perl[(](%{optional_deps})[)]

# Filter unversioned and bogus provides
# AnyEvent::Impl::{Cocoa,FLTK,UV} are filtered as the required
# underlying modules are not currently available in Fedora
%global __provides_exclude ^perl[(](AnyEvent(::Impl::(Cocoa|FLTK|UV))?|DB)[)]$


%description
AnyEvent provides an identical interface to multiple event loops. This allows
module authors to utilize an event loop without forcing module users to use the
same event loop (as multiple event loops cannot coexist peacefully at any one
time).


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/AnyEvent-7.17.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "50beea689c098fe4aaeb83806c40b9fe7f946d5769acf99f849f099091a4b985" || { echo "oreon: Source0 SHA256 mismatch for AnyEvent-7.17.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n AnyEvent-%{version}%{?subver}


%build
PERL_CANARY_STABILITY_NOPROMPT=1 perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%if !%{with perl_AnyEvent_enables_Event}
rm %{buildroot}%{perl_vendorarch}/AnyEvent/Impl/Event.pm
rm %{buildroot}%{_mandir}/man3/AnyEvent::Impl::Event.3*
%endif
%if !%{with perl_AnyEvent_enables_Glib}
rm %{buildroot}%{perl_vendorarch}/AnyEvent/Impl/Glib.pm
rm %{buildroot}%{_mandir}/man3/AnyEvent::Impl::Glib.3*
%endif
%if !%{with perl_AnyEvent_enables_POE}
rm %{buildroot}%{perl_vendorarch}/AnyEvent/Impl/POE.pm
rm %{buildroot}%{_mandir}/man3/AnyEvent::Impl::POE.3*
%endif
%if !%{with perl_AnyEvent_enables_Tk}
rm %{buildroot}%{perl_vendorarch}/AnyEvent/Impl/Tk.pm
rm %{buildroot}%{_mandir}/man3/AnyEvent::Impl::Tk.3*
%endif


%check
# PERL_ANYEVENT_NET_TESTS shouldn't be set to avoid network tests
# on our builder.
export PERL_ANYEVENT_LOOP_TESTS=1
make test


%files
%license COPYING
%doc Changes README
%{perl_vendorarch}/AE.pm
%{perl_vendorarch}/AnyEvent.pm
%dir %{perl_vendorarch}/AnyEvent/
%{perl_vendorarch}/AnyEvent/constants.pl
%{perl_vendorarch}/AnyEvent/DNS.pm
%{perl_vendorarch}/AnyEvent/Debug.pm
%{perl_vendorarch}/AnyEvent/FAQ.pod
%{perl_vendorarch}/AnyEvent/Handle.pm
%dir %{perl_vendorarch}/AnyEvent/Impl
%{perl_vendorarch}/AnyEvent/Impl/Cocoa.pm
%{perl_vendorarch}/AnyEvent/Impl/EV.pm
%if %{with perl_AnyEvent_enables_Event}
%{perl_vendorarch}/AnyEvent/Impl/Event.pm
%endif
%{perl_vendorarch}/AnyEvent/Impl/EventLib.pm
%{perl_vendorarch}/AnyEvent/Impl/FLTK.pm
%if %{with perl_AnyEvent_enables_Glib}
%{perl_vendorarch}/AnyEvent/Impl/Glib.pm
%endif
%{perl_vendorarch}/AnyEvent/Impl/IOAsync.pm
%{perl_vendorarch}/AnyEvent/Impl/Irssi.pm
%{perl_vendorarch}/AnyEvent/Impl/Perl.pm
%if %{with perl_AnyEvent_enables_POE}
%{perl_vendorarch}/AnyEvent/Impl/POE.pm
%endif
%{perl_vendorarch}/AnyEvent/Impl/Qt.pm
%if %{with perl_AnyEvent_enables_Tk}
%{perl_vendorarch}/AnyEvent/Impl/Tk.pm
%endif
%{perl_vendorarch}/AnyEvent/Impl/UV.pm
%{perl_vendorarch}/AnyEvent/Intro.pod
%{perl_vendorarch}/AnyEvent/IO.pm
%dir %{perl_vendorarch}/AnyEvent/IO
%{perl_vendorarch}/AnyEvent/IO/IOAIO.pm
%{perl_vendorarch}/AnyEvent/IO/Perl.pm
%{perl_vendorarch}/AnyEvent/Log.pm
%{perl_vendorarch}/AnyEvent/Loop.pm
%{perl_vendorarch}/AnyEvent/Socket.pm
%{perl_vendorarch}/AnyEvent/Strict.pm
%{perl_vendorarch}/AnyEvent/TLS.pm
%{perl_vendorarch}/AnyEvent/Util.pm
%dir %{perl_vendorarch}/AnyEvent/Util
%{perl_vendorarch}/AnyEvent/Util/idna.pl
%{perl_vendorarch}/AnyEvent/Util/uts46data.pl
%{_mandir}/man3/AE.3*
%{_mandir}/man3/AnyEvent.3*
%{_mandir}/man3/AnyEvent::DNS.3*
%{_mandir}/man3/AnyEvent::Debug.3*
%{_mandir}/man3/AnyEvent::FAQ.3*
%{_mandir}/man3/AnyEvent::Handle.3*
%{_mandir}/man3/AnyEvent::Impl::Cocoa.3*
%{_mandir}/man3/AnyEvent::Impl::EV.3*
%if %{with perl_AnyEvent_enables_Event}
%{_mandir}/man3/AnyEvent::Impl::Event.3*
%endif
%{_mandir}/man3/AnyEvent::Impl::EventLib.3*
%{_mandir}/man3/AnyEvent::Impl::FLTK.3*
%if %{with perl_AnyEvent_enables_Glib}
%{_mandir}/man3/AnyEvent::Impl::Glib.3*
%endif
%{_mandir}/man3/AnyEvent::Impl::IOAsync.3*
%{_mandir}/man3/AnyEvent::Impl::Irssi.3*
%if %{with perl_AnyEvent_enables_POE}
%{_mandir}/man3/AnyEvent::Impl::POE.3*
%endif
%{_mandir}/man3/AnyEvent::Impl::Perl.3*
%{_mandir}/man3/AnyEvent::Impl::Qt.3*
%if %{with perl_AnyEvent_enables_Tk}
%{_mandir}/man3/AnyEvent::Impl::Tk.3*
%endif
%{_mandir}/man3/AnyEvent::Impl::UV.3*
%{_mandir}/man3/AnyEvent::Intro.3*
%{_mandir}/man3/AnyEvent::IO.3*
%{_mandir}/man3/AnyEvent::IO::IOAIO.3*
%{_mandir}/man3/AnyEvent::IO::Perl.3*
%{_mandir}/man3/AnyEvent::Log.3*
%{_mandir}/man3/AnyEvent::Loop.3*
%{_mandir}/man3/AnyEvent::Socket.3*
%{_mandir}/man3/AnyEvent::Strict.3*
%{_mandir}/man3/AnyEvent::TLS.3*
%{_mandir}/man3/AnyEvent::Util.3*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.17-23
- Prepare for Oreon 11 (RP1)
