%global source0_hash c50814aa6743cd8c4e88c84a0cdd8889d883c3be122289be90c63d7d67883fc0
Name:           libsigrokdecode
Version:        0.5.3
Release:        1%{?dist}
Summary:        Basic API for running protocol decoders
License:        GPL-3.0-or-later
URL:            http://www.sigrok.org
Source0:        http://www.sigrok.org/download/source/%{name}/%{name}-%{version}.tar.gz
Patch0:         %{name}-0.5.3-python3.patch
Patch1:         0001-srd-drop-deprecated-PyEval_InitThreads-on-Python-3.9.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3-devel
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libsigrokdecode-devel -f %{oreon_filedir}/libsigrokdecode-devel.list

%changelog

%autochangelog
