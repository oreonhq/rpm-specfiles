%global source0_hash 8660e2eb37d3905ff90ee959fb84fd5921bfc798afba330cc7a32996f695ffbc

Summary: A utility to collect various Linux performance data
Name: collectl
Version: 4.3.5
Release: 10%{?dist}
License: GPL-1.0-or-later OR Artistic-1.0-Perl
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.src.tar.gz
Source1: %{name}.service
Source2: %{name}.sysconfig
URL: http://collectl.sourceforge.net
BuildArch: noarch
BuildRequires: perl-generators
BuildRequires: systemd
Requires: perl(Sys::Syslog), perl(Time::HiRes), perl(Compress::Zlib)
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
A utility to collect Linux performance data

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}

# rename directory for easier inclusion
mv docs html

%build
# nothing to do

%install
# create required directories
mkdir -p        $RPM_BUILD_ROOT%{_unitdir} \
                $RPM_BUILD_ROOT%{_sysconfdir} \
                $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig \
                $RPM_BUILD_ROOT%{_bindir} \
                $RPM_BUILD_ROOT%{_datadir}/%{name}/utils \
                $RPM_BUILD_ROOT%{_mandir}/man1/ \
                $RPM_BUILD_ROOT%{_localstatedir}/log/%{name}

# install the files, setting the mode
install -p -m 755  collectl          $RPM_BUILD_ROOT%{_bindir}/
install -p -m 755  colmux            $RPM_BUILD_ROOT%{_bindir}/
install -p -m 644  *.ph              $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644  envrules.std      $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 755  client.pl         $RPM_BUILD_ROOT%{_datadir}/%{name}/utils
install -p -m 644  man1/*.1          $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 644  collectl.conf     $RPM_BUILD_ROOT%{_sysconfdir}
install -p -m 644  %{SOURCE1}        $RPM_BUILD_ROOT%{_unitdir}
install -p -m 644  %{SOURCE2}        $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service 

%files
%doc ARTISTIC COPYING GPL RELEASE-collectl html
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_bindir}/%{name}
%{_bindir}/colmux
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/colmux.1*
%{_localstatedir}/log/%{name}/

%changelog
%autochangelog
