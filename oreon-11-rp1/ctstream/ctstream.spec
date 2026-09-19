%global source0_hash none

Name:           ctstream
Version:        33
Release:        9%{?dist}
Summary:        Get URLs of Czech Television video streams
License:        GPL-1.0-or-later
URL:            http://xpisar.wz.cz/%{name}/
Source0:        %{url}%{name}-%{version}
Source1:        %{url}%{name}-%{version}.asc
# Key exported from Petr Pisar's keyring
Source2:        gpgkey-E3F42FCE156830A80358E6E94FD1AEC3365AF7BF.gpg
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  gnupg2
BuildRequires:  perl-generators
Requires:       perl(LWP::Protocol::https)

%description
Get locators of Czech Television video streams for given web page.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%build
# Empty %%build section for possible RPM hooks

%install
install -d %{buildroot}%{_bindir}
install %{SOURCE0} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/ctstream

%changelog
%autochangelog
