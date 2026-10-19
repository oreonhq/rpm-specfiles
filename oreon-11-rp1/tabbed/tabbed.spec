%global source0_hash 0acf87457b7419e66fbfa3a9cec95ffb46d254c6b88b5e4bb7cc18c3a92008a8
Name:           tabbed
Version:        0.9
Release:        1%{?dist}
Summary:        Simple Xembed container manager
%global         _tabbedsourcedir %{_usrsrc}/tabbed-user-%{version}-%{release}
License:        MIT
URL:            http://tools.suckless.org/tabbed
Source0:        http://dl.suckless.org/tools/%{name}-%{version}.tar.gz
Source1:        %{name}-user
Source2:        %{name}-user.1
Source3:        xembed.1
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
# oreon:deps
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  fontconfig-devel
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description
A simple generic fronted to XEmbed aware applications.

%package user
Summary:        Tabbed sources and tools for user configuration
License:        MIT
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       binutils
Requires:       coreutils
Requires:       findutils
Requires:       fontconfig-devel
Requires:       gcc
Requires:       libX11-devel
Requires:       libXft-devel
Requires:       make
Requires:       patch
Requires:       redhat-rpm-config
Requires:       sed
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
%description user
Tabbed source files and a launcher/builder wrapper script for
customized configurations.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# XXX: To be dropped with 0.8+
cp %{SOURCE3} .
sed -e 's|/usr/local|%{_prefix}|g' \
    -e 's|/usr/lib|%{_libdir}|g' \
    -e 's|-std=c99 -pedantic -Wall -Os|%{optflags}|g' \
    -e 's|-s\b||' \
    -e 's|\(${LIBS}\)|\1 %{?__global_ldflags}|' \
    -i config.mk
sed -i 's!^\(\t\+\)@!\1!' Makefile 

%build

make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
mv %{buildroot}%{_bindir}/%{name}{,-fedora}
install -pm755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}-user
install -Dpm644 %{SOURCE2} %{buildroot}%{_mandir}/man1/%{name}-user.1
for file in \
    %{buildroot}%{_bindir}/%{name}-user \
    %{buildroot}%{_mandir}/man1/%{name}-user.1; do
sed -i -e 's/VERSION/%{version}/' \
       -e 's/RELEASE/%{release}/' \
       ${file}
done
mkdir -p %{buildroot}%{_tabbedsourcedir}
install -m644 arg.h config.def.h config.mk Makefile tabbed.c xembed.c \
     %{buildroot}%{_tabbedsourcedir}
touch %{buildroot}%{_bindir}/%{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre

[ -L %{_bindir}/%{name} ] || rm -f %{_bindir}/%{name}
%post

%{_sbindir}/update-alternatives --install %{_bindir}/%{name} %{name} \
    %{_bindir}/%{name}-fedora 10
%postun

if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}-fedora
fi
%post user

%{_sbindir}/update-alternatives --install %{_bindir}/%{name} %{name} \
    %{_bindir}/%{name}-user 20
%postun user

if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}-user
fi
%files -f %{oreon_filedir}/main.list
%files -n tabbed-user -f %{oreon_filedir}/tabbed-user.list

%changelog

%autochangelog
