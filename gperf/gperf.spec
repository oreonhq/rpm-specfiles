Summary: A perfect hash function generator
Name: gperf
Version: 3.2.1
Release: 3%{?dist}
License: GPL-3.0-or-later
Source: https://ftp.gnu.org/pub/gnu/gperf/gperf-%{version}.tar.gz
URL: http://www.gnu.org/software/gperf/

BuildRequires:  gcc-c++
BuildRequires:  make

%description
Gperf is a perfect hash function generator written in C++. Simply
stated, a perfect hash function is a hash function and a data
structure that allows recognition of a key word in a set of words
using exactly one probe into the data structure.

%prep
%setup -q

%build
%configure
%make_build

%install
#mkdir -p $RPM_BUILD_ROOT/usr/share/{man,info}
%make_install

# remove the stuff from the buildroot
rm -rf $RPM_BUILD_ROOT{%{_mandir}/{dvi,html},%{_datadir}/doc}

%files
%doc README NEWS doc/*.{html,pdf} COPYING
%{_bindir}/%{name}
%{_mandir}/man1/gperf.1*
%{_infodir}/gperf.info*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.2.1-3
- Prepare for Oreon 11 (RP1)
