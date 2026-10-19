%global source2_hash 2cf9526061070ecaf1629130b57db96a05c0b27714f29000d6a2930b655b5a3f
%global source0_hash 2846819d4f80df7c753530b2ea93484d41326f5dc5162dc453b92579203c0c32
Name:           nginx-mod-fancyindex
Version:        0.6.0
Release:        1%{?dist}
Summary:        Nginx FancyIndex module
License:        BSD-2-Clause
URL:            https://github.com/aperezdc/ngx-fancyindex
Source0:        https://github.com/aperezdc/ngx-fancyindex/releases/download/v%{version}/ngx-fancyindex-%{version}.tar.xz
Source1:        %{url}/releases/download/v%{version}/ngx-fancyindex-%{version}.tar.xz.sig
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/5AA3BC334FD7E3369E7C77B291C559DBE4C9123B
Requires:       nginx
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  nginx-mod-devel
# /oreon:deps
%description
The Fancy Index module makes possible the generation of file listings,
like the built-in autoindex module does, but adding a touch of style.
This is possible because the module allows a certain degree of
customization of the generated content:

* Custom headers. Either local or stored remotely.
* Custom footers. Either local or stored remotely.
* Add you own CSS style rules.
* Allow choosing to sort elements by name (default),
  modification time, or size; both ascending (default),
  or descending.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n ngx-fancyindex-%{version}

%build

%nginx_modconfigure
%nginx_modbuild
%install
pushd %{_vpath_builddir}
install -dm 0755 %{buildroot}%{nginx_moddir}
install -pm 0755 ngx_http_fancyindex_module.so %{buildroot}%{nginx_moddir}
popd
install -dm 0755 %{buildroot}%{nginx_modconfdir}
echo 'load_module "%{nginx_moddir}/ngx_http_fancyindex_module.so";' \
    > %{buildroot}%{nginx_modconfdir}/mod-fancyindex.conf
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
