%global source0_hash 4511d2fa6d8b1631e7b5b7a76015f980abfdc3a6d6a9783a9f9e7ed4b5cab954

Name:          initoverlayfs
Version:       0.995
Release:       5%{?dist}
Summary:       An initial scalable filesystem for Linux operating systems
License:       GPL-2.0-only
URL:           https://github.com/containers/initoverlayfs
Source0:       %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: libblkid-devel
Recommends: lz4
Recommends: gzip
Requires: erofs-utils
Requires: dracut

%global debug_package %{nil}

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build
RPM_OPT_FLAGS="${RPM_OPT_FLAGS/-flto=auto /}"
gcc ${RPM_OPT_FLAGS} -lblkid initoverlayfs.c -o initoverlayfs

%install
install -D -m755 bin/initoverlayfs-install ${RPM_BUILD_ROOT}/%{_bindir}/initoverlayfs-install
install -D -m755 initoverlayfs ${RPM_BUILD_ROOT}/%{_sbindir}/initoverlayfs
install -D -m755 lib/dracut/modules.d/81initoverlayfs/module-setup.sh ${RPM_BUILD_ROOT}/%{_prefix}/lib/dracut/modules.d/81initoverlayfs/module-setup.sh
install -D -m644 lib/systemd/system/pre-initoverlayfs.target ${RPM_BUILD_ROOT}/%{_prefix}/lib/systemd/system/pre-initoverlayfs.target
install -D -m644 lib/systemd/system/pre-initoverlayfs.service ${RPM_BUILD_ROOT}/%{_prefix}/lib/systemd/system/pre-initoverlayfs.service
install -D -m644 lib/systemd/system/pre-initoverlayfs-switch-root.service ${RPM_BUILD_ROOT}/%{_prefix}/lib/systemd/system/pre-initoverlayfs-switch-root.service
install -D -m755 lib/kernel/install.d/94-initoverlayfs.install ${RPM_BUILD_ROOT}/%{_prefix}/lib/kernel/install.d/94-initoverlayfs.install

%files
%license LICENSE
%doc README.md
%attr(0755,root,root)
%{_bindir}/initoverlayfs-install
%{_sbindir}/initoverlayfs
%{_prefix}/lib/dracut/modules.d/81initoverlayfs/
%{_prefix}/lib/systemd/system/pre-initoverlayfs.target
%{_prefix}/lib/systemd/system/pre-initoverlayfs.service
%{_prefix}/lib/systemd/system/pre-initoverlayfs-switch-root.service
%{_prefix}/lib/kernel/install.d/94-initoverlayfs.install

%changelog
%autochangelog
