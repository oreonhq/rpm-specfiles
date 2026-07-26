%global source0_hash f2c82b073a947c8255284249097667f9b14e660bf86186f3fcd3b3b3e087814e

Summary:      Disposable Soft Synth Interface
Name:         dssi
Version:      1.1.1
Release:      32%{?dist}
# Automatically converted from old format: MIT - review is highly recommended.
License:      MIT
URL:          http://dssi.sourceforge.net/
Source0:      http://download.sf.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Source1:      http://download.sf.net/sourceforge/%{name}/README
# Fix 64bit plugin path
# http://sourceforge.net/tracker/?func=detail&aid=2798711&group_id=104230&atid=637350
Patch1:       %{name}-lib64.patch
Patch2:       %{name}-liblo.patch

BuildRequires: alsa-lib-devel
BuildRequires: gcc
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: ladspa-devel
BuildRequires: liblo-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
# for the examples
BuildRequires: qt4-devel
BuildRequires: make

%description
Disposable Soft Synth Interface (DSSI, pronounced "dizzy") is a proposal for a
plugin API for software instruments (soft synths) with user interfaces,
permitting them to be hosted in-process by Linux audio applications. Think of
it as LADSPA-for-instruments, or something comparable to a simpler version of
VSTi.

%package examples
Summary:  DSSI plugin examples
# Automatically converted from old format: Public Domain - review is highly recommended.
License:  LicenseRef-Callaway-Public-Domain
Requires: %{name} = %{version}

%description examples
Example plugins for the Disposable Soft Synth Interface.

%package devel
Summary:  Libraries, includes, etc to develop DSSI applications
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:  LicenseRef-Callaway-LGPLv2+
Requires: alsa-lib-devel
Requires: ladspa-devel
Requires: pkgconfig

%description devel
Libraries, include files, etc you can use to develop DSSI based applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

cp -a %{SOURCE1} README.%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/dssi/*.la

%check
# Build and run the tests
make -C tests controller
tests/controller

%files
%doc README* ChangeLog doc/TODO
%{_bindir}/dssi_osc_send
%{_bindir}/dssi_osc_update
%{_bindir}/jack-dssi-host
%{_bindir}/dssi_analyse_plugin
%{_bindir}//dssi_list_plugins
%dir %{_libdir}/dssi
%{_mandir}/man1/*

%files examples
%{_libdir}/dssi/less_trivial_synth.so
%{_libdir}/dssi/less_trivial_synth
%{_libdir}/dssi/trivial_sampler.so
%{_libdir}/dssi/trivial_sampler
%{_libdir}/dssi/trivial_synth.so
%{_libdir}/dssi/karplong.so
%{_bindir}/trivial_sampler
%{_bindir}/trivial_synth
%{_bindir}/less_trivial_synth
%{_bindir}/karplong

%files devel
%doc doc/*.txt COPYING
%{_includedir}/dssi.h
%{_libdir}/pkgconfig/dssi.pc

%changelog
%autochangelog
