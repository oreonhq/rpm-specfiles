%global source0_hash f51b27689b43e32a0181876a4904740b989b9e484c723ddd4219993407554d71
%global srcname TITools
%global commit cc7dc08d831beaf6c4f865c3acd49a2be58df5a9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20160515
Name:           titools
Version:        0.2^%{date}g%{shortcommit}
Release:        1%{?dist}
Summary:        Command-line programs for communicating with a TI calculator
License:        GPL-3.0-or-later
URL:            https://github.com/Jonimoose/%{srcname}
Source0:        https://github.com/Jonimoose/%{srcname}/archive/%{commit}/%{srcname}-%{commit}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tilibs-devel
# /oreon:deps
%description
This package contains a collection of simple command-line tools for
communicating with TI graphing calculators.  These tools are based on
the excellent libticalcs2 library developed by the TiLP project (or
the equivalent libcalcprotocols library.)

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{commit}

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
