# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash bb4338102ff3b49a81423da8a1a158b420124b055b60fa76cfb4b18677130a23
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:          espeak-ng
Version:       1.52.0
Release:       1%{?dist}
Summary:       eSpeak NG Text-to-Speech

License:       GPL-3.0-only AND GPL-3.0-or-later AND Apache-2.0 AND BSD-2-Clause AND Unicode-DFS-2016 AND CC-BY-SA-3.0
URL:           https://github.com/espeak-ng/espeak-ng
Source0:       %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: rubygem-ronn-ng
BuildRequires: rubygem-kramdown
BuildRequires: pcaudiolib-devel

Patch:        espeak-ng-1.52-add-text-to-phonemes-with-terminator.patch

%description
The eSpeak NG (Next Generation) Text-to-Speech program is an open source speech
synthesizer that supports over 70 languages. It is based on the eSpeak engine
created by Jonathan Duddington. It uses spectral formant synthesis by default
which sounds robotic, but can be configured to use Klatt formant synthesis
or MBROLA to give it a more natural sound.

%package devel
Summary: Development files for espeak-ng
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for eSpeak NG, a software speech synthesizer.

%package vim
Summary: Vim syntax highlighting for espeak-ng data files
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description vim
%{summary}.

%package doc
Summary: Documentation for espeak-ng
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description doc
Documentation for eSpeak NG, a software speech synthesizer.

%prep
%oreon_sha256
%autosetup -p1
rm -rf src/include/compat/endian.h src/compat/getopt.c android/

%build
./autogen.sh
%configure
%make_build src/espeak-ng src/speak-ng
make
LC_ALL=C.UTF-8 make docs

%install
%make_install
rm -vf %{buildroot}%{_libdir}/libespeak-ng-test.so*
rm -vf %{buildroot}%{_libdir}/*.{a,la}
rm -vf %{buildroot}%{_bindir}/{speak,espeak}
rm -vrf %{buildroot}%{_includedir}/espeak
mv %{buildroot}%{_datadir}/vim/addons %{buildroot}%{_datadir}/vim/vimfiles
rm -vrf %{buildroot}%{_datadir}/vim/registry

%check
ESPEAK_DATA_PATH=`pwd` LD_LIBRARY_PATH=src:${LD_LIBRARY_PATH} src/espeak-ng ...

%ldconfig_scriptlets

%files
%license COPYING
%license COPYING.APACHE
%license COPYING.BSD2
%license COPYING.UCD
%doc README.md
%doc ChangeLog.md
%{_bindir}/speak-ng
%{_bindir}/espeak-ng
%{_libdir}/libespeak-ng.so.1
%{_libdir}/libespeak-ng.so.1.*
%{_datadir}/espeak-ng-data
%{_mandir}/man1/speak-ng.1.gz
%{_mandir}/man1/espeak-ng.1.gz

%files devel
%{_libdir}/pkgconfig/espeak-ng.pc
%{_libdir}/libespeak-ng.so
%{_includedir}/espeak-ng

%files vim
%{_datadir}/vim/vimfiles/ftdetect/espeakfiletype.vim
%{_datadir}/vim/vimfiles/syntax/espeaklist.vim
%{_datadir}/vim/vimfiles/syntax/espeakrules.vim

%files doc
%doc docs/*.html

%changelog
%autochangelog
