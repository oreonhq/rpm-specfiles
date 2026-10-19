%global source0_hash 50beea689c098fe4aaeb83806c40b9fe7f946d5769acf99f849f099091a4b985
%bcond_without perl_AnyEvent_enables_Event
%bcond_without perl_AnyEvent_enables_Glib
%bcond_without perl_AnyEvent_enables_POE
%bcond_without perl_AnyEvent_enables_Tk
%global debug_package %{nil}
%global have_weak_deps 0%{?fedora} > 20 || 0%{?rhel} > 7
Name:           perl-AnyEvent
Version:        7.17
Release:        23%{?dist}
Summary:        Framework for multiple event loops
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/AnyEvent
Source0:        https://cpan.metacpan.org/modules/by-module/AnyEvent/AnyEvent-%{version}.tar.gz
%if 0%{!?perl_bootstrap:1}
%if %{with perl_AnyEvent_enables_Event}
%endif
%if %{with perl_AnyEvent_enables_Glib}
%endif
%if %{with perl_AnyEvent_enables_POE}
%endif
%if %{with perl_AnyEvent_enables_Tk}
%endif
%endif
Requires:       perl(File::Temp)
%if %{have_weak_deps}
Recommends:     perl(Guard)
Recommends:     perl(Storable)
Recommends:     perl(Sys::Syslog)
Recommends:     perl(Task::Weaken)
Recommends:     perl(Unicode::Normalize)
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
%global __requires_exclude ^perl[(](%{optional_deps})[)]
%global __provides_exclude ^perl[(](AnyEvent(::Impl::(Cocoa|FLTK|UV))?|DB)[)]$
Provides:       perl(AnyEvent)
Provides:       perl(AnyEvent)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(Canary::Stability)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Event)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Glib)
BuildRequires:  perl(Guard)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Net::SSLeay)
BuildRequires:  perl(POE)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Tk)
BuildRequires:  perl(Unicode::Normalize)
BuildRequires:  perl(base)
BuildRequires:  perl(integer)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
AnyEvent provides an identical interface to multiple event loops. This allows
module authors to utilize an event loop without forcing module users to use the
same event loop (as multiple event loops cannot coexist peacefully at any one
time).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main
%endif
%check

export PERL_ANYEVENT_LOOP_TESTS=1
make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.17-23
- Prepare for Oreon 11 (RP1)
