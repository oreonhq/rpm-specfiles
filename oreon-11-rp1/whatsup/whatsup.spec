%global source0_hash 1b476e2e9f5c531b8dc1475ef45ce883be03c60aa2538535cabf7b736f9fe555
%global libname libnodeupdown
%ifnarch %{arm} s390 s390x
%global with_ib 1
%else
%global with_ib 0
%endif
Summary:        Node up/down detection utility
Name:          whatsup
Version:       1.14
Release:        51%{?dist}
License:       GPL-2.0-or-later
URL:           https://computing.llnl.gov/linux/whatsup.html
Source0:        http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}-1/%{name}-%{version}.tar.gz
Source1:       %{name}-hostsfile
Source2:       %{name}-pingd.service
Patch0:        %{name}-%{version}-bug#1117251.patch
Patch1:        %{name}-%{version}-Adjust-to-Autoconf-2.71.patch
Requires:      %{libname} = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  expat-devel
BuildRequires:  ganglia-devel
BuildRequires:  libgenders-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
# /oreon:deps
%description
Whatsup is a cluster node up/down detection utility.

Whatsup can quickly calculate and output the up and down nodes of a cluster.
Whatsup allows some tools, such as Pdsh, to operate more quickly by
not operating on down nodes. Whatsup calculates the up and down nodes of a
cluster through one of several possible backend tools
and several optional cluster node databases.

%package -n    %{libname}-devel
Summary:       Development headers for %{libname}
Requires:      %{libname} = %{version}-%{release}
%description -n %{libname}-devel
development headers for %{libname}

%package -n    %{libname}
Summary:       A cluster node up/down detection library
%description -n %{libname}
A cluster node up/down detection library, with different backends

%package -n    %{libname}-backend-ganglia
Summary:       Ganglia backend for %{libname}
Requires:      %{libname} = %{version}-%{release}
BuildRequires: ganglia-devel
%description -n %{libname}-backend-ganglia
Ganglia backend module for %{libname}

%package -n    %{libname}-backend-pingd
Summary:       Pingd backend for %{libname}
Requires:      %{libname} = %{version}-%{release}
Requires:      %{name}-pingd = %{version}-%{release}
%description -n %{libname}-backend-pingd
pingd backend module for %{libname}

%package -n    %{name}-pingd
Summary:       Pingd daemon for %{name}
Requires:      %{libname} = %{version}-%{release}
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts
Requires(postun): initscripts
%description -n %{name}-pingd
pingd daemon for %{name}

%package -n    perl-%{libname}
Summary:       Perl bindings for %{libname}
Requires:      %{libname} = %{version}-%{release}
%description -n perl-%{libname}
Perl bindings for %{libname}

%{?filter_setup:
%filter_provides_in %{perl_vendorarch}/.*\.so$
%filter_setup
}

%package -n    %{libname}-clusterlist-hostsfile
Summary:       Hostsfile clusterlist module for %{libname}
Requires:      %{libname} = %{version}-%{release}
%description -n %{libname}-clusterlist-hostsfile
Hostsfile clusterlist module for %{libname}

%package -n    %{libname}-clusterlist-genders
Summary:       Genders clusterlist module for %{libname}
Requires:      %{libname} = %{version}-%{release}
%description -n %{libname}-clusterlist-genders
Genders clusterlist module for %{libname}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0
%patch -P1 -p1

%build

%configure \
    --disable-static \
    --with-perl-extensions \
    --with-perl-vendor-arch \
    --with-perl-destdir="%{buildroot}"
make %{?_smpflags}
%install
DESTDIR=%{buildroot} make install
chmod -x %{buildroot}%{_sysconfdir}/nodeupdown.conf
chmod -x %{buildroot}%{_sysconfdir}/pingd.conf
install -m 644 -p %{SOURCE1} %{buildroot}%{_sysconfdir}/hostsfile
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name "*.bs" -exec rm -f {} \;
find %{buildroot} -type f -name "*.la" -exec rm -f {} \;
%{_fixperms} %{buildroot}/*
touch %{buildroot}%{_sysconfdir}/hostsfile
%ldconfig_scriptlets -n %{libname}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/*/lib*.so.*

%post -n %{name}-pingd

if [ $1 -eq 1 ] ; then 
    /sbin/chkconfig --add whatsup-pingd
fi
%preun -n %{name}-pingd

if [ $1 -eq 0 ] ; then
    /sbin/service whatsup-pingd stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del whatsup-pingd >/dev/null 2>&1 || :
fi
%postun -n %{name}-pingd

if [ $1 -ge 1 ] ; then
    /sbin/service whatsup-pingd condrestart
fi
%files -f %{oreon_filedir}/main.list
%files -n libnodeupdown-devel -f %{oreon_filedir}/libnodeupdown-devel.list
%files -n libnodeupdown -f %{oreon_filedir}/libnodeupdown.list
%files -n libnodeupdown-backend-ganglia -f %{oreon_filedir}/libnodeupdown-backend-ganglia.list
%files -n libnodeupdown-backend-pingd -f %{oreon_filedir}/libnodeupdown-backend-pingd.list
%files -n whatsup-pingd -f %{oreon_filedir}/whatsup-pingd.list
%files -n perl-libnodeupdown -f %{oreon_filedir}/perl-libnodeupdown.list
%files -n libnodeupdown-clusterlist-hostsfile -f %{oreon_filedir}/libnodeupdown-clusterlist-hostsfile.list
%files -n libnodeupdown-clusterlist-genders -f %{oreon_filedir}/libnodeupdown-clusterlist-genders.list

%changelog

%autochangelog
