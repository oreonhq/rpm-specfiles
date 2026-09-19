%global source0_hash f300caf9a5710bef0e6b6ead9626c7fd6a904fe20cdc51796cf7d0567d070f38

%if 0%{?el9}
%ifarch ppc64le
%bcond check 1_asan
%else
%bcond check 0_asan
%endif
%else
%bcond check 0_asan
%endif

%if 0%{?el8}
# EPEL 8's unit presets defaults to enabling, avoid it
# i.e. no /usr/lib/systemd/user-preset/99-default-disable.preset
%bcond_with systemd_scriptlets
%else
%bcond_without systemd_scriptlets
%endif

Name:           psi-notify
Version:        1.3.1
Release:        %autorelease
Summary:        Alert when your machine is becoming over-saturated

License:        MIT
URL:            https://github.com/cdown/psi-notify
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        disable-test-asan.diff

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libsystemd)
%if %{with check_asan}
BuildRequires:  libasan
BuildRequires:  libubsan
%endif
# EPEL 8's unit presets defaults to enabling, avoid it
%if %{with systemd_scriptlets}
BuildRequires:  systemd-rpm-macros
%endif

%description
psi-notify is a minimal unprivileged notifier for system-wide resource pressure
using PSI.

This can help you to identify misbehaving applications on your machine before
they start to severely impact system responsiveness, in a way which MemAvailable
or other metrics cannot.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
%if %{without check_asan}
cat %{SOURCE1} | patch -p1
%endif

%build
export CC=gcc
%set_build_flags
%make_build

%install
%make_install DESTDIR=%{buildroot} prefix=%{_prefix}

%if %{with systemd_scriptlets}
%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun_with_restart %{name}.service
%endif

%check
export CC=gcc
%set_build_flags
%make_build test

%files
%license LICENSE
%doc README.md demo.gif
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%dir %{_userunitdir}
%{_userunitdir}/%{name}.service

%changelog
%autochangelog
