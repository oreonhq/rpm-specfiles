%global source0_hash 852defe7743c12984c632f9882c21384382a58fd34b740a154b04451f7ffc896

Name:           borgmatic
Version:        2.1.3
Release:        %autorelease
Summary:        Simple Python wrapper script for borgbackup

License:        GPL-3.0-or-later
URL:            https://torsion.org/borgmatic
Source0:        https://projects.torsion.org/borgmatic-collective/borgmatic/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros

Requires:       borgbackup
# These hints are for commands run as part of the database backup and restore
# hooks. It is assumed that users who configure these hooks will already have
# the respective DBMS installed, otherwise there'd be nothing to back up.
# Leaving this here for posterity.
Suggests:       mysql
Suggests:       postgresql
Suggests:       sqlite

%description
borgmatic (formerly atticmatic) is a simple Python wrapper script for
the Borg backup software that initiates a backup, prunes any old backups
according to a retention policy, and validates backups for consistency.

%generate_buildrequires
%pyproject_buildrequires

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}

%build
%pyproject_wheel

%{__python3} -c 'from borgmatic.commands.completion.bash import bash_completion; print(bash_completion())' > %{name}-bash-completion

%install
%pyproject_install
%pyproject_save_files %{name}

install -dm 0750 %{buildroot}%{_sysconfdir}/borgmatic
install -dm 0750 %{buildroot}%{_sysconfdir}/borgmatic.d

sed -i 's#/root/.local/bin/borgmatic#%{_bindir}/%{name}#' sample/systemd/%{name}.service
install -Dpm 0644 sample/systemd/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -Dpm 0644 sample/systemd/%{name}.timer %{buildroot}%{_unitdir}/%{name}.timer

install -Dpm 0644 %{name}-bash-completion %{buildroot}%{_datadir}/bash-completion/completions/%{name}

%files -f %{pyproject_files}
%doc AUTHORS NEWS README.md
%license LICENSE
%attr(0750, root, root) %{_sysconfdir}/borgmatic
%attr(0750, root, root) %{_sysconfdir}/borgmatic.d
%{_bindir}/borgmatic
%{_bindir}/generate-borgmatic-config
%{_bindir}/validate-borgmatic-config
%{_datadir}/bash-completion/completions/%{name}
%{_unitdir}/borgmatic.service
%{_unitdir}/borgmatic.timer

%post
%systemd_post borgmatic.timer

%preun
%systemd_preun borgmatic.timer

%postun
%systemd_postun borgmatic.timer

%changelog
%autochangelog
