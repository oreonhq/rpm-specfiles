%global source0_hash 34761bae1a23c58192281a5115fb07fbf22c9b0133c08166beffc70fed3ebc12

Name:		supervisor
Version:	4.2.5
Release:	%autorelease
Summary:	A system for allowing the control of process state on UNIX

License:	BSD-3-Clause AND MIT
URL:		http://supervisord.org
Source0:	https://pypi.python.org/packages/source/s/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}d.service
Source2:	%{name}d.conf
Source3:	%{name}.logrotate
Source4:	%{name}.tmpfiles

Patch0:		pytest.patch

BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	systemd-units

%description
The supervisor is a client/server system that allows its users to control a
number of processes on UNIX-like operating systems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
%py3_shebang_fix supervisor/scripts

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

mkdir -p %{buildroot}/%{_sysconfdir}
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}d.d
mkdir -p %{buildroot}/%{_sysconfdir}/logrotate.d/
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/%{_localstatedir}/log/%{name}
mkdir -p %{buildroot}/%{_rundir}/%{name}
chmod 755 %{buildroot}/%{_localstatedir}/log/%{name}
install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}d.service
install -p -m 644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/%{name}d.conf
install -p -m 644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/%{name}.conf

%check	
%pytest -v

%post
%systemd_post %{name}d.service

%preun
%systemd_preun %{name}d.service

%postun
%systemd_postun_with_restart %{name}d.service

%files -n supervisor -f %{pyproject_files}
%doc CHANGES.rst README.rst
%license COPYRIGHT.txt LICENSES.txt
%dir %{_localstatedir}/log/%{name}
%{_unitdir}/%{name}d.service
%{_bindir}/%{name}*
%{_bindir}/echo_supervisord_conf
%{_bindir}/pidproxy
%{_tmpfilesdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}d.conf
%dir %{_sysconfdir}/%{name}d.d
%dir %{_rundir}/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}

%changelog
%autochangelog
