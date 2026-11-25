# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash c16cbd1d5494b1b058b787ef936fa483ac2f3ce92657372c92b3dbf153750457
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           festival-freebsoft-utils
Version:        0.10
Release:        %{autorelease}
Summary:        Utilities that enhance Festival with some useful features

BuildArch:      noarch

License:        GPL-2.0-or-later
%global doc_license GPL-2.0-or-later OR GFDL-1.2-no-invariants-or-later
SourceLicense:  %{license} AND %{doc_license}
URL:            https://www.freebsoft.org/festival-freebsoft-utils
Source0:        https://freebsoft.org/pub/projects/%{name}/%{name}-%{version}.tar.gz

Patch:          https://github.com/brailcom/festival-freebsoft-utils/pull/1.patch

BuildRequires: oreon-rpm-macros
BuildRequires:  festival
BuildRequires:  sox
BuildRequires:  /usr/bin/iconv

Requires:       festival
Recommends:     sox
Recommends:     /usr/bin/iconv

%description
A collection of utilities that enhance Festival with some useful features. They
provide all that is needed for interaction with Speech Dispatcher.

Key festival-freebsoft-utils features are:

• Generalized concept of input events. festival-freebsoft-utils allows not only
  plain text synthesis, but also combining it with sounds. Additionally,
  mechanism of logical events mapped to other events is provided.
• Substitution of events for given words.
• High-level voice selection mechanism and setting of basic prosodic parameters.
• Spelling mode.
• Capital letter signalization.
• Punctuation modes, for explicit reading or not reading punctuation characters.
• Incremental synthesis of texts and events.
• Speech Dispatcher support.
• Rudimentary SSML support.
• Enhance the Festival extension language with functions commonly used in Lisp.
• Support for wrapping already defined Festival functions by your own code.
• Everything is written in the extension language, no patching of the Festival
  C++ sources is needed.

%package doc
Summary:        Documentation for festival-freebsoft-utils
License:        %{doc_license}

BuildRequires:  make

%description doc
Documentation for festival-freebsoft-utils in info and HTML formats.

%prep
%oreon_sha256
%autosetup -p1

%build
%make_build clean
%make_build info html

%install
install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}/%{_datadir}/festival' *.scm
install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}/%{_infodir}' doc/*.info
install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}/%{_pkgdocdir}' \
    doc/*.html ANNOUNCE NEWS README

%files
%license COPYING
%{_datadir}/festival/*.scm

%files doc
%license COPYING
%doc %{_pkgdocdir}/ANNOUNCE
%doc %{_pkgdocdir}/NEWS
%doc %{_pkgdocdir}/README

%doc %{_pkgdocdir}/festival-freebsoft-utils.html

%doc %{_infodir}/festival-freebsoft-utils.info*

%changelog
%autochangelog
