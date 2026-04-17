%bcond_without  dafsa

Name:           publicsuffix-list
Version:        20260116
Release:        %autorelease
Summary:        Cross-vendor public domain suffix database

License:        MPL-2.0
URL:            https://publicsuffix.org/
Source0:        https://publicsuffix.org/list/public_suffix_list.dat
Source1:        https://www.mozilla.org/media/MPL/2.0/index.txt
Source2:        https://github.com/publicsuffix/list/raw/main/tests/test_psl.txt
# Bootstrap: DAFSA generator (same script as libpsl's psl-make-dafsa subpackage) so we
# do not need that RPM installed before publicsuffix-list-dafsa exists.
%global libpsl_tools_ver 0.21.5
Source3:        https://github.com/rockdaboot/libpsl/releases/download/%{libpsl_tools_ver}/libpsl-%{libpsl_tools_ver}.tar.gz

BuildArch:      noarch


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


%files
%license COPYING
%dir %{_datadir}/publicsuffix
%{_datadir}/publicsuffix/effective_tld_names.dat
%{_datadir}/publicsuffix/public_suffix_list.dat
%{_datadir}/publicsuffix/test_psl.txt

%if %{with dafsa}
%files dafsa
%license COPYING
%dir %{_datadir}/publicsuffix
%{_datadir}/publicsuffix/public_suffix_list.dafsa
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20260116-1
- Prepare for Oreon 11 (RP1)
