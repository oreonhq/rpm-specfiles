%global source0_hash 9332a884c559fbcf96cbe2c1b46312eb1e1b7191eb9a73a3d3b857d4e9789eb1
%ifnarch s390x
%bcond check 0
%endif
%global goipath         github.com/Shopify/toxiproxy
Version:                2.12.0
%gometa
%global godevelheader %{expand:
Obsoletes:      golang-github-Shopify-toxiproxy-devel < 2.1.3-3
}
%global common_description %{expand:
Toxiproxy is a framework for simulating network conditions. It's made
specifically to work in testing, CI and development environments, supporting
deterministic tampering with connections, but with support for randomized
chaos and customization. Toxiproxy is the tool you need to prove with tests
that your application doesn't have single points of failure.
Toxiproxy usage consists of two parts. A TCP proxy written in Go (what this
repository contains) and a client communicating with the proxy over HTTP. You
configure your application to make all test connections go through Toxiproxy
and can then manipulate their health via HTTP. See Usage below on how to set
up your project.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md CREATING_TOXICS.md README.md README-client.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        TCP proxy to simulate network and system conditions for resiliency testing
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/toxiproxy-%{version}.tar.gz
Source1:        toxiproxy-server.1
Source2:        toxiproxy-cli.1
Source3:        toxiproxy.default
Source4:        toxiproxy.service
Source5:        toxiproxy.logrotate
%{?systemd_requires}
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%package -n       toxiproxy
Summary:        TCP proxy to simulate network and system conditions for resiliency testing
BuildArch:      noarch

%description -n toxiproxy
TCP proxy to simulate network and system conditions for resiliency testing

%description
%{common_description}

%package -n toxiproxy
Summary:        TCP proxy to simulate network and system conditions for resiliency testing
%description -n toxiproxy
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
mv client/README.md README-client.md

# Create a sysusers.d config file
cat >golang-github-shopify-toxiproxy.sysusers.conf <<EOF
u toxiproxy - 'Toxiproxy-server account' %{_sharedstatedir}/toxiproxy -
EOF

%build

%gobuild -o %{gobuilddir}/bin/toxiproxy-cli     %{goipath}/cli
%gobuild -o %{gobuilddir}/bin/toxiproxy-server  %{goipath}/cmd
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -d -m 0755 %{buildroot}%{_mandir}/man1
install -p -m 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/toxiproxy-server.1
install -p -m 0644 %{SOURCE2} %{buildroot}%{_mandir}/man1/toxiproxy-cli.1
install -d -m 0755 %{buildroot}%{_sysconfdir}/default
install -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/default/toxiproxy
install -d -m 0755 %{buildroot}%{_unitdir}
install -p -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/toxiproxy.service
install -d -m 0755 %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/logrotate.d/toxiproxy
install -d -m 0755 %{buildroot}%{_sharedstatedir}/toxiproxy
install -d -m 0755 %{buildroot}%{_localstatedir}/log/toxiproxy
install -m0644 -D golang-github-shopify-toxiproxy.sysusers.conf %{buildroot}%{_sysusersdir}/golang-github-shopify-toxiproxy.conf
%oreon_autofiles toxiproxy usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%gocheck
%endif
%post  -n toxiproxy

%systemd_post toxiproxy.service
%preun  -n toxiproxy

%systemd_preun toxiproxy.service
%postun  -n toxiproxy

%systemd_postun_with_restart toxiproxy.service
%files -f %{oreon_filedir}/main.list
%files -n toxiproxy -f %{oreon_filedir}/toxiproxy.list

%changelog

%autochangelog
