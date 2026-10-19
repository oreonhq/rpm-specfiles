%global source0_hash cd35166b2725e0b12f675d3045d1722ac2a0bc97aa1a39a92c30f09019f5c2b9
%global forgeurl        https://github.com/trbs/bucky
%global commit          cda507241c8898c3a1926cae18371bce84be6d2c
%global forgesetupargs  -n bucky-%{commit}
Name:           python-bucky
Version:        2.3.1
Release:        1%{?dist}
Summary:        CollectD and StatsD adapter for Graphite
%forgemeta
License:        Apache-2.0
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{commit}/bucky-%{commit}.tar.gz
Source1:        python-bucky-example.conf
Source2:        python-bucky-supervisord-example.conf
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-bucky
Summary: %summary
Requires:       collectd
Requires:       python3-six
Requires:       python3-setuptools
Requires:       python3-watchdog
Requires:       python3-setproctitle
Requires:       python3-cryptography
%{?python_provide:%python_provide python3-bucky}
%description -n python3-bucky

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup
%{__install} -m 644 %{SOURCE2} .

# Create a sysusers.d config file
cat >python-bucky.sysusers.conf <<EOF
u bucky - 'Bucky daemon' - -
EOF

%build

%py3_build
%install
rm -rf %{_bindir}/bucky
%py3_install
%{__mkdir_p} %{buildroot}%{_localstatedir}/log/bucky
%{__mkdir_p} %{buildroot}%{_localstatedir}/run/bucky
%{__mkdir_p} %{buildroot}%{_sysconfdir}/bucky
%{__install} -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/bucky/bucky.conf
install -m0644 -D python-bucky.sysusers.conf %{buildroot}%{_sysusersdir}/python-bucky.conf
%oreon_autofiles python3-bucky usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-bucky -f %{oreon_filedir}/python3-bucky.list

%changelog

%autochangelog
