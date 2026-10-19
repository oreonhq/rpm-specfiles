%global source0_hash 739c44b9fcd2c48541cfdd0b700b5d2f45f111457838103e43869b792137646c
Name:           rpld
Version:        1.8
Release:        1%{?dist}
Summary:        RPL/RIPL remote boot daemon
License:        GPL-1.0-or-later
URL:            http://gimel.esc.cam.ac.uk/james/rpld/index.html
Source0:        http://gimel.esc.cam.ac.uk/james/rpld/src/rpld-1.8-beta-1.tar.gz
Source2:	%{name}.sysconfig
Source3:	%{name}.service
Patch0:         rpld_1.8beta1-6.diff.gz
Patch1:         rpld-1.8-makefile.patch
Patch2:         rpld-c99.patch
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
Daemon to net-boot IBM style RPL boot ROMs (this is not the
same as the Novell IPX-style RPL protocol, despite the
name).

%post

%systemd_post rpld.service
%preun

%systemd_preun rpld.service
%postun

%systemd_postun rpld.service
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

for I in debian/patches/* ;
do
  patch -p1 -i ${I}
done

%patch -P1 -p1
%patch -P2 -p1

%build

make OPT="-fPIE -pie $RPM_OPT_FLAGS" %{?_smp_mflags}
make OPT="-fPIE -pie $RPM_OPT_FLAGS" %{?_smp_mflags}
mv LICENCE LICENSE
%install
mkdir -p $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man{8,5}}
make install DESTDIR=$RPM_BUILD_ROOT BINMODE=755 MANMODE=644
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
install -d $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -m 0644 %SOURCE2 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
install -d $RPM_BUILD_ROOT%{_unitdir}
install -m 0644 %SOURCE3 $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
