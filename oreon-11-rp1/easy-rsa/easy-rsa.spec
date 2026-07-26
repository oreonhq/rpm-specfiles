%global source0_hash c2572990ce91112eef8d1b8e4a3b58790da95b68501785c621f69121dfbd22d7

Name:      easy-rsa
Version:   3.2.6
Release:   1%{?dist}

Summary:   Simple shell based CA utility
License:   GPL-2.0-only

URL:       https://github.com/OpenVPN/easy-rsa
Source0:   %{url}/releases/download/v%{version}/EasyRSA-%{version}.tgz

Requires:  openssl
BuildArch: noarch

%description
This is a small RSA key management package, based on the openssl
command line tool, that can be found in the easy-rsa subdirectory
of the OpenVPN distribution. While this tool is primary concerned
with key management for the SSL VPN application space, it can also
be used for building web certificates.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n EasyRSA-%{version} -p1

%build
#Nothing to build

%install
mkdir -p %{buildroot}%{_datadir}/easy-rsa/%{version}/
(
cd %{buildroot}%{_datadir}/easy-rsa
ln -s %{version} 3.0
ln -s %{version} 3
)
cp -rp easyrsa %{buildroot}%{_datadir}/easy-rsa/%{version}/
cp -rp openssl-easyrsa.cnf %{buildroot}%{_datadir}/easy-rsa/%{version}/
cp -rp x509-types %{buildroot}%{_datadir}/easy-rsa/%{version}/

%files
%doc ChangeLog *.md vars.example
%license gpl-2.0.txt COPYING.md
%{_datadir}/easy-rsa/

%changelog
%autochangelog
