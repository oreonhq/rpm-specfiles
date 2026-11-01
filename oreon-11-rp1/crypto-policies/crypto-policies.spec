%global source0_hash 6b504147227dbd98f92039234ac4c8678cffcda406ae301ad4f5582c389aaf41
%global commit 14a7b30a95489e38e63c61779e2410cbf5884613
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: crypto-policies
Version: 20261005
Release: 1%{?dist}
Summary: System-wide crypto policies
License: LGPL-2.1-or-later
URL: https://gitlab.com/redhat-crypto/fedora-crypto-policies
Source0: https://gitlab.com/redhat-crypto/fedora-crypto-policies/-/archive/%{commit}/fedora-crypto-policies-%{commit}.tar.gz
BuildArch: noarch
Requires: python3

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: python3
BuildRequires: make
%endif

%description
Policy definitions and generated back-end configuration that set one
system-wide cryptographic policy for TLS, SSH, Kerberos and other libraries.

%prep
%oreon_sha256
%autosetup -n fedora-crypto-policies-%{commit} -p1
rm -f policies/FEDORA*.pol

%build
mkdir -p output
python3 python/build-crypto-policies.py --reloadcmds policies output

%install
d=%{buildroot}%{_datadir}/crypto-policies
mkdir -p $d %{buildroot}%{_bindir} %{buildroot}%{_libexecdir}
install -pm0644 default-config default-fips-config output/reload-cmds.sh $d/
for f in $(find output -name '*.txt'); do x=$(dirname $f | cut -f 2- -d /); install -pm0644 -D -t $d/$x $f; done
for f in $(find policies -name '*.p*'); do install -pm0644 -D -t $d/$(dirname $f) $f; done
for f in $(find python -name '*.py'); do install -pm0644 -D -t $d/$(dirname $f) $f; done
chmod 0755 $d/python/update-crypto-policies.py $d/python/build-crypto-policies.py
install -pm0755 update-crypto-policies %{buildroot}%{_bindir}/
install -pm0755 fips-crypto-policy-overlay fips-setup-helper %{buildroot}%{_libexecdir}/
install -Dpm0644 fips-crypto-policy-overlay.service %{buildroot}%{_unitdir}/fips-crypto-policy-overlay.service
mkdir -p %{buildroot}%{_sysconfdir}/crypto-policies/{back-ends,state,local.d,policies/modules}
echo DEFAULT > %{buildroot}%{_sysconfdir}/crypto-policies/config
echo DEFAULT > %{buildroot}%{_sysconfdir}/crypto-policies/state/current
for f in $d/DEFAULT/*.txt; do
  b=$(basename $f .txt)
  ln -s %{_datadir}/crypto-policies/DEFAULT/$b.txt %{buildroot}%{_sysconfdir}/crypto-policies/back-ends/$b.config
done
sed -i '1s|^#!.*python.*|#!/usr/bin/python3|' $d/python/*.py
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING.LESSER
%dir %{_sysconfdir}/crypto-policies
%dir %{_sysconfdir}/crypto-policies/back-ends
%dir %{_sysconfdir}/crypto-policies/state
%dir %{_sysconfdir}/crypto-policies/local.d
%dir %{_sysconfdir}/crypto-policies/policies
%dir %{_sysconfdir}/crypto-policies/policies/modules
