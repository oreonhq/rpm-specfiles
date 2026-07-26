%global source0_hash ea971a52f95489211d91e050af1244f38e4d401de1636e890bc51a55526ed9a8

Name: smcalc
Summary: Matrix Calculator
URL: http://smcalc.sourceforge.net
Version: 1.0.1
Release: 15%{?dist}
Source0: https://sourceforge.net/projects/smcalc/files/smcalc/%{name}-%{version}.tar.gz
License: MIT

BuildRequires: make
BuildRequires: gcc-c++

%description
Simple matrix calculator with TUI able to
do basic matrix operations including fast
computing of determinant.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}
sed -i s:/usr/local:%{buildroot}%_prefix:g src/Makefile
sed -i 's:-ansi:-ansi -g:g' src/Makefile

%build
cd src
%make_build

%install
cd src
%make_install

%files
%license COPIYNG
%doc AUTHORS Changelog README
%{_bindir}/%{name}

%changelog
%autochangelog
