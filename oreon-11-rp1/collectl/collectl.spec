%global source0_hash 6a66b2c1431c72c255031eb446e6548a4109f13cc867480007e632e464c84092
Summary:        A utility to collect various Linux performance data
Name: collectl
Version: 4.3.20.3
Release:        1%{?dist}
License: GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.src.tar.gz
Source1: %{name}.service
Source2: %{name}.sysconfig
URL: http://collectl.sourceforge.net
BuildArch: noarch
Requires: perl(Sys::Syslog), perl(Time::HiRes), perl(Compress::Zlib)
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  perl-generators
BuildRequires:  systemd
# /oreon:deps
%description
A utility to collect Linux performance data

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}

# rename directory for easier inclusion
mv docs html

%build

%install
mkdir -p        $RPM_BUILD_ROOT%{_unitdir} \
                $RPM_BUILD_ROOT%{_sysconfdir} \
                $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig \
                $RPM_BUILD_ROOT%{_bindir} \
                $RPM_BUILD_ROOT%{_datadir}/%{name}/utils \
                $RPM_BUILD_ROOT%{_mandir}/man1/ \
                $RPM_BUILD_ROOT%{_localstatedir}/log/%{name}
install -p -m 755  collectl          $RPM_BUILD_ROOT%{_bindir}/
install -p -m 755  colmux            $RPM_BUILD_ROOT%{_bindir}/
install -p -m 644  *.ph              $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644  envrules.std      $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 755  client.pl         $RPM_BUILD_ROOT%{_datadir}/%{name}/utils
install -p -m 644  man1/*.1          $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 644  collectl.conf     $RPM_BUILD_ROOT%{_sysconfdir}
install -p -m 644  %{SOURCE1}        $RPM_BUILD_ROOT%{_unitdir}
install -p -m 644  %{SOURCE2}        $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
%oreon_autofiles main

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service 
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
