%global source1_hash b11744dbee03728bdedd619b442138afb29d25cfebbd2849e9876f4a10530480
%global source0_hash 67b43aaaef5c951fa7af1a557cf7201a11fe89876b7c22ba0a03cbc316db5a9c
%global source2_key_fpr 7F49314A26E0DE78427680E05F1B2A0789F12B11
Name:           babeltrace
Version:        1.5.11
Release:        17%{?dist}
Summary:        Trace Viewer and Converter, mainly for the Common Trace Format
License:        MIT AND GPL-3.0-or-later WITH Bison-exception-2.2 AND LGPL-2.1-only AND BSD-4-Clause-UC
URL:            https://www.efficios.com/babeltrace
Source0:        https://www.efficios.com/files/%{name}/%{name}-%{version}.tar.bz2
Source1:        https://www.efficios.com/files/%{name}/%{name}-%{version}.tar.bz2.asc
Source2:        gpgkey-7F49314A26E0DE78427680E05F1B2A0789F12B11.gpg
Patch0:         babeltrace-getaddrinfo.patch
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  elfutils-devel
BuildRequires:  flex
BuildRequires:  glib2-devel
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  popt-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  swig
# /oreon:deps
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

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

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
rm -f %{buildroot}/%{_pkgdocdir}/API.txt
rm -f %{buildroot}/%{_pkgdocdir}/LICENSE
rm -f %{buildroot}/%{_pkgdocdir}/gpl-2.0.txt
rm -f %{buildroot}/%{_pkgdocdir}/mit-license.txt
rm -f %{buildroot}/%{_pkgdocdir}/std-ext-lib.txt
%ldconfig_scriptlets  -n lib%{name}
%oreon_autofiles libbabeltrace usr/*/lib*.so.*
%oreon_autofiles libbabeltrace-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles python3-babeltrace usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libbabeltrace -f %{oreon_filedir}/libbabeltrace.list
%files -n libbabeltrace-devel -f %{oreon_filedir}/libbabeltrace-devel.list
%files -n python3-babeltrace -f %{oreon_filedir}/python3-babeltrace.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.11-17
- Prepare for Oreon 11 (RP1)
