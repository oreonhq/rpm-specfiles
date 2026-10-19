%global source0_hash c16cbd1d5494b1b058b787ef936fa483ac2f3ce92657372c92b3dbf153750457
Name:           festival-freebsoft-utils
Version:        0.10
Release:        1%{?dist}
Summary:        Utilities that enhance Festival with some useful features
BuildArch:      noarch
License:        GPL-2.0-or-later
%global doc_license GPL-2.0-or-later OR GFDL-1.2-no-invariants-or-later
SourceLicense:  %{license} AND %{doc_license}
URL:            https://www.freebsoft.org/festival-freebsoft-utils
Source0:        https://freebsoft.org/pub/projects/%{name}/%{name}-%{version}.tar.gz
Patch:          https://github.com/brailcom/festival-freebsoft-utils/pull/1.patch
Requires:       festival
Recommends:     sox
Recommends:     /usr/bin/iconv
# oreon:deps
BuildRequires:  /usr/bin/iconv
BuildRequires:  festival
BuildRequires:  make
BuildRequires:  sox
BuildRequires:  tex(latex)
BuildRequires:  texinfo-tex
# /oreon:deps
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
BuildRequires:  texinfo-tex
BuildRequires:  tex(latex)
%description doc
Documentation for festival-freebsoft-utils in info, PDF, and HTML formats.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build clean
%make_build info pdf html
%install
install -t '%{buildroot}/%{_datadir}/festival' -D -p -m 0644 *.scm
install -t '%{buildroot}/%{_infodir}' -D -p -m 0644 doc/*.info
install -t '%{buildroot}/%{_pkgdocdir}' -D -p -m 0644 \
    doc/*.pdf doc/*.html ANNOUNCE NEWS README
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n festival-freebsoft-utils-doc -f %{oreon_filedir}/festival-freebsoft-utils-doc.list

%changelog

%autochangelog
