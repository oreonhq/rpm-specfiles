%global source0_hash 9cf88763c8f32d206301eba39d8cf1fada0ce112ece70f10d20bde1d077ee850

Name:           rpld
Version:        1.8
Release:        0.44.beta1%{?dist}
Summary:        RPL/RIPL remote boot daemon
# No version specified.
License:        GPL-1.0-or-later
URL:            http://gimel.esc.cam.ac.uk/james/rpld/index.html
Source0:        http://gimel.esc.cam.ac.uk/james/rpld/src/rpld-1.8-beta-1.tar.gz
Source2:	%{name}.sysconfig
Source3:	%{name}.service
Patch0:         rpld_1.8beta1-6.diff.gz
Patch1:         rpld-1.8-makefile.patch
Patch2:         rpld-c99.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  byacc flex systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

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
# mkdir -p $RPM_BUILD_ROOT/usr/{sbin,share/man/man{8,5}}
mkdir -p $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man{8,5}}
make install DESTDIR=$RPM_BUILD_ROOT BINMODE=755 MANMODE=644

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

install -d $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -m 0644 %SOURCE2 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
install -d $RPM_BUILD_ROOT%{_unitdir}
install -m 0644 %SOURCE3 $RPM_BUILD_ROOT%{_unitdir}/%{name}.service

%files
%doc README LICENSE INSTALL rpld.conf.sample
%{_sbindir}/*
%{_mandir}/man[^3]/*
%{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/%{name}.service

%changelog
%autochangelog
