%global source0_hash 6391587ae54ca243760e3ecc08032ab0bdfb3b8dbb234f5cf5b9ba5b2409929a
%global commithash da6852df4103492f9136ef814cda0c7d402e0a90
%global origname ngx_http_js_challenge_module
Name:          nginx-mod-js-challenge
Summary:        Simple JavaScript proof-of-work based access for Nginx with virtually no overhead
URL:           https://github.com/simon987/%{origname}
License:       GPL-3.0-or-later
Version:       0^20230517.git%(echo %{commithash}|head -c7)
Release:        1%{?dist}
Source0:        https://github.com/simon987/%{origname}/archive/%{commithash}.zip
Requires:      nginx(abi)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  nginx-mod-devel
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{origname}-%{commithash}

%build

%nginx_modconfigure
%nginx_modbuild
%install
pushd %{_vpath_builddir}
install -dm 0755 %{buildroot}%{nginx_moddir}
install -pm 0755 %{origname}.so %{buildroot}%{nginx_moddir}
install -dm 0755 %{buildroot}%{nginx_modconfdir}
echo 'load_module "%{nginx_moddir}/%{origname}.so";' \
    > %{buildroot}%{nginx_modconfdir}/mod-js-challenge.conf
popd
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
