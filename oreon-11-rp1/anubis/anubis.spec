%global source20_hash ff44e2b5ae30417689a1a97e79f88a89e7fc70450444407d9568e7fe66258091
%global source0_hash 5a3f93d5b763283e2432f2574f30d30434befd5e1788990bd031bdf0696e78b3
%bcond check 1
%global goipath         github.com/TecharoHQ/anubis
Version:                1.27.0
%gometa -L -f
Name:           anubis
Release:        1%{?dist}
Summary:        Weighs the soul of incoming HTTP requests to stop AI crawlers
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Source20:       https://github.com/TecharoHQ/anubis/releases/download/v%{version}/anubis-src-vendor-npm-%{version}.tar.gz
# oreon:deps
BuildRequires:  bash
BuildRequires:  brotli
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
BuildRequires:  golang-github-evanw-esbuild
BuildRequires:  gzip
BuildRequires:  make
BuildRequires:  nodejs-cssnano
BuildRequires:  nodejs-cssnano-preset-advanced
BuildRequires:  nodejs-npm
BuildRequires:  nodejs-postcss-url
BuildRequires:  postcss-cli
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
BuildRequires:  zstd
# /oreon:deps
%description
Weighs the soul of incoming HTTP requests to stop AI crawlers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 -a20 %{forgesetupargs}
rm -rf anubis-src-vendor-npm-%{version}/vendor
cp -r anubis-src-vendor-npm-%{version}/* ./
#autopatch -p1

# Neuter vendoring logic in the Makefile
sed -i 's/assets: deps/assets:/' Makefile

%build

%global gomodulesmode GO111MODULE=on
export GO_LDFLAGS="-X 'github.com/TecharoHQ/anubis.Version=%{version}-%{release}'"
%gobuild -o %{gobuilddir}/bin/%{name} %{goipath}/cmd/%{name}
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dpm0644 -t %{buildroot}%{_unitdir}/ run/anubis@.service
install -Dpm0644 -t %{buildroot}%{_sysconfdir}/%{name}/ run/default.env
%oreon_autofiles main

%post

%systemd_post anubis@default.service
%preun

%systemd_preun anubis@default.service
%postun

%systemd_postun_with_restart anubis@default.service
%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
export DONT_USE_NETWORK=1
rm lib/{anubis,http}_test.go
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
