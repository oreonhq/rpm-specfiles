%global source1_hash 11576dde4b1e583ea3a92b47c97c30c17bab7bffa401b1a790ce154ca72fa5b6
%global source0_hash f2c82b073a947c8255284249097667f9b14e660bf86186f3fcd3b3b3e087814e
Summary:        Disposable Soft Synth Interface
Name:         dssi
Version:      1.1.1
Release:        1%{?dist}
License:      MIT
URL:          http://dssi.sourceforge.net/
Source0:        http://download.sf.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Source1:      http://download.sf.net/sourceforge/%{name}/README
Patch1:       %{name}-lib64.patch
Patch2:       %{name}-liblo.patch
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  gcc
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  ladspa-devel
BuildRequires:  liblo-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  make
BuildRequires:  qt4-devel
# /oreon:deps
%description
Disposable Soft Synth Interface (DSSI, pronounced "dizzy") is a proposal for a
plugin API for software instruments (soft synths) with user interfaces,
permitting them to be hosted in-process by Linux audio applications. Think of
it as LADSPA-for-instruments, or something comparable to a simpler version of
VSTi.

%package examples
Summary:  DSSI plugin examples
License:  LicenseRef-Callaway-Public-Domain
Requires: %{name} = %{version}
%description examples
Example plugins for the Disposable Soft Synth Interface.

%package devel
Summary:  Libraries, includes, etc to develop DSSI applications
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make -C tests controller
tests/controller
%files -f %{oreon_filedir}/main.list
%files -n dssi-examples -f %{oreon_filedir}/dssi-examples.list
%files -n dssi-devel -f %{oreon_filedir}/dssi-devel.list

%changelog

%autochangelog
