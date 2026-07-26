%global source0_hash fb626472eca43ac2bc03526d49151c5f76b46b92327ab9ee9c9455210b938c2b

%define cvsver 20100106
%define codename BlameMichelson

Summary: Controllable Regex Mutilator: multi-method content classifier and filter
Name: crm114
Version: 0
Release: 36.%{cvsver}%{?dist}
URL: http://crm114.sourceforge.net/
# Automatically converted from old format: GPLv3 - review is highly recommended.
License: GPL-3.0-only
Source0: http://crm114.sourceforge.net/tarballs/%{name}-%{cvsver}-%{codename}.src.tar.gz
Patch0: %{name}-rpm.patch
Patch1: %{name}-tre.patch
# fix build with gcc5 (rhbz#1239418)
Patch2: %{name}-gcc5.patch
# fix potential string format overflow caught by gcc
Patch3: %{name}-format-overflow.patch
# fix build with gcc10
Patch4: %{name}-gcc10.patch
BuildRequires: emacs
BuildRequires: gcc
BuildRequires: tre-devel >= 0.8.0
# for tests
BuildRequires: words
BuildRequires: make
Requires: emacs-filesystem >= %{_emacs_version}

%description 
CRM114 is a system to examine incoming e-mail, system log streams,
data files or other data streams, and to sort, filter, or alter the
incoming files or data streams according to the user's wildest
desires. Criteria for categorization of data can be by satisfaction of
regexes, by sparse binary polynomial matching with a Bayesian Chain
Rule evaluator, or by other means.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{cvsver}-%{codename}.src
%patch -P0 -p1 -b .r
%patch -P1 -p1 -b .tre
%patch -P2 -p1 -b .gcc5
%patch -P3 -p1 -b .fmt-ovfl
%patch -P4 -p1 -b .gcc10
chmod 644 mailfilter.cf

%build
make OPTFLAGS="$RPM_OPT_FLAGS -fPIE" LDFLAGS="$RPM_LD_FLAGS -fPIE" %{?_smp_mflags}
%{_emacs_bytecompile} %{name}-mode.el

%install
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_emacs_sitelispdir}/crm114}
make DESTDIR=$RPM_BUILD_ROOT INSTALLFLAGS="-m 755 -p" install
install -pm 755 mail{filter,lib,reaver,trainer}.crm shuffle.crm $RPM_BUILD_ROOT%{_datadir}/%{name}/
install -pm 644 crm114-mode.elc $RPM_BUILD_ROOT%{_emacs_sitelispdir}/crm114
mv $RPM_BUILD_ROOT%{_emacs_sitelispdir}/{%{name}-mode.el,%{name}/}
chmod 644 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{name}/%{name}-mode.el

%check
make megatest

%files
%doc README *.txt *.recipe *.example mailfilter.cf
%{_bindir}/*
%{_datadir}/%{name}
%{_emacs_sitelispdir}/%{name}

%changelog
%autochangelog
