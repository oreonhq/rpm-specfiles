%global source0_hash 6b102492d7d328c75c9354bf0e81de8495e54fa25264aba5173b47d04650b422
Name:           btrfs-backup-ng
Version:        0.9.12
Release:        1%{?dist}
Summary:        Intelligent, feature-rich backups for btrfs
License:        MIT
URL:            https://github.com/berrym/btrfs-backup-ng
Source0:        https://files.pythonhosted.org/packages/source/b/btrfs_backup_ng/btrfs_backup_ng-%{version}.tar.gz
BuildArch:      noarch
Requires:       btrfs-progs
Requires:       openssh-clients
Requires:       pv
Requires:       gzip
Requires:       bzip2
Requires:       zstd
Requires:       xz
Requires:       lz4
Requires:       lzo
Requires:       pigz
Requires:       pbzip2
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0
Requires:       python3-btrfs-backup-ng = %{version}-%{release}
# /oreon:deps
%package -n       python3-btrfs-backup-ng+test
Summary:        Metapackage for python3-btrfs-backup-ng test extras
Requires:       python3-btrfs-backup-ng = %{version}-%{release}
Requires:       python3dist(pytest) >= 7.0
Requires:       python3dist(pytest-cov) >= 4.0
Requires:       python3dist(pytest-asyncio) >= 0.23.0
Provides:       python3dist(btrfs-backup-ng[test]) = %{version}-%{release}

%description -n python3-btrfs-backup-ng+test
Metapackage for python3-btrfs-backup-ng test extras.

%package -n       python3-btrfs-backup-ng+dev
Summary:        Metapackage for python3-btrfs-backup-ng dev extras
Requires:       python3-btrfs-backup-ng = %{version}-%{release}
Requires:       python3dist(pytest) >= 7.0
Requires:       python3dist(pytest-cov) >= 4.0
Requires:       python3dist(pytest-asyncio) >= 0.23.0
Requires:       python3dist(ruff) >= 0.15.0
Requires:       python3dist(ruff) < 0.16.0
Requires:       python3dist(mypy) >= 1.0
Provides:       python3dist(btrfs-backup-ng[dev]) = %{version}-%{release}

%description -n python3-btrfs-backup-ng+dev
Metapackage for python3-btrfs-backup-ng dev extras.

%description
Complete btrfs backup solution with automated snapshots,
incremental transfers, restore functionality,
snapper integration, btrbk migration, and systemd scheduling

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir btrfs_backup_ng-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
install -d %{buildroot}%{_mandir}/man1
install -m 0644 man/man1/btrfs*.1* %{buildroot}%{_mandir}/man1
%define bash_compdir  %{_prefix}/share/bash-completions/completions
%define zsh_compdir   %{_prefix}/share/zsh/site-functions
%define fish_compdir  %{_prefix}/share/fish/vendor_completions.d
install -d %{buildroot}%{bash_compdir}
install -d %{buildroot}%{zsh_compdir}
install -d %{buildroot}%{fish_compdir}
install -m 0644 completions/btrfs-backup-ng.bash %{buildroot}%{bash_compdir}/btrfs-backup-ng
install -m 0644 completions/btrfs-backup-ng.zsh  %{buildroot}%{zsh_compdir}/_btrfs-backup-ng
install -m 0644 completions/btrfs-backup-ng.fish %{buildroot}%{fish_compdir}/btrfs-backup-ng.fish
%oreon_autofiles main

%check

%{pytest}
%files

%changelog

%autochangelog
