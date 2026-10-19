%global source0_hash e704978368c6f72f14dfc1e93806e2917f154f1184a9fe46162291c500dbd962
Name:           borgmatic
Version:        2.1.9
Release:        1%{?dist}
Summary:        Simple Python wrapper script for borgbackup
License:        GPL-3.0-or-later
URL:            https://torsion.org/borgmatic
Source0:        https://projects.torsion.org/borgmatic-collective/borgmatic/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       borgbackup
Suggests:       mysql
Suggests:       postgresql
Suggests:       sqlite
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-borgmatic = %{version}-%{release}
# /oreon:deps
%package -n       python3-borgmatic+Apprise
Summary:        Metapackage for python3-borgmatic Apprise extras
Requires:       python3-borgmatic = %{version}-%{release}
Provides:       python3dist(borgmatic[Apprise]) = %{version}-%{release}

%description -n python3-borgmatic+Apprise
Metapackage for python3-borgmatic Apprise extras.

%package -n       python3-borgmatic+browse
Summary:        Metapackage for python3-borgmatic browse extras
Requires:       python3-borgmatic = %{version}-%{release}
Provides:       python3dist(borgmatic[browse]) = %{version}-%{release}

%description -n python3-borgmatic+browse
Metapackage for python3-borgmatic browse extras.

%package -n       python3-borgmatic+browse-dev
Summary:        Metapackage for python3-borgmatic browse-dev extras
Requires:       python3-borgmatic = %{version}-%{release}
Provides:       python3dist(borgmatic[browse-dev]) = %{version}-%{release}

%description -n python3-borgmatic+browse-dev
Metapackage for python3-borgmatic browse-dev extras.

%description
borgmatic (formerly atticmatic) is a simple Python wrapper script for
the Borg backup software that initiates a backup, prunes any old backups
according to a retention policy, and validates backups for consistency.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}
%oreon_prep
%build

%pyproject_wheel
%{__python3} -c 'from borgmatic.commands.completion.bash import bash_completion; print(bash_completion())' > %{name}-bash-completion
%install
%pyproject_install
install -dm 0750 %{buildroot}%{_sysconfdir}/borgmatic
install -dm 0750 %{buildroot}%{_sysconfdir}/borgmatic.d
sed -i 's#/root/.local/bin/borgmatic#%{_bindir}/%{name}#' sample/systemd/%{name}.service
install -Dpm 0644 sample/systemd/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -Dpm 0644 sample/systemd/%{name}.timer %{buildroot}%{_unitdir}/%{name}.timer
install -Dpm 0644 %{name}-bash-completion %{buildroot}%{_datadir}/bash-completion/completions/%{name}
%oreon_autofiles main

%post

%systemd_post borgmatic.timer
%preun

%systemd_preun borgmatic.timer
%postun

%systemd_postun borgmatic.timer
%files

%changelog

%autochangelog
