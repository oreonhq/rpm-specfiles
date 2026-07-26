%global source0_hash 96cc377e66770659392a4bb02ec6c7b68864f9b5279f33a13c0590a2bef2aa5d

%global __requires_exclude perl\\(.*[.]pl\\)|\/bin\/bash
%global modulename mlmmj
%global selinuxtype targeted

Name:           mlmmj
Version:        1.8.0
Release:        1%{?dist}
Summary:        A simple and slim mailing list manager inspired by ezmlm
License:        MIT
URL:            https://codeberg.org/mlmmj/mlmmj
Source0:        https://codeberg.org/%{name}/%{name}/releases/download/%{name}-%{version}.tar.gz
Source1:        %{modulename}.te
Source2:        %{modulename}.fc
Source3:        README.SELinux

BuildRequires:  gcc
BuildRequires:  findutils
BuildRequires:  kyua
BuildRequires:  libatf-c-devel
BuildRequires:  libatf-sh-devel
BuildRequires:  make

%description
Mlmmj(Mailing List Management Made Joyful) is a simple and slim mailing list 
manager (MLM) inspired by ezmlm. It works with many different Mail Transport 
Agents (MTAs) and is simple for a system adminstrator to install, configure 
and integrate with other software. As it uses very few resources, and requires
no daemons, it is ideal for installation on systems where resources are 
limited, such as Virtual Private Servers (VPSes).

Although it doesn't aim to include every feature possible, but focuses on 
staying mean and lean, and doing what it does do well, it does have a great 
set of features, including:

- Archive
- Custom headers / footer
- Fully automated bounce handling (similar to ezmlm)
- Complete requeueing functionality
- Moderation functionality
- Subject prefix
- Subscribers only posting
- Regular expression access control
- Functionality to retrieve old posts
- Web interface
- Digests
- No-mail subscription
- VERP support
- Delivery Status Notification (RFC1891) support
- Rich, customisable texts for automated operations

%package        selinux
Summary:        SELinux support for mlmmj
BuildArch:      noarch
Requires:       %{name} = %{version}
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
BuildRequires:  selinux-policy-devel

%description selinux
This package adds SELinux enforcement support to mlmmj.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# SELinux
mkdir selinux
cp -p %{SOURCE1} selinux/%{modulename}.te
cp -p %{SOURCE2} selinux/%{modulename}.fc
cp -p %{SOURCE3} selinux/README.SELinux
touch selinux/%{modulename}.if

# Create a sysusers.d config file
cat >mlmmj.sysusers.conf <<EOF
u mlmmj - 'mlmmj user' %{_localstatedir}/spool/%{name} -
EOF

%build
%configure --enable-receive-strip
%make_build
# SELinux
make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp
bzip2 -9 %{modulename}.pp

%install
%make_install

mkdir -p %{buildroot}%{_localstatedir}/spool/%{name}
find contrib/ -type f -name *.pl -exec chmod -x {} ";"
find contrib/ -type f -name *.cgi -exec chmod -x {} ";"

# SELinux
install -D -m 0644 %{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2

install -m0644 -D mlmmj.sysusers.conf %{buildroot}%{_sysusersdir}/mlmmj.conf

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}

%files
%license COPYING
%doc AUTHORS ChangeLog FAQ README* TODO TUNABLES.md UPGRADE
%doc contrib/web/
%{_bindir}/*
%{_mandir}/man1/mlmmj*.1*
%{_datadir}/%{name}/
%dir %attr(0700,mlmmj,root) %{_localstatedir}/spool/%{name}
%{_sysusersdir}/mlmmj.conf

%files selinux
%doc selinux/README.SELinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.*
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename}

%changelog
%autochangelog
