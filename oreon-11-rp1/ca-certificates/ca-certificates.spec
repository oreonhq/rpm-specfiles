%global source0_hash 3ec2b4d240dc12c747eaf450061db84af757c483bbda302f9e29ceb5d70be510
%global nss_tag 3_132
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: ca-certificates
Version: 3.132
Release: 2%{?dist}
Summary: Mozilla CA root certificate bundle
License: MPL-2.0
URL: https://hg.mozilla.org/projects/nss
Source0: https://raw.githubusercontent.com/nss-dev/nss/NSS_%{nss_tag}_RTM/lib/ckfw/builtins/certdata.txt
Source3: oreon-certdata2pem.py
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3

%description
The Mozilla set of trusted root CA certificates for TLS server
authentication, as a PEM bundle.

%prep
%oreon_sha256
%setup -q -c -T -n ca-certificates-%{version}
cp -p %{SOURCE0} %{SOURCE3} .

%build
python3 oreon-certdata2pem.py certdata.txt ca-bundle.crt

%install
install -Dpm0644 ca-bundle.crt %{buildroot}%{_sysconfdir}/pki/tls/certs/ca-bundle.crt
install -Dpm0644 ca-bundle.crt %{buildroot}%{_datadir}/pki/ca-trust-source/anchors/ca-bundle.crt
mkdir -p %{buildroot}%{_sysconfdir}/pki/ca-trust/source/anchors
mkdir -p %{buildroot}%{_sysconfdir}/ssl %{buildroot}%{_sysconfdir}/pki/tls
ln -s ../pki/tls/certs %{buildroot}%{_sysconfdir}/ssl/certs
ln -s certs/ca-bundle.crt %{buildroot}%{_sysconfdir}/pki/tls/cert.pem
ln -s ../pki/tls/certs/ca-bundle.crt %{buildroot}%{_sysconfdir}/ssl/cert.pem
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%dir %{_sysconfdir}/pki
%dir %{_sysconfdir}/pki/tls
%dir %{_sysconfdir}/pki/tls/certs
%dir %{_sysconfdir}/ssl
%dir %{_sysconfdir}/pki/ca-trust
%dir %{_sysconfdir}/pki/ca-trust/source
%dir %{_sysconfdir}/pki/ca-trust/source/anchors
%dir %{_datadir}/pki
%dir %{_datadir}/pki/ca-trust-source
%dir %{_datadir}/pki/ca-trust-source/anchors
