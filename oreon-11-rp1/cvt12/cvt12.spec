%global source0_hash f76d2c7712234629e88cf629204ee2def26c842fe5fdf2df3db500397f3d0283

%global commit 6f66135104dc50425c904898822d49c50e130751
%global date 20221228
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Summary: CVT (Coordinated Video Timings) modeline calculator with CVT v1.2 timings
Name: cvt12
Version: 0^%{date}git%{shortcommit}
Release: 7%{?dist}
URL: https://github.com/kevinlekiller/cvt_modeline_calculator_12
Source0: %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
License: BSD-3-Clause
BuildRequires: gcc
BuildRequires: make

%description
CVT (Coordinated Video Timings) modeline calculator with CVT v1.2
timings.

This is a modified CVT modeline calculator based on cvt by
erich@uruk.org, which is based on GTF modeline calculator by Andy
Ritger.

This modified version adds support for CVT v1.2 (VESA-2013-3 v1.2).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n cvt_modeline_calculator_12-%{commit} -p1

%build
gcc $CFLAGS $LDFLAGS cvt12.c -o cvt12 -lm

%install
install -D -pm0755 -t %{buildroot}%{_bindir} cvt12

%files
%doc README.md
%{_bindir}/cvt12

%changelog
%autochangelog
