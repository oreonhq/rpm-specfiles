%global source0_hash 6f94f3ae4558e82388611ea485225e63f01493647ac2ad5ef8c010aecd57d655

Name:           python-exabgp
Version:        5.0.5
Release:        1%{?dist}
Summary:        The BGP swiss army knife of networking (Library)

License:        BSD-3-Clause
URL:            https://github.com/Exa-Networks/exabgp
Source0:        https://github.com/Exa-Networks/exabgp/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        exabgp.sysusers.exabgp.conf
Source2:        exabgp.tmpfiles.exabgp.conf
Source3:        exabgp.systemd.exabgp.service
Source4:        exabgp.systemd.exabgp@.service
Patch0100:      0100-Adjust-python-versions.patch

BuildArch:      noarch

%description
ExaBGP python module

%package -n python3-exabgp
Summary:        The BGP swiss army knife of networking
BuildRequires:  python3-devel
Requires:       python3 >= 3.8.1
Obsoletes:      python2-exabgp <= %{version}
%{?python_provide:%python_provide python3-exabgp}
# Test dependencies:
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(psutil)

%description -n python3-exabgp
The BGP swiss army knife of networking

%package -n exabgp
Summary:        The BGP swiss army knife of networking
BuildRequires:  systemd-rpm-macros
Requires:       systemd
Requires:       python3-exabgp = %{version}-%{release}

%description -n exabgp
The BGP swiss army knife of networking (exabgp systemd unit)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n exabgp-%{version}

%generate_buildrequires
%pyproject_buildrequires -p

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files exabgp

# Install health check with non-generic name
install -p -m 0755 bin/healthcheck %{buildroot}%{_bindir}/exabgphealthcheck

# Install exabgpcli
install -p -m 0755 bin/exabgpcli %{buildroot}%{_bindir}/

# Configure required directories for the exabgp service
mkdir -p %{buildroot}%{_sysconfdir}/exabgp

# Install exabgp systemd unit files
mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/exabgp.service
install -p -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/exabgp@.service

# Install man pages
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 0644 doc/man/exabgp.1 %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{_mandir}/man5
install -p -m 0644 doc/man/exabgp.conf.5 %{buildroot}%{_mandir}/man5/

# Install sysusers.d files
mkdir -p %{buildroot}%{_sysusersdir}
install -p -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/exabgp.conf

# Install tmpfiles.d files
mkdir -p %{buildroot}%{_tmpfilesdir}
install -p -m 0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/exabgp.conf

# Remove examples
rm -rf %{buildroot}%{_usr}/etc

%check
%pyproject_check_import -t
%pytest --cov --cov-reset tests/unit

%pre -n exabgp
%sysusers_create_package exabgp %{SOURCE1}
%tmpfiles_create_package exabgp %{SOURCE2}

%post -n exabgp
%systemd_post exabgp.service

%preun -n exabgp
%systemd_preun exabgp.service

%postun -n exabgp
%systemd_postun_with_restart exabgp.service

%files -n python3-exabgp -f %{pyproject_files}
%doc README.md
%license LICENCE.txt

%files -n exabgp
%{_bindir}/exabgpcli
%{_bindir}/exabgp-cli
%{_bindir}/exabgp
%{_bindir}/exabgp-healthcheck
%{_bindir}/exabgphealthcheck
%dir %{_sysconfdir}/exabgp
%{_unitdir}/exabgp.service
%{_unitdir}/exabgp@.service
%{_mandir}/man1/exabgp.1{,.*}
%{_mandir}/man5/exabgp.conf.5{,.*}
%{_sysusersdir}/exabgp.conf
%{_tmpfilesdir}/exabgp.conf

%changelog
%autochangelog
