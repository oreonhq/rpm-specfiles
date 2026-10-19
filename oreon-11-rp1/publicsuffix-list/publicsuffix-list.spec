%global source2_hash 8f50ad958916d6a8f79fba2363501475571acce752757f9126fe9d2f17dd920d
%global source1_hash 3f3d9e0024b1921b067d6f7f88deb4a60cbe7a78e76c64e3f1d7fc3b779b9d04
%global source0_hash 3e6ca639b7ef33f86ec0e6fe9a475857cf2585f28fdf485f38f14d5f00c1c2a4
%global source3_hash 1dcc9ceae8b128f3c0b3f654decd0e1e891afc6ff81098f227ef260449dae208
%bcond_without  dafsa
Name:           publicsuffix-list
Version:        20260116
Release:        1%{?dist}
Summary:        Cross-vendor public domain suffix database
License:        MPL-2.0
URL:            https://publicsuffix.org/
Source0:        https://publicsuffix.org/list/public_suffix_list.dat
Source1:        https://www.mozilla.org/media/MPL/2.0/index.txt
Source2:        https://github.com/publicsuffix/list/raw/main/tests/test_psl.txt
%global libpsl_tools_ver 0.21.5
Source3:        https://github.com/rockdaboot/libpsl/releases/download/0.21.5/libpsl-0.21.5.tar.gz
BuildArch:      noarch
%if %{with dafsa}
%endif
# oreon:deps
BuildRequires:  python3
# /oreon:deps
%description
The Public Suffix List is a cross-vendor initiative to provide
an accurate list of domain name suffixes, maintained by the hard work 
of Mozilla volunteers and by submissions from registries.
Software using the Public Suffix List will be able to determine where 
cookies may and may not be set, protecting the user from being 
tracked across sites.

%if %{with dafsa}
%package dafsa
Summary:        Cross-vendor public domain suffix database in DAFSA form
%description dafsa
The Public Suffix List is a cross-vendor initiative to provide
an accurate list of domain name suffixes, maintained by the hard work 
of Mozilla volunteers and by submissions from registries.
Software using the Public Suffix List will be able to determine where 
cookies may and may not be set, protecting the user from being 
tracked across sites.

This package includes a DAFSA representation of the Public Suffix List
for runtime loading.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source3_hash}" = "none" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source3_hash}" || { echo "oreon: Source3 hash mismatch" >&2; exit 1; }; }
%setup -c -T
cp -av %{SOURCE0} .
install -m 644 -p -v %{SOURCE1} COPYING
%if %{with dafsa}
tar xf %{SOURCE3} libpsl-%{libpsl_tools_ver}/src/psl-make-dafsa
install -m755 libpsl-%{libpsl_tools_ver}/src/psl-make-dafsa ./psl-make-dafsa-bootstrap
sed -i '1s|.*|#!/usr/bin/python3|' ./psl-make-dafsa-bootstrap
%endif

%build

%if %{with dafsa}
LC_CTYPE=C.UTF-8 \
./psl-make-dafsa-bootstrap --output-format=binary \
  public_suffix_list.dat public_suffix_list.dafsa
%endif
%install
%if %{with dafsa}
install -m 644 -p -D public_suffix_list.dafsa $RPM_BUILD_ROOT/%{_datadir}/publicsuffix/public_suffix_list.dafsa
%endif
install -m 644 -p -D %{SOURCE0} $RPM_BUILD_ROOT/%{_datadir}/publicsuffix/public_suffix_list.dat
install -m 644 -p -D %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/publicsuffix/test_psl.txt
ln -s public_suffix_list.dat $RPM_BUILD_ROOT/%{_datadir}/publicsuffix/effective_tld_names.dat
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n publicsuffix-list-dafsa -f %{oreon_filedir}/publicsuffix-list-dafsa.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20260116-1
- Prepare for Oreon 11 (RP1)
