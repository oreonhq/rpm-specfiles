%global source0_hash f5bb864aef9ff41bff17d5fdf207903bffd6c4d2d6d30e5742fc9e7e0021c60c
Name:           noggin
Version:        1.11.0
Release:        1%{?dist}
Summary:        Self-service user portal for FreeIPA for communities
License:        MIT
URL:            https://noggin-aaa.readthedocs.io/
Source0:        https://github.com/fedora-infra/noggin/archive/v%{version}/%{name}-%{version}.tar.gz
Source10:       noggin-README.Fedora
BuildArch:      noarch
Requires:       nginx-filesystem
Requires:       (python3dist(gunicorn) with /usr/bin/gunicorn-3)
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-noggin = %{version}-%{release}
# /oreon:deps
%package -n       python3-noggin+deploy
Summary:        Metapackage for python3-noggin deploy extras
Requires:       python3-noggin = %{version}-%{release}
Requires:       python3dist(gunicorn) (>=20.0
Requires:       python3dist(gunicorn) < 24.0.0)
Provides:       python3dist(noggin[deploy]) = %{version}-%{release}

%description -n python3-noggin+deploy
Metapackage for python3-noggin deploy extras.

%description
Noggin is a self-service portal for FreeIPA.

The primary purpose of the portal is to allow users to sign up
and manage their account information and group membership.

%package theme-fas
Summary:        Fedora Account System theme for Noggin
Requires:       %{name} = %{version}-%{release}
%description theme-fas
Provides a theme for Noggin used for the Fedora Account System.

%package theme-centos
Summary:        CentOS Accounts theme for Noggin
Requires:       %{name} = %{version}-%{release}
%description theme-centos
Provides a theme for Noggin used for CentOS Accounts.

%package theme-openSUSE
Summary:        openSUSE Accounts theme for Noggin
Requires:       %{name} = %{version}-%{release}
%description theme-openSUSE
Provides a theme for Noggin used for openSUSE Accounts.

%prep

%autosetup -n %{name}-%{version} -p1

# Allow markupsafe 3 and newer
sed -i "/^markupsafe/s/\^/>=/" pyproject.toml

# Install README.Fedora file
install -pm 0644 %{SOURCE10} README.Fedora

%build

%pyproject_wheel
%install
%pyproject_install
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 deployment/scripts/sar.py %{buildroot}%{_bindir}/noggin-sar
%py3_shebang_fix %{buildroot}%{_bindir}/noggin-sar
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}%{_localstatedir}/log/noggin
install -pm 0644 deployment/noggin.service %{buildroot}%{_unitdir}/%{name}.service
install -pm 0644 deployment/noggin.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{name}
touch %{buildroot}%{_sysconfdir}/%{name}/%{name}.cfg
touch %{buildroot}%{_localstatedir}/log/noggin/access.log
touch %{buildroot}%{_localstatedir}/log/noggin/error.log
mkdir -p %{buildroot}%{_sysconfdir}/nginx/conf.d
install -pm 0644 deployment/nginx.conf %{buildroot}%{_sysconfdir}/nginx/conf.d/noggin.conf
mkdir -p %{buildroot}%{_localstatedir}/log/nginx
touch %{buildroot}%{_localstatedir}/log/nginx/noggin.access.log
touch %{buildroot}%{_localstatedir}/log/nginx/noggin.error.log
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files
%files -n noggin-theme-fas -f %{oreon_filedir}/noggin-theme-fas.list
%files -n noggin-theme-centos -f %{oreon_filedir}/noggin-theme-centos.list
%files -n noggin-theme-openSUSE -f %{oreon_filedir}/noggin-theme-openSUSE.list

%changelog

%autochangelog
