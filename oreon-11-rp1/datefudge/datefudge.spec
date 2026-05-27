%global source0_hash 0f7c0ca9bd2b0ef6aa01eaaf82e36b94b5424b6b70d49a8123478bf4cdfb2a2d

Name:		datefudge
Version:	1.27
Release:	%{?autorelease}%{!?autorelease:1%{?dist}}
Summary:	Fake the system date

License:	GPL-2.0-or-later
URL:		http://packages.qa.debian.org/d/datefudge.html
Source0:	http://cdn.debian.net/debian/pool/main/d/datefudge/%{name}_%{version}.tar.xz

BuildRequires:  gcc
BuildRequires: make
%description
This program (and preload library) fakes the system date so that 
programs think the wall clock is ... different. The faking is not 
complete; time-stamp on files are not affected in any way. This 
package is useful if you want to test the date handling of your 
programs without changing the system clock. 

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1
sed "s/VERSION := \$\(.*\)/VERSION := %{version}/g" -i Makefile
sed 's/-o root -g root/-p/g' -i Makefile

%build
LDFLAGS="%{__global_ldflags}" CFLAGS="%{optflags}" make libdir=%{_libexecdir} %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} libdir=%{_libexecdir}
chmod +x %{buildroot}/%{_libexecdir}/%{name}/datefudge.so #for stripping

%files
%{_libexecdir}/%{name}

%doc README COPYING
%{_mandir}/man1/datefudge.1*
%{_bindir}/datefudge

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.27-1
- Prepare for Oreon 11 (RP1)
