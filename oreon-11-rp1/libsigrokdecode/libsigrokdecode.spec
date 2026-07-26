%global source0_hash c50814aa6743cd8c4e88c84a0cdd8889d883c3be122289be90c63d7d67883fc0

Name:           libsigrokdecode
Version:        0.5.3
Release:        28%{?dist}
Summary:        Basic API for running protocol decoders
# Combined GPLv3+ and GPLv2+
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.sigrok.org
Source0:        %{url}/download/source/%{name}/%{name}-%{version}.tar.gz
# https://github.com/sigrokproject/libsigrokdecode/commit/9b0ad5177bd692f7556a4756bdbd2da81d9c34ce
# https://github.com/sigrokproject/libsigrokdecode/commit/c4c10b89396fe21a622b8c38dd5815a496b007bf
# https://github.com/sigrokproject/libsigrokdecode/commit/a6a5e2c8b0e9ecf5d69d0c237c8e8b717b82b36f
Patch0:         %{name}-0.5.3-python3.patch
# Upstream commit 0c35c5c5845d05e5f624c99d58af992d2f004446
Patch1:         0001-srd-drop-deprecated-PyEval_InitThreads-on-Python-3.9.patch

BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  python3-devel
BuildRequires:  autoconf libtool
BuildRequires: make

%description
%{name} is a library which provides (streaming) protocol decoding
functionality for sigrok.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

autoreconf -f

# Bytecompile script yet again wants to break our build. Retarded!
%global _python_bytecompile_errors_terminate_build 0

%build
%configure --disable-static
V=1 make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc README NEWS COPYING
%{_libdir}/libsigrokdecode.so.4*
%{_datadir}/libsigrokdecode/

%files devel
%{_includedir}/libsigrokdecode/
%{_libdir}/libsigrokdecode.so
%{_libdir}/pkgconfig/libsigrokdecode.pc

%changelog
%autochangelog
