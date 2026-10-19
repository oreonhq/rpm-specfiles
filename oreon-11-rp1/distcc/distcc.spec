%global source0_hash 37a34c9555498a1168fea026b292ab07e7bb394715d87d8403e0c33b16d2d008
%global _lto_cflags %nil
Name:       distcc
Version:    3.4
Release:        1%{?dist}
Summary:        Distributed C/C++ compilation
License:    GPL-2.0-or-later
URL:        https://github.com/distcc/distcc
Source0:        https://github.com/distcc/distcc/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    hosts.sample
Source2:    distccd.service
Patch0:     distcc-localhost.patch
Patch1:     crash.patch
Patch2:     479.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  avahi-devel
BuildRequires:  binutils-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-devel
BuildRequires:  krb5-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pango-devel
BuildRequires:  popt-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd-rpm-macros
BuildRequires:  which
# /oreon:deps
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
install -Dm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/hosts
install -Dm 0644 contrib/redhat/sysconfig $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/distccd
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -Dm 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/distccd.service
mkdir -p $RPM_BUILD_ROOT/usr/lib/distcc
mkdir -p $RPM_BUILD_ROOT/usr/lib/gcc-cross
if [ ! -d $RPM_BUILD_ROOT/usr/lib64 ]; then
  mkdir -p $RPM_BUILD_ROOT/usr/lib64
fi
ln -s /usr/lib/distcc $RPM_BUILD_ROOT/usr/lib64/distcc
rm -rf $RPM_BUILD_ROOT%{_docdir}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post server

%systemd_post distccd.service
%{_sbindir}/update-distcc-symlinks > /dev/null 2>&1
%preun server

%systemd_preun distccd.service
%postun server

%systemd_postun_with_restart distccd.service
%files -f %{oreon_filedir}/main.list
%files -n distcc-gnome -f %{oreon_filedir}/distcc-gnome.list
%files -n distcc-server -f %{oreon_filedir}/distcc-server.list

%changelog

%autochangelog
