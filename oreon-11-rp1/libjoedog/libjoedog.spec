%global source0_hash c951e8f54744e62b10082b9f05d154a136ddd8778b9e18a8a44b132517813348

%global _hardened_build 1
%global libname joedog
%global current 0

Name:           lib%{libname}
Version:        %{current}.1.2
Release:        29%{?dist}
Summary:        Repack of the common code base of fido and siege as shared library

# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://www.%{libname}.org/
Source0:        https://github.com/rmohr/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: libjoedog-c99.patch

%{?el5:BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)}
BuildRequires:  libtool
BuildRequires: make

%description
%{name} is a library containing the common code base of siege and fido by Jeff
Fulmer. It consists mostly of convenience wrapper functions and a hash table
implementation.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# old autotools want m4-dir to be present
mkdir -p m4
autoreconf -fi

%build
%configure --disable-static
# dirty hack to force immediate binding with hardenend build having
# autocrap's libtool pass the needed ld-specs to the linker.
sed -i -e 's! \\\$compiler_flags !&%{?_hardening_ldflags} !' libtool
make %{?_smp_mflags}

%install
%if 0%{?el5}
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%else
%make_install
%endif

install -Dpm 0644 config.h %{buildroot}%{_includedir}/%{libname}
rm -f %{buildroot}%{_libdir}/%{name}.la

%ldconfig_scriptlets

%files
%doc README ChangeLog COPYING
%{_libdir}/%{name}.so.%{current}
%{_libdir}/%{name}.so.%{version}

%files devel
%{_includedir}/%{libname}
%{_libdir}/%{name}.so

%changelog
%autochangelog
