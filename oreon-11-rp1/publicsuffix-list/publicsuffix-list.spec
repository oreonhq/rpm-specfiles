%global source0_hash ed8204a65ce5f3ee78e33ef4e46a15d7ef52d12caf092b31fd5f6e80cdea46f9
%global commit 73f8cc701c084fe07d888ec552b2f0b53281a674
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: publicsuffix-list
Version: 20261031
Release: 1%{?dist}
Summary: Cross-vendor public domain suffix database
License: MPL-2.0
URL: https://publicsuffix.org/
Source0: https://github.com/publicsuffix/list/archive/%{commit}/list-%{commit}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
%endif

%description
The Public Suffix List is a cross-vendor initiative to provide an accurate
list of domain name suffixes.

%prep
%oreon_sha256
%autosetup -n list-%{commit} -p1

%build


%install
install -Dpm0644 public_suffix_list.dat %{buildroot}%{_datadir}/publicsuffix/public_suffix_list.dat
ln -s public_suffix_list.dat %{buildroot}%{_datadir}/publicsuffix/effective_tld_names.dat
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license LICENSE
%dir %{_datadir}/publicsuffix
