%global source0_hash 37a34c9555498a1168fea026b292ab07e7bb394715d87d8403e0c33b16d2d008

%global _lto_cflags %nil

Name:       distcc
Version:    3.4
Release:    14%{?dist}
Summary:    Distributed C/C++ compilation
License:    GPL-2.0-or-later
URL:        https://github.com/distcc/distcc
Source0:    https://github.com/distcc/distcc/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    hosts.sample
Source2:    distccd.service
Patch0:     distcc-localhost.patch
Patch1:     crash.patch
Patch2:     479.patch

BuildRequires: automake
BuildRequires: autoconf
BuildRequires: which
BuildRequires: libtool
BuildRequires: popt-devel
BuildRequires: gtk3-devel
BuildRequires: pango-devel
BuildRequires: python3-devel
Buildrequires: python3-setuptools
BuildRequires: desktop-file-utils
BuildRequires: avahi-devel
BuildRequires: krb5-devel
BuildRequires: binutils-devel
BuildRequires: systemd-rpm-macros
BuildRequires: make

%description
distcc is a program to distribute compilation of C or C++ code across
several machines on a network. distcc should always generate the same
results as a local compile, is simple to install and use, and is often
two or more times faster than a local compile.

%package    gnome
Summary:    Gnome frontend of distcc monitoring tool
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description gnome
This package contains the Gnome frontend of the distcc monitoring tool.

%package     server
Summary:    Server for distributed C/C++ compilation
License:    GPL-2.0-or-later

Requires:   %{name}%{?_isa} = %{version}-%{release}
%{?systemd_requires}

%description server
This package contains the compilation server needed to use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p0
%patch -P 1 -p0
%patch -P 2 -p1

%build
export PYTHON='/usr/bin/python3'
./autogen.sh
export CFLAGS="%{optflags} -fcommon"
%configure --with-gtk --disable-Werror --with-auth
%make_build

%install
%make_install

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

# Install sample hosts file
install -Dm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/hosts

# Install sample distccd config file
install -Dm 0644 contrib/redhat/sysconfig $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/distccd

# Install distcdd unit file
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -Dm 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/distccd.service

# Install distcc dirs
mkdir -p $RPM_BUILD_ROOT/usr/lib/distcc
mkdir -p $RPM_BUILD_ROOT/usr/lib/gcc-cross
if [ ! -d $RPM_BUILD_ROOT/usr/lib64 ]; then
  mkdir -p $RPM_BUILD_ROOT/usr/lib64
fi
ln -s /usr/lib/distcc $RPM_BUILD_ROOT/usr/lib64/distcc

rm -rf $RPM_BUILD_ROOT%{_docdir}/*

%post server
%systemd_post distccd.service
%{_sbindir}/update-distcc-symlinks > /dev/null 2>&1

%preun server
%systemd_preun distccd.service

%postun server
%systemd_postun_with_restart distccd.service

%files
%license COPYING
%doc AUTHORS doc/* NEWS README.pump TODO
%doc INSTALL README survey.txt
%{_bindir}/distcc
%{_bindir}/distccmon-text
%{_bindir}/lsdistcc
%{_bindir}/pump
%{_mandir}/man1/distcc.*
%{_mandir}/man1/distccmon*
%{_mandir}/man1/pump*
%{_mandir}/man1/include_server*
%{_mandir}/man1/lsdistcc*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/hosts
%{python3_sitearch}/include_server*

%files gnome
%{_bindir}/distccmon-gnome
%{_datadir}/pixmaps/distccmon-gnome.png
%{_datadir}/applications/*.desktop

%files server
%license COPYING
%doc README
%{_bindir}/distccd
%{_unitdir}/*
%{_sysconfdir}/default/distcc
%{_sysconfdir}/distcc/*allow*
%{_mandir}/man1/distccd*
%config(noreplace) %{_sysconfdir}/sysconfig/distccd
%{_sbindir}/update-distcc-symlinks
%dir /usr/lib/distcc
/usr/lib64/distcc
%dir /usr/lib/gcc-cross

%changelog
%autochangelog
