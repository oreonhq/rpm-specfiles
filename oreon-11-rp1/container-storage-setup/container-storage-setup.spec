%global source0_hash 20544aa14858ffddcd9943b02c12483368208fb58aacbb84f43792c0cdb1ea78

%global git0 https://github.com/projectatomic/%{name}
%global csslibdir %{_datadir}/%{name}
%global commit0 413b4080c0b9346a242d88137bb3e9e0a6aa25f9
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: container-storage-setup
Version: 0.11.0
Release: 21.dev.git%{shortcommit0}%{?dist}
Summary: A simple service to setup container storage devices
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: %{git0}
Source0: %{git0}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
BuildArch: noarch
BuildRequires: git
BuildRequires: make
Requires: lvm2
Requires: xfsprogs
Requires: parted

%description
This is a simple service to configure Container Runtimes to use an LVM-managed
thin pool.  It also supports auto-growing both the pool as well
as the root logical volume and partition table.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -Sgit -n %{name}-%{commit0}

%build

%install
install -dp %{buildroot}%{_datadir}/%{name}
install -dp %{buildroot}%{_mandir}/man1
install -D -p -m 755 %{name}.sh %{buildroot}%{_bindir}/%{name}
install -p -m 644 %{name}.conf %{buildroot}%{csslibdir}/%{name}
install -p -m 755 libcss.sh %{buildroot}/%{csslibdir}
install -p -m 755 css-child-read-write.sh %{buildroot}/%{csslibdir}/css-child-read-write
install -p -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
#%{__make} install-core DESTDIR=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%dir %{csslibdir}
%{_mandir}/man1/%{name}.1*
%{csslibdir}/%{name}
%{csslibdir}/css-child-read-write
%{csslibdir}/libcss.sh

%changelog
%autochangelog
