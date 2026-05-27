%global source0_hash none

%bcond_without httpd
%bcond_without nginx

Name:           web-assets
Version:        5
Release:        25%{?dist}
Summary:        A simple framework for bits pushed to browsers
License:        MIT
URL:            https://fedoraproject.org/wiki/User:Patches/PackagingDrafts/Web_Assets
Source0:        LICENSE
Source1:        README.devel
Source2:        macros.web-assets
Source3:        httpd-web-assets.conf
Source4:        nginx-web-assets.conf
BuildArch:      noarch
BuildRequires:  coreutils

%description
%{summary}.

%package filesystem
Summary:        The basic directory layout for Web Assets
#there's nothing copyrightable about a few directories and symlinks
License:        LicenseRef-Not-Copyrightable
Requires:       fonts-filesystem

%description filesystem
%{summary}.

%package devel
Summary:        RPM macros for Web Assets packaging
License:        MIT
Requires:       web-assets-filesystem = %{version}-%{release}

%description devel
%{summary}.

%if %{with httpd}
%package httpd
Summary:        Web Assets aliases for the Apache HTTP daemon
License:        MIT
Requires:       web-assets-filesystem = %{version}-%{release}
Requires:       httpd

%description httpd
%{summary}.
%endif

%if %{with nginx}
%package nginx
Summary:        Web Assets aliases for the nginx daemon
License:        MIT
Requires:       web-assets-filesystem = %{version}-%{release}
Requires:       nginx

%description nginx
%{summary}.
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -c -T
cp %{SOURCE0} LICENSE
cp %{SOURCE1} README.devel

%build
#nothing to do

%install
mkdir -p %{buildroot}%{_datadir}/web-assets
mkdir -p %{buildroot}%{_datadir}/javascript
ln -sf ../javascript %{buildroot}%{_datadir}/web-assets/javascript
ln -sf ../javascript %{buildroot}%{_datadir}/web-assets/js
ln -sf ../fonts %{buildroot}%{_datadir}/web-assets/fonts
install -Dpm0644 %{SOURCE2} %{buildroot}%{_rpmconfigdir}/macros.d/macros.web-assets
%if %{with httpd}
install -Dpm0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/httpd/conf.d/web-assets.conf
%endif
%if %{with nginx}
install -Dpm0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/nginx/default.d/web-assets.conf
%endif

%if %{with httpd}
%post httpd
[ -x %{_bindir}/systemctl ] && reload-or-try-restart httpd.service || :

%postun httpd
[ -x %{_bindir}/systemctl ] && reload-or-try-restart httpd.service || :
%endif

%if %{with nginx}
%post nginx
[ -x %{_bindir}/systemctl ] && systemctl reload-or-try-restart nginx.service || :

%postun nginx
[ -x %{_bindir}/systemctl ] && systemctl reload-or-try-restart nginx.service || :
%endif

%files filesystem
%{_datadir}/web-assets
%{_datadir}/javascript

%files devel
%{_rpmconfigdir}/macros.d/macros.web-assets
%license LICENSE
%doc README.devel

%if %{with httpd}
%files httpd
%config(noreplace) %{_sysconfdir}/httpd/conf.d/web-assets.conf
%license LICENSE
%endif

%if %{with nginx}
%files nginx
%config(noreplace) %{_sysconfdir}/nginx/default.d/web-assets.conf
%license LICENSE
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5-25
- Prepare for Oreon 11 (RP1)
