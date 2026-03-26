Summary:        Oreon package repositories
Name:           oreon-repos
Version:        11
Release:        3%{?dist}
License:        MIT
URL:            https://oreonhq.com/

Provides:       oreon-repos(%{version}) = %{release}
Requires:       system-release(43)
Requires:       oreon-gpg-keys >= %{version}-%{release}
BuildArch:      noarch

Source1:        oreon.repo
Source10:       RPM-GPG-KEY-oreon-11-primary

%description
Oreon package repository configuration and GPG keys.

%package -n oreon-gpg-keys
Summary:        Oreon RPM GPG keys
Requires:       filesystem >= 3.18-6

%description -n oreon-gpg-keys
GPG keys for Oreon 11 package verification.

%prep

%build

%install
# Install GPG keys
install -d -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
install -m 644 %{SOURCE10} $RPM_BUILD_ROOT/etc/pki/rpm-gpg/

# Create arch-specific key symlinks
pushd $RPM_BUILD_ROOT/etc/pki/rpm-gpg/
ln -s RPM-GPG-KEY-oreon-11-primary RPM-GPG-KEY-oreon-11-x86_64
ln -s RPM-GPG-KEY-oreon-11-primary RPM-GPG-KEY-oreon-11-noarch
popd

# Install repo config
install -d -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/etc/yum.repos.d/oreon.repo

%files
%dir /etc/yum.repos.d
%config(noreplace) /etc/yum.repos.d/oreon.repo

%files -n oreon-gpg-keys
%dir /etc/pki/rpm-gpg
/etc/pki/rpm-gpg/RPM-GPG-KEY-oreon-*

%changelog
* Mon Jan 06 2026 Oreon HQ Packaging Team <packaging@oreonhq.com> - 11-1
- Oreon 11
