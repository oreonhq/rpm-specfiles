Name:		pps-tools
Version:	1.0.3
Release:	12%{?dist}
Summary:	LinuxPPS user-space tools

License:	GPL-2.0-or-later
URL:		https://github.com/redlab-i/pps-tools
Source0:	https://github.com/redlab-i/pps-tools/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 89163e29f1a4a0a702bbe25b900fd37d2eb86442329cefee58847e57e1964d7a
%global source0_file pps-tools-1.0.3.tar.gz
# oreon url source checksums end

BuildRequires: make
BuildRequires:	gcc

%description
This package includes the LinuxPPS user-space tools.

%package devel
Summary: LinuxPPS PPSAPI header file

%description devel
This package includes the header needed to compile PPSAPI (RFC-2783)
applications.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/pps-tools-1.0.3.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "89163e29f1a4a0a702bbe25b900fd37d2eb86442329cefee58847e57e1964d7a" || { echo "oreon: Source0 SHA256 mismatch for pps-tools-1.0.3.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" make %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/sys}
install -m755 -t $RPM_BUILD_ROOT%{_bindir} \
	ppsctl ppsfind ppsldisc ppstest ppswatch
install -p -m644 -t $RPM_BUILD_ROOT%{_includedir}/sys timepps.h

%files
%license COPYING
%{_bindir}/pps*

%files devel
%license COPYING
%{_includedir}/sys/timepps.h

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.3-12
- Import
