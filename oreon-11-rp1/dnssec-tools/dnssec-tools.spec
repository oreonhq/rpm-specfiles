%global source0_hash c12fe51a94607f3ae340a8f72aa5deb8a846edb3b15e78dbaa3c5ddffca58911
Summary:        A suite of tools for managing dnssec aware DNS usage
Name: dnssec-tools
Version: 2.2.3
Release:        1%{?dist}
License: LicenseRef-Callaway-BSD
URL: http://www.dnssec-tools.org/
Source0:        https://www.hardakers.net/software/%{name}-%{version}.tar.gz
Source1: dnssec-tools-dnsval.conf
Source2: libval-config
Requires: dnssec-tools-perlmods, bind, perl(Getopt::GUI::Long)
Requires: perl(GraphViz)
Patch5: dnssec-tools-linux-conf-paths-1.13.patch
Patch13: dnssec-tools-2.0-autoconf-for-aarch64.patch
Patch17: dnssec-tools-new-2017-key.patch
Patch18: dnssec-tools-new-openssl-APIs.patch
Patch19: 7287c6b96422e499560fb10b95c1a481ea82656d.patch
Patch20: dnssec-tools-2.2.3-link-libval-threads-with-libs.patch
Patch21: dnssec-tools-2.2.3-add_ifdedf_to_engine.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
# /oreon:deps
%description

The goal of the DNSSEC-Tools project is to create a set of tools,
patches, applications, wrappers, extensions, and plugins that will
help ease the deployment of DNSSEC-related technologies.

%package perlmods
Summary: Perl modules supporting DNSSEC (needed by the dnssec-tools)
Requires: perl(Getopt::GUI::Long)
%description perlmods

The dnssec-tools project comes with a number of perl modules that are
required by the DNSSEC tools themselves as well as modules that are
useful for other developers.

%package libs
Summary: C-based libraries for dnssec aware tools
Requires: openssl
%description libs
C-based libraries useful for developing dnssec aware tools.

%package libs-devel
Summary: C-based development libraries for dnssec aware tools
Requires: dnssec-tools-libs = %{version}-%{release}
%description libs-devel
C-based libraries useful for developing dnssec aware tools.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P5 -p0 
#%%patch6 -p2
#%%patch12 -p2
#%%patch13 -p2
#%%patch14 -p2
#%%patch15 -p2
#%%patch16 -p2
#%%patch17 -p2
#%%patch18 -p2
%patch -P19 -p2
%patch -P20 -p1 -b .link-with-libs
%patch -P21 -p1

%build

%configure --with-validator-testcases-file=%{_datadir}/dnssec-tools/validator-testcases --with-perl-build-args="INSTALLDIRS=vendor OPTIMIZE='$RPM_OPT_FLAGS'" --sysconfdir=/etc --with-root-hints=/etc/dnssec-tools/root.hints --with-resolv-conf=/etc/dnssec-tools/resolv.conf --disable-static --with-nsec3 --with-ipv6 --with-dlv --disable-bind-checks
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' validator/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' validator/libtool
make CCFLAGS="-D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64"
%install
rm -rf %{buildroot}
make install DESTCONFDIR=%{buildroot}/etc/dnssec-tools/ DESTDIR=%{buildroot} QUIET=
%{__install} -m 644 %{SOURCE1} %{buildroot}/etc/dnssec-tools/dnsval.conf
%{__install} -m 644 validator/etc/root.hints %{buildroot}/etc/dnssec-tools/root.hints
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name perllocal.pod -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*
rm -f %{buildroot}%{_libdir}/*.la
mv ${RPM_BUILD_ROOT}/%{_bindir}/libval-config ${RPM_BUILD_ROOT}/%{_bindir}/libval-config-%{_arch}
install -m 755 %SOURCE2 ${RPM_BUILD_ROOT}/%{_bindir}/libval-config
%ldconfig_scriptlets libs
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n dnssec-tools-perlmods -f %{oreon_filedir}/dnssec-tools-perlmods.list
%files -n dnssec-tools-libs -f %{oreon_filedir}/dnssec-tools-libs.list
%files -n dnssec-tools-libs-devel -f %{oreon_filedir}/dnssec-tools-libs-devel.list

%changelog

%autochangelog
