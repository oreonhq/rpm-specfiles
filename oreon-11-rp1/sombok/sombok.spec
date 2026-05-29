%global source0_hash 14d9dcd3621bf9d591a7158aeac99b4d4a60296558173be51d57b54b8f9d70a2

Name:           sombok
Version:        2.4.0
Release:        25%{?dist}
Summary:        Unicode Text Segmentation Package
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND (GPL-2.0-or-later OR Artistic-1.0-Perl)
URL:            http://sf.net/projects/linefold/
Source0:        https://github.com/hatukanezumi/sombok/archive/sombok-2.4.0.tar.gz
# A multilib-safe wrapper, bug #1853260
Source1:        sombok.h

BuildRequires: make
BuildRequires:  libthai-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool


%description
Sombok library package performs Line Breaking Algorithm described in Unicode
Standards Annex #14 (UAX #14). East_Asian_Width informative properties defined
by Annex #11 (UAX #11) may be concerned to determine breaking positions. This
package also implements "default" Grapheme Cluster segmentation described in
Annex #29 (UAX #29).


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{name}-%{name}-%{version}


%build
autoreconf -vif
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Rename sombok.h to sombok-ARCH.h and install a sombok.h wrapper to avoid
# a file conflict on multilib systems, bug #1853260
mv %{buildroot}/%{_includedir}/sombok.h %{buildroot}/%{_includedir}/sombok-%{_arch}.h
install -m 0644 %{SOURCE1} %{buildroot}/%{_includedir}/sombok.h


%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS ChangeLog ChangeLog.REL1 NEWS README README.ja_JP
%{_libdir}/libsombok.so.*


%files devel
%{_includedir}/sombok*.h
%{_libdir}/libsombok.so
%{_libdir}/pkgconfig/sombok.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4.0-25
- Prepare for Oreon 11 (RP1)
