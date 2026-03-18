Name:           babeltrace
Version:        1.5.11
Release:        17%{?dist}
Summary:        Trace Viewer and Converter, mainly for the Common Trace Format
License:        MIT AND GPL-3.0-or-later WITH Bison-exception-2.2 AND LGPL-2.1-only AND BSD-4-Clause-UC
URL:            https://www.efficios.com/babeltrace
Source0:        https://www.efficios.com/files/%{name}/%{name}-%{version}.tar.bz2
Source1:        https://www.efficios.com/files/%{name}/%{name}-%{version}.tar.bz2.asc
# gpg2 --export --export-options export-minimal 7F49314A26E0DE78427680E05F1B2A0789F12B11 > gpgkey-7F49314A26E0DE78427680E05F1B2A0789F12B11.gpg
Source2:        gpgkey-7F49314A26E0DE78427680E05F1B2A0789F12B11.gpg
Patch0:         babeltrace-getaddrinfo.patch

BuildRequires:  bison >= 2.4
BuildRequires:  flex >= 2.5.35
BuildRequires:  glib2-devel >= 2.22.0
BuildRequires:  libuuid-devel
BuildRequires:  popt-devel >= 1.13
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  swig >= 2.0
BuildRequires:  elfutils-devel >= 0.154
BuildRequires:  autoconf automake libtool
BuildRequires:  gnupg2
BuildRequires:  make

Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description
This project provides trace read and write libraries, as well as a trace
converter. A plugin can be created for any trace format to allow its conversion
to/from another trace format.

The main format expected to be converted to/from is the Common Trace
Format (CTF). See http://www.efficios.com/ctf.


%package -n lib%{name}
Summary:        Common Trace Format Babel Tower

%description -n lib%{name}
This project provides trace read and write libraries, as well as a trace
converter. A plugin can be created for any trace format to allow its conversion
to/from another trace format.


%package -n lib%{name}-devel
Summary:        Common Trace Format Babel Tower
Requires:       lib%{name}%{?_isa} = %{version}-%{release} glib2-devel

%description -n lib%{name}-devel
This project provides trace read and write libraries, as well as a trace
converter. A plugin can be created for any trace format to allow its conversion
to/from another trace format.


%package -n python3-%{name}
Summary:        Common Trace Format Babel Tower
Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
This project provides trace read and write libraries, as well as a trace
converter. A plugin can be created for any trace format to allow its conversion
to/from another trace format.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
# Reinitialize libtool with the fedora version to remove Rpath
autoreconf -vif

export PYTHON=%{__python3}
export PYTHON_CONFIG=%{__python3}-config
%configure --disable-static --enable-python-bindings

make %{?_smp_mflags} V=1

%check
make check

%install
make DESTDIR=%{buildroot} install
find %{buildroot} -type f -name "*.la" -delete
# Clean installed doc
rm -f %{buildroot}/%{_pkgdocdir}/API.txt
rm -f %{buildroot}/%{_pkgdocdir}/LICENSE
rm -f %{buildroot}/%{_pkgdocdir}/gpl-2.0.txt
rm -f %{buildroot}/%{_pkgdocdir}/mit-license.txt
rm -f %{buildroot}/%{_pkgdocdir}/std-ext-lib.txt

%ldconfig_scriptlets  -n lib%{name}

%files
%doc ChangeLog
%doc doc/lttng-live.txt
%{_bindir}/%{name}*
%{_mandir}/man1/*.1*

%files -n lib%{name}
%doc doc/API.txt
%doc std-ext-lib.txt
%{!?_licensedir:%global license %%doc}
%license LICENSE gpl-2.0.txt mit-license.txt
%{_libdir}/*.so.*

%files -n lib%{name}-devel
%{_prefix}/include/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/babeltrace.pc
%{_libdir}/pkgconfig/babeltrace-ctf.pc

%files -n python3-%{name}
%{python3_sitearch}/babeltrace
%{python3_sitearch}/babeltrace*.egg-info


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.11-17
- Prepare for Oreon 11 (RP1)
