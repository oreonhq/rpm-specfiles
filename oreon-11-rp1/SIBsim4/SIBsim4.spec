%global source0_hash ee02ae5f678d6843cf3ba267140dfccf9648a60d1f01263ae70d405723a35463

Name:           SIBsim4
Version:        0.20
Release:        33%{?dist}
Summary:        Align expressed RNA sequences on a DNA template
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://sibsim4.sourceforge.net
Source0:        http://downloads.sourceforge.net/sibsim4/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc

%description
SIBsim4 is a modified version of the sim4 program, which is a
similarity-based tool for aligning an expressed DNA sequence (EST,
mRNA) with a genomic sequence.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
make %{?_smp_mflags} OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 755 SIBsim4 $RPM_BUILD_ROOT/%{_bindir}/
install -m 644 SIBsim4.1 $RPM_BUILD_ROOT/%{_mandir}/man1

%files
%doc COPYRIGHT
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
