Name:           livesys-scripts
Version:        0.8.0
Release:        4%{?dist}
Summary:        Scripts for auto-configuring live media during boot

License:        GPL-3.0-or-later
URL:            https://pagure.io/livesys-scripts
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# https://pagure.io/livesys-scripts/pull-request/28
# https://bugzilla.redhat.com/show_bug.cgi?id=2240823
# Fix installer launch on i3
Patch0:         0001-livesys-i3-restore-the-hack-to-fix-the-installer.patch

BuildRequires:  systemd-rpm-macros
BuildRequires:  make

BuildArch:      noarch


%description
%{summary}.


%prep
%autosetup -p1


%build
# Nothing to do

%install
%make_install

# Make ghost files
mkdir -p %{buildroot}%{_sharedstatedir}/livesys
touch %{buildroot}%{_sharedstatedir}/livesys/livesys-session-extra
touch %{buildroot}%{_sharedstatedir}/livesys/livesys-session-late-extra


%preun
%systemd_preun livesys.service livesys-late.service


%post
%systemd_post livesys.service livesys-late.service


%postun
%systemd_postun livesys.service livesys-late.service


%files
%license COPYING
%doc README.md
%config(noreplace) %{_sysconfdir}/sysconfig/livesys
%{_libexecdir}/livesys/
%{_unitdir}/livesys*
%dir %{_sharedstatedir}/livesys
%ghost %{_sharedstatedir}/livesys/livesys-session-extra
%ghost %{_sharedstatedir}/livesys/livesys-session-late-extra


%changelog
* Wed Apr 8 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8.0-4
- Prepare for Oreon 11 (RP1)
