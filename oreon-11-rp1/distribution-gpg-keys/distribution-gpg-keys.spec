%global source0_hash none

Name:		distribution-gpg-keys
Version:	1.118
Release:	1%{?dist}
Summary:	GPG keys of various Linux distributions

License:	CC0-1.0
URL:		https://github.com/rpm-software-management/distribution-gpg-keys
# Sources can be obtained by
# git git://github.com/rpm-software-management/distribution-gpg-keys.git
# cd distribution-gpg-keys
# tito build --tgz
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

%if 0%{?fedora} > 0
Suggests:	ubu-keyring
Suggests:	debian-keyring
Suggests:	archlinux-keyrings
Suggests:   %{name}-copr
%endif

%description
GPG keys used by various Linux distributions to sign packages.

%package copr
Summary: GPG keys for Copr projects
BuildArch: noarch

%description copr
GPG keys used by Copr projects.

%prep
%setup -q

%build
#nothing to do here

%install
mkdir -p %{buildroot}%{_datadir}/%{name}/
cp -a keys/* %{buildroot}%{_datadir}/%{name}/

%files
%license LICENSE
%doc README.md SOURCES.md
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/copr

%files copr
%license LICENSE
%{_datadir}/%{name}/copr

%changelog
%autochangelog
