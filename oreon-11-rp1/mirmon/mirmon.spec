%global source0_hash db02edd28f785cf1662e42134cc5bcc35acc1689719c2b69310b4416c3798e67

Name:           mirmon
Version:        2.11
Release:        22%{?dist}
Summary:        Monitor the status of mirrors
License:        MIT
URL:            http://www.staff.science.uu.nl/~penni101/mirmon/
Source0:        http://www.staff.science.uu.nl/~penni101/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}-httpd.conf
BuildArch:      noarch
BuildRequires:  perl-generators

%description
Many software projects are mirrored worldwide. The mirror sites are required 
to update the mirror archive regularly (daily, weekly) from a root server.

Mirmon helps administrators in keeping an eye on the mirror sites. In a 
concise graphic format, mirmon shows each site's status history of the 
last two weeks. It is easy to spot stale or dead mirrors.

%package        httpd
Summary:        Apache configuration for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       httpd

%description    httpd
This package provides the Apache configuration for
applications using an Alias to %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
# Nothing to build.

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1
install -pm644 %{name}.1 %{buildroot}%{_mandir}/man1/
install -pm644 %{name}.pm.1 %{buildroot}%{_mandir}/man1/
install -pDm755 %{name} %{buildroot}%{_bindir}/%{name}
install -pDm755 probe %{buildroot}%{_bindir}/probe
install -pDm0644 %{S:1} %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf
cp -pa countries.list icons %{buildroot}%{_datadir}/%{name}/

%files
%license LICENSE
%doc RELEASE-NOTES *.{txt,html}
%{_bindir}/%{name}
%{_bindir}/probe
%{_datadir}/%{name}
%{_mandir}/man1/%{name}*.1*

%files httpd
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf

%changelog
%autochangelog
