# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 aeab12754f557cba3ce2950a2029963d817490df7edb49880008b34d7ff8feba
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           libnetfilter_cttimeout
Version:        1.0.0
Release:        29%{?dist}
Summary:        Timeout policy tuning for Netfilter/conntrack
License:        GPL-2.0-or-later
URL:            http://netfilter.org
Source0:        http://netfilter.org/projects/%{name}/files/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  libmnl-devel >= 1.0.0, pkgconfig, kernel-headers
BuildRequires: make

%description
This infrastructure allows you to define fine-grain timeout
policies per flow. Basically, from user-space, you can create
timeout policy objects via nfct_timeout_alloc(), set the
policy attributes, via nfct_timeout_*_attr_set(), and then
build the ctnetlink message to communicate this new timeout
policy to the kernel.

%package        devel
Summary:        Timeout policy tuning for Netfilter/conntrack
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libmnl-devel >= 1.0.0
Requires:       kernel-headers

%description    devel
This infrastructure allows you to define fine-grain timeout
policies per flow. Basically, from user-space, you can create
timeout policy objects via nfct_timeout_alloc(), set the
policy attributes, via nfct_timeout_*_attr_set(), and then
build the ctnetlink message to communicate this new timeout
policy to the kernel.

%prep
%oreon_verify_sources
%setup -q

%build
%configure --disable-static

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc COPYING README
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/libnetfilter_cttimeout
%{_includedir}/libnetfilter_cttimeout/*.h

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.0-29
- Import
