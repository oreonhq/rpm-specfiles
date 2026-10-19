%global source0_hash 9ed9feabcded713d4ded38c8cebf36a3b08f0042ef7934a0e2b2409da56e649b
Name:             st
Version:          0.9.3
Release:        1%{?dist}
Summary:        A simple terminal implementation for X
%global           _stsourcedir %{_usrsrc}/%{name}-user-%{version}-%{release}
License:          MIT
URL:              http://%{name}.suckless.org/
Source0:        http://dl.suckless.org/%{name}/%{name}-%{version}.tar.gz
Source1:          %{name}.desktop
Source2:          %{name}-user
Source3:          %{name}-user.1
Requires:         font(liberationmono)
Requires:         ncurses-base
Requires(post):   %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
# oreon:deps
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description
A simple virtual terminal emulator for X which sucks less.

%package user
Summary:          Sources and tools for user configuration of st
License:          MIT
Requires:         %{name}%{?_isa} = %{version}-%{release}
Requires:         binutils
Requires:         coreutils
Requires:         findutils
Requires:         gcc
Requires:         libX11-devel
Requires:         libXext-devel
Requires:         libXft-devel
Requires:         make
Requires:         patch
Requires:         redhat-rpm-config
%description user
Source files for st and a launcher/builder wrapper script for
customized configurations.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# terminfo entries are provided by ncurses-base
sed -e "/tic .*st.info/d" -i Makefile

%build

CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}" make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}
mv %{buildroot}%{_bindir}/%{name}{,-fedora}
install -pm755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}-user
install -Dpm644 %{SOURCE3} %{buildroot}%{_mandir}/man1/%{name}-user.1
for file in \
    %{buildroot}%{_bindir}/%{name}-user \
    %{buildroot}%{_mandir}/man1/%{name}-user.1; do
sed -i -e 's/VERSION/%{version}/' \
       -e 's/RELEASE/%{release}/' \
       ${file}
done
mkdir -p %{buildroot}%{_stsourcedir}
install -m644 * \
    %{buildroot}%{_stsourcedir}
touch %{buildroot}%{_bindir}/%{name}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
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
%files -n st-user -f %{oreon_filedir}/st-user.list

%changelog

%autochangelog
