# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 c581e7ae72b2c8bd9421d2ec88cce1c8890f86c3d8fac4a1e7b86b7a4848d416
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           livesys-scripts
Version:        0.8.0
Release:        4%{?dist}
Summary:        Scripts for auto-configuring live media during boot

License:        GPL-3.0-or-later
URL:            https://pagure.io/livesys-scripts
Source0:        https://pagure.io/livesys-scripts/archive/0.8.0/livesys-scripts-0.8.0.tar.gz

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
%oreon_verify_sources
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
