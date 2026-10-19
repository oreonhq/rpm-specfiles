%global source0_hash 7a480c38b3b5bf492b3c386ff6bf2baa5905556dd4a7187e157368f35ca13b8b
Name:           needrestart
Version:        3.11
Release:        1%{?dist}
Summary:        Restart daemons after library updates
License:        GPL-2.0-or-later
URL:            https://github.com/liske/%{name}
Source0:        https://github.com/liske/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        debconf__needrestart.templates
Source2:        restart.d__auditd.service
Source3:        yum__plugin.py
Source4:        dnf__plugin.py
BuildArch:         noarch
Requires:          yum
Requires:          python2-subprocess32
Requires:          xz
Requires:          iucode-tool
%{?perl_default_filter}
# oreon:deps
BuildRequires:  debconf
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-generators
BuildRequires:  po-debconf
# /oreon:deps
%description
needrestart checks which daemons need to be restarted after library
upgrades. It is inspired by checkrestart from the debian-goodies
package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%make_build
%install
%make_install
mkdir -p %{buildroot}/%{_mandir}/man1
cp man/needrestart.1 %{buildroot}/%{_mandir}/man1/
%find_lang %{name}
%find_lang needrestart-notify
rm -rf %{buildroot}/%{perl_archlib}
mkdir -p %{buildroot}/usr/bin
mv %{buildroot}/usr/sbin/%{name} %{buildroot}/usr/bin/%{name}
cp %{SOURCE1} %{buildroot}/%{_datadir}/%{name}/needrestart.templates
cp %{SOURCE2} %{buildroot}/%{_sysconfdir}/%{name}/restart.d/auditd.service
chmod a+x %{buildroot}/%{_sysconfdir}/%{name}/restart.d/auditd.service
mkdir -p %{buildroot}/%{_sysconfdir}/yum/pluginconf.d %{buildroot}/usr/lib/yum-plugins
echo -e "[main]\nenabled=1\n" >%{buildroot}/%{_sysconfdir}/yum/pluginconf.d/needrestart.conf
cp %{SOURCE3} %{buildroot}/usr/lib/yum-plugins/needrestart.py
rm %{buildroot}/%{_sysconfdir}/%{name}/hook.d/20-rpm
mkdir -p %{buildroot}/%{_sysconfdir}/default
echo "IUCODE_TOOL_EXTRA_OPTIONS=--ignore-broken" >%{buildroot}/%{_sysconfdir}/default/intel-microcode
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
